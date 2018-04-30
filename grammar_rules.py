import ply.yacc as yacc
from token_rules import tokens

def p_calc(p):
    '''
    calc : expression
         | empty
    '''
    print(p[1])

def p_expression(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None
