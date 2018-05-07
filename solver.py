from parser import Parser
import speaker

from sortedcontainers import SortedDict
from queue import Queue
import random


def generate_point(area):
    _point = {}
    for name in variable_list:
        _point[name] = random.uniform(0, area)
    return _point


def check_point_for_constraints(parser, given_point):
    for constraint in constraint_list:
        if parser.evaluate(constraint, given_point) is not True:
            return False
    return True


# magical numbers
POINTS_PER_ITERATION = 1000
STARTING_AREA = 10000
RELATIVE_DIFFERENCE_THRESHOLD = 0.01

# get data from user
variable_list = speaker.get_variables()
constraint_list = speaker.get_constraint_functions()
goal_function = speaker.get_goal_function()
objective = speaker.get_min_or_max()

points_queue = Queue()
valid_points = SortedDict()
new_parser = Parser()


for i in range(POINTS_PER_ITERATION):
    new_point = generate_point(STARTING_AREA)
    points_queue.put(new_point)


while not points_queue.empty():
    point = points_queue.get()
    if check_point_for_constraints(new_parser, point) is True:
        goal_function_value_at_point = new_parser.evaluate(goal_function, point)
        valid_points[goal_function_value_at_point] = point
    points_queue.task_done()


if objective == "max":
    current_best_value, current_best_point = valid_points.popitem()
elif objective == "min":
    current_best_value, current_best_point = valid_points.popitem(False)

print(current_best_value)

