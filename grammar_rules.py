import ply.yacc as yacc
import math
from token_rules import tokens

precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "MULTIPLY", "DIVIDE"),
    ("right", "POW"),
    ("right", "UMINUS"),
)


# For testing purposes
#====================================================
def p_calc(p):
    '''
    calc : expression
         | empty
    '''
    print(p[1])

#====================================================
def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]

def p_expression_constant(p):
    '''
    expression : CONST_PI
               | CONST_E
    '''
    p[0] = p[1]

def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = p[1]

def p_expression_u_minus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]
#====================================================
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
#====================================================
def p_expression_power(p):
    'expression : expression POW expression'
    p[0] = p[1] ** p[3]


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_trigonometric_function(p):
    'expression : FUNCTION LPAREN expression RPAREN'
    if p[1] == "sin":
        p[0] = math.sin(p[3])
    elif p[1] == "cos":
        p[0] = math.cos(p[3])
    elif p[1] == "tan":
        p[0] = math.tan(p[3])
    elif p[1] == "cotan":
        p[0] = 1/math.tan(p[3])

#====================================================
def p_empty(p):
    'empty : '
    p[0] = None

#====================================================
def p_error(p):
    print("Syntax error in input!")

