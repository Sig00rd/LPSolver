from parser import Parser

point = {"x1":5, "x2":3}
parser = Parser()

a = parser.evaluate("3 > 2 > 1", point)
print(a)
b = parser.evaluate("sin(x1)+17*tan(PI+1)^5", point)
print(b)

