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
        'MULTIPLY',
        'EQUALS',
        'LESSEQUAL',
        'MOREEQUAL',
        'LESS',
        'MORE',
        'LPAREN',
        'RPAREN',
        'SIN',
        'COS',
        'TAN',
        'COTAN'

]

#=================================
t_PLUS = r"\+"
t_MINUS = r"\-"
t_MULTIPLY = r"\*"
t_DIVIDE = r"\/"
t_LESSEQUAL = r"\<\="
t_MOREEQUAL = r"\>\="
t_LESS = r"\<"
t_MORE = r"\>"
t_EQUALS = r"\="
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_VARIABLE = r"[a-zA-Z_][a-zA_Z_0-9]*"
t_SIN = r"sin"
t_COS = r"cos"
t_TAN = r"tan|tg"
t_COTAN = r"cotan|ctg"

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


#=================================
def t_error(t):
    print("Illegal characters!")
    t.lexer.skip()

#=================================
lexer = lex.lex()

lexer.input("sin(x1+cotan(x2))")

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
