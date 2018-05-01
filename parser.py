import grammar_rules
import token_rules

import ply.lex as lex
import ply.yacc as yacc

class Parser:

    def __init__(self):
        self.point = []
        lex.lex(module=token_rules)
        yacc.yacc(module=grammar_rules)

    def run(self):
        while True:
            try:
                s = input(">> ")
            except EOFError:
                break
            result = yacc.parse(s)
            print(result)

    def evaluate(self, function, _point):
        self.point = _point

        try:
            s = function
            a = yacc.parse(s)
            return a
        except EOFError:
            print("Zły error")
