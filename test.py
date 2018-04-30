import token_rules
import ply.lex as lex
import ply.yacc as yacc
import sys

lexer = lex.lex(module=token_rules)

lexer.input("sin(x)+cos(x)")

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
