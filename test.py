from parser import Parser

point = {"x1":5.1, "x3":6.1}
parser = Parser()

a = parser.evaluate("2+5 < 2", point)

print(a)
