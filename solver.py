from parser import Parser
import random

# magical numbers
POINTS_PER_ITERATION = 100
STARTING_AREA = 10000
RELATIVE_DIFFERENCE_THRESHOLD = 0.01

variableNames = []
constraintFunctions = []

def getConstraintFunctions():
    while(True):
        newConstraint = input("Proszę wpisać ograniczenie lub kliknąć "+
                "enter aby zakończyć: ")
        if(newConstraint == ""):
            return
        constraintFunctions.append(newConstraint)

def getVariableNames():
    while(True):
        newVariable = input("Proszę wpisać nową zmienną lub kliknąć enter żeby "
        + "zakończyć: ")
        if(newVariable == ""):
            return
        variableNames.append(newVariable)

getVariableNames()
getConstraintFunctions()
point = {}
for name in variableNames:
    point[name] = random.uniform(0, STARTING_AREA)


parser = Parser()

for constraint in constraintFunctions:
    result = parser.evaluate(constraint, point)
    print(result)

