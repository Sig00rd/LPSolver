import ply.lex as lex
import ply.yacc as yacc
import math


#=================================
tokens = [

        'INT',
        'FLOAT',
        'VARIABLE',
        'PLUS',
        'MINUS',
        'DIVIDE',
        'POW',
        'MULTIPLY',
        'COMPARISON',
        'LPAREN',
        'RPAREN',
        'FUNCTION',
        'CONST_PI',
        'CONST_E'
]

#=================================
t_PLUS = r"\+"
t_MINUS = r"\-"
t_MULTIPLY = r"\*"
t_DIVIDE = r"\/"
t_POW = r"\^"
t_LPAREN = r"\("
t_RPAREN = r"\)"

t_ignore = r" "
#=================================
def t_FLOAT(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_FUNCTION(t):
    r"sin|cos|tan|cotan|sqrt"
    return t

def t_CONST_PI(t):
    r"PI|pi"
    t.value = math.pi
    return t

def t_CONST_E(t):
    r"e"
    t.value = math.e
    return t

def t_COMPARISON(t):
    r"<=|>=|<|>"
    return t

#=================================
def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

t_VARIABLE = r"[a-zA-Z_][a-zA_Z_0-9]*"
