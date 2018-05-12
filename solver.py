from typing import Dict, Any

from parser import Parser
import speaker
import points

from queue import Queue
import math


# magical numbers
POINTS_PER_ITERATION = 10000
STARTING_RADIUS = 500

DIFFERENCE_THRESHOLD = 5
MAX_NUMBER_OF_RETRIES = 5


# get data from user
variable_list = speaker.get_variables()
dziedzina = "r"
constraint_list = speaker.get_constraint_functions()
goal_function = speaker.get_goal_function()
objective = speaker.get_min_or_max()
new_parser = Parser()

fail_count = 0

# set starting point, value at point and radius
starting_point = points.generate_starting_point(variable_list, STARTING_RADIUS)
current_radius = STARTING_RADIUS
current_best_point, current_best_value = starting_point, None

while True:
    points_queue = Queue()
    valid_points = []

    for i in range(POINTS_PER_ITERATION):
        if dziedzina == "n":
            new_point = points.generate_point_int(current_best_point,
                                                  current_radius, variable_list)
        else:
            new_point = points.generate_point(current_best_point,
                                              current_radius, variable_list)
        points_queue.put(new_point)

    while not points_queue.empty():
        point = points_queue.get()
        if points.check_point_for_constraints(new_parser, point, constraint_list) is True:
            goal_function_value_at_point = new_parser.evaluate(goal_function, point)
            valid_points.append((point, goal_function_value_at_point))
        points_queue.task_done()

    try:
        current_step_best_point, current_step_best_value = points.get_best_point_and_value(valid_points, objective)

        if current_best_value is None:
            current_best_point = current_step_best_point
            current_best_value = current_step_best_value

        elif (objective == "max" and current_step_best_value > current_best_value)\
                or (objective == "min" and current_step_best_value < current_best_value):

            difference = math.fabs(current_step_best_value - current_best_value)
            current_radius = points.distance(current_best_point, current_step_best_point, variable_list)
            current_best_point = current_step_best_point
            current_best_value = current_step_best_value

            if difference < DIFFERENCE_THRESHOLD:
                break

    except points.ListEmptyError:
        fail_count += 1
        if fail_count >= MAX_NUMBER_OF_RETRIES:
            break


points.present(current_best_point, variable_list, current_best_value)
