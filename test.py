import token_rules
import grammar_rules
import ply.lex as lex
import ply.yacc as yacc
import sys

lexer = lex.lex(module = token_rules)
parser = yacc.yacc(module = grammar_rules)

while True:
    try:
        s = input("")

    except EOFError:
        break
    parser.parse(s)
