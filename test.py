from parser import Parser

point = {"x1":5, "x2":3}
parser = Parser()

a = parser.evaluate("x1 < x2", point)
print(a)
a = parser.evaluate("x1 > x2", point)
print(a)
a = parser.evaluate("x1 >= x2 + 2", point)
print(a)
