import ply.yacc as yacc
from token_rules import tokens

def p_calc(p):
    '''
    calc : expression
         | empty
    '''
    print(p[1])

def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

def p_expression_multiply(p):
    'expression : expression MULTIPLY expression'
    p[0] = p[1] * p[3]

def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    p[0] = p[1] / p[3]

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
    print("Syntax error in input!")

