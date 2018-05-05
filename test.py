from parser import Parser

point = {"x1":5, "x2":3}
parser = Parser()

a = parser.evaluate("1 > 1 > 1", point)
print(a)
a =  parser.evaluate("1 > 2 > 3 ", point)
print(a)
a = parser.evaluate("3 > 2 > 1", point)
print(a)
a = parser.evaluate("1 <= 1 <= 1", point)
print(a)
