from parser import Parser

point = [1, 2, 3]
parser = Parser()

a = parser.evaluate("2+5 < 2", point)

print(a)
