import math
import random


class ListEmptyError(Exception):
    pass


def generate_point(previous_best_point, radius, variables):
    _point = {}
    for variable in variables:
        _point[variable] = random.uniform(previous_best_point[variable] - radius,
                                          previous_best_point[variable] + radius)
    return _point


def generate_point_int(previous_best_point, radius, variables):
    _point = {}
    for variable in variables:
        _point[variable] = random.randint(previous_best_point[variable] - radius,
                                          previous_best_point[variable] + radius)
    return _point


def generate_starting_point(variables, _starting_radius):
    _point = {}
    for variable in variables:
        _point[variable] = _starting_radius
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


def present(point, variables, best_value):
    if best_value is None:
        print("Nie znaleziono punktu spełniajacego założenia :-(")
    else:
        for variable in variables:
            print("Wartość: {0:8.8f} zmiennej {1}:".format(point[variable], variable))

        print("Wartość funkcji celu w tym punkcie: {:8.4f}".format(best_value))


def get_best_point_and_value(point_list, _objective):
    if not point_list:
        raise ListEmptyError

    else:
        _point, _value = point_list.pop()

    for point in point_list:
        new_point, new_point_value = point

        if _objective == "max":
            if new_point_value > _value:
                _point, _value = new_point, new_point_value
        else:
            if new_point_value < _value:
                _point, _value = new_point, new_point_value

    return _point, _value
