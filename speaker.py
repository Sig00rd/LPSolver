def get_constraint_functions():
    constraint_list = []

    while True:
        new_constraint = input("Proszę wpisać ograniczenie lub kliknąć enter aby zakończyć: ")
        if new_constraint == "":
            return constraint_list
        constraint_list.append(new_constraint)


def get_variables():
    variable_list = []

    while True:
        new_variable = input("Proszę wpisać nową zmienną lub kliknąć enter aby zakończyć: ")
        if new_variable == "":
            return variable_list
        variable_list.append(new_variable)


def get_goal_function():
    goal_function = input("Proszę wpisać funkcję celu: ")
    return goal_function


def get_min_or_max():
    answer = input("Szukana jest minimalna (min) czy maksymalna (max) wartosc funkcji celu? min/max: ")
    if answer == "min" or answer == "max":
        return answer
    return
