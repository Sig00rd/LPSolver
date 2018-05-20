import token_rules

import ply.lex as lex
import ply.yacc as yacc

import math


class Parser:
    tokens = token_rules.tokens

    def __init__(self):
        self.lexer = lex.lex(module=token_rules)


class VariableExtractor(Parser):
    def __init__(self):
        super().__init__()
        self.variable_list = []
        self.expression_list = []

    def extract_variables(self, expression_list):
        self.expression_list = expression_list
        for expression in self.expression_list:
            self.extract_from_expression(expression)
        return self.variable_list

    def extract_from_expression(self, expression):
        token_list = self.build_token_list(expression)
        for token in token_list:
            if token.type == "VARIABLE":
                variable = token.value
                if not self.variable_list.count(variable):
                    self.variable_list.append(variable)

    def build_token_list(self, expression):
        token_list = []
        self.lexer.input(expression)
        while True:
            token = self.lexer.token()
            if token:
                token_list.append(token)
            else:
                break
        return token_list


class PointParser(Parser):
    precedence = (
        ("nonassoc", "COMPARISON"),
        ("left", "PLUS", "MINUS"),
        ("left", "MULTIPLY", "DIVIDE"),
        ("right", "POW"),
        ("right", "UMINUS"),
    )

    def __init__(self):
        super().__init__()
        self.yacc = yacc.yacc(module=self)
        self.point = {}

    def run(self):
        while True:
            try:
                s = input(">> ")
            except EOFError:
                break
            result = self.yacc.parse(s)
            print(result)

    def evaluate(self, function_expression, _point):
        self.point = _point
        try:
            a = self.yacc.parse(function_expression)
            return a
        except EOFError:
            print("Groźny błąd!")

#====================================================
    def p_result_calc(self, p):
        '''
        result : expression
               | empty
        '''
        p[0] = p[1]

    def p_result_doublecomp(self, p):
        'result : expression COMPARISON expression COMPARISON expression'
        p[0] = (self.evaluate(str(p[1]) + str(p[2]) + str(p[3]), self.point) and
                self.evaluate(str(p[3]) + str(p[4]) + str(p[5]), self.point))

    def p_result_comp(self, p):
        'result : expression COMPARISON expression'
        if p[2] == "<=":
            p[0] = (p[1] <= p[3])
        elif p[2] == ">=":
            p[0] = (p[1] >= p[3])
        elif p[2] == "<":
            p[0] = (p[1] < p[3])
        elif p[2] == ">":
            p[0] = (p[1] > p[3])

#====================================================
    def p_factor_constant_or_number(self, p):
        '''
        factor     : INT
                   | FLOAT
                   | CONST_PI
                   | CONST_E
        '''
        p[0] = p[1]

    def p_factor_variable(self, p):
        'factor : VARIABLE'
        p[0] = self.point[p[1]]

    def p_expression_u_minus(self, p):
        'expression : MINUS expression %prec UMINUS'
        p[0] = -p[2]

    def p_expression_term(self, p):
        'expression : term'
        p[0] = p[1]

    def p_term_factor(self, p):
        'term : factor'
        p[0] = p[1]

#====================================================
    def p_expression_plus(self, p):
        'expression : expression PLUS expression'
        p[0] = p[1] + p[3]

    def p_expression_minus(self, p):
        'expression : expression MINUS expression'
        p[0] = p[1] - p[3]

    def p_term_multiply(self, p):
        'term : term MULTIPLY factor'
        p[0] = p[1] * p[3]

    def p_expression_divide(self, p):
        'term : term DIVIDE factor'
        p[0] = p[1] / p[3]

    def p_expression_power(self, p):
        'factor : factor POW factor'
        p[0] = math.pow(p[1], p[3])

    def p_expression_starless_multiplication(self, p):
        'expression : term VARIABLE'
        p[0] = p[1] * self.point[p[2]]

#====================================================
    def p_factor_group(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_expression_function(self, p):
        'factor : FUNCTION LPAREN expression RPAREN'
        if p[1] == "sin":
            p[0] = math.sin(p[3])
        elif p[1] == "cos":
            p[0] = math.cos(p[3])
        elif p[1] == "tan":
            p[0] = math.tan(p[3])
        elif p[1] == "cotan":
            p[0] = 1/math.tan(p[3])

    def p_empty(self, p):
        'empty : '
        p[0] = None

    def p_error(self, p):
        pass