import math
import random


def generate_point(previous_best_point, radius, variables):
    _point = {}
    for variable in variables:
         _point[variable] = random.uniform(previous_best_point[variable] - radius,
                                           previous_best_point[variable] + radius)
    return _point


def generate_point_int(previous_best_point, radius, variables):
    _point = {}
    for variable in variables:
        _point[variable] = random.randrange(int(previous_best_point[variable] - radius),
                                            int(previous_best_point[variable] + radius))
    return _point


def generate_starting_point(variables, start_radius):
    _point = {}
    for variable in variables:
        _point[variable] = 0
    return _point


def check_point_for_constraints(parser, given_point, constraints):
    for constraint in constraints:
        if parser.evaluate(constraint, given_point) is not True:
            return False
    return True


def distance(point1, point2, variables):
    total_distance = 0.0
    for variable in variables:
        total_distance += (point1[variable] - point2[variable])**2
    return math.sqrt(total_distance)


def present(point, variables):
    for variable in variables:
        print("Wartosc: %9.7f zmiennej :" % point[variable], variable)

