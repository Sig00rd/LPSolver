from parser import Parser

point = {"x1":5, "x2":3}
parser = Parser()

a = parser.evaluate("-2/3x2", point)
print(a)
b = parser.evaluate("sin(x1)+17*tan(PI+1)^5", point)
print(b)

