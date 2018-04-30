import ply.lex as lex
import ply.yacc as yacc
import sys


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
        'LESSEQUAL',
        'MOREEQUAL',
        'LESS',
        'MORE',
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
t_LESSEQUAL = r"\<\="
t_MOREEQUAL = r"\>\="
t_LESS = r"\<"
t_MORE = r"\>"
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
    r"sin|cos|tan|cotan"
    return t

def t_CONST_PI(t):
    r"PI|pi"
    t.value = 3.14
    return t

def t_CONST_E(t):
    r"e"
    t.value = 2.72
    return t

#=================================
def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

t_VARIABLE = r"[a-zA-Z_][a-zA_Z_0-9]*"
