import token_rules

import ply.lex as lex
import ply.yacc as yacc

import math


class Parser:

    point = {}
    tokens = ()

    precedence = (
        ("nonassoc", "COMPARISON"),
        ("left", "PLUS", "MINUS"),
        ("left", "MULTIPLY", "DIVIDE"),
        ("right", "POW"),
        ("right", "UMINUS"),
    )

    def __init__(self):
        self.tokens = token_rules.tokens
        lex.lex(module=token_rules)
        yacc.yacc(module=self)

    def run(self):
        while True:
            try:
                s = input(">> ")
            except EOFError:
                break
            result = yacc.parse(s)
            print(result)

    def evaluate(self, function_expression, _point):
        self.point = _point

        try:
            a = yacc.parse(function_expression)
            return a
        except EOFError:
            print("Zły error")

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
        'expression : expression POW expression'
        p[0] = math.pow(p[1], p[3])

    def p_expression_starless_multiplication(self, p):
        'expression : term VARIABLE'
        p[0] = p[1] * self.point[p[2]]

#====================================================
    def p_expression_group(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_expression_function(self, p):
        'expression : FUNCTION LPAREN factor RPAREN'
        if p[1] == "sin":
            p[0] = math.sin(p[3])
        elif p[1] == "cos":
            p[0] = math.cos(p[3])
        elif p[1] == "tan":
            p[0] = math.tan(p[3])
        elif p[1] == "cotan":
            p[0] = 1/math.tan(p[3])

#====================================================
    def p_empty(self, p):
        'empty : '
        p[0] = None

#====================================================
    def p_error(self, p):
        pass
