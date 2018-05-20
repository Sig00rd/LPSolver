import parser
import speaker
import solver_utils
import points

import multiprocessing
import time


def check_point(in_queue, out_queue, given_parser, constraints, goal_function_expression):
    while not in_queue.empty():
        point = in_queue.get()
        in_queue.task_done()

        if points.check_point_for_constraints(given_parser, point, constraints) is True:
            goal_function_value_at_point = given_parser.evaluate(goal_function_expression, point)
            out_queue.put((point, goal_function_value_at_point))


# magical numbers
POINTS_PER_ITERATION = 500
STARTING_RADIUS = 10
RELATIVE_DIFFERENCE_THRESHOLD = 0.005
ABSOLUTE_DIFFERENCE_THRESHOLD = 0.001
MAX_NUMBER_OF_RETRIES = 20
NUMBER_OF_PROCESSES = multiprocessing.cpu_count()


# get data from user
constraint_list = speaker.get_constraint_functions()
goal_function = speaker.get_goal_function()
objective = speaker.get_min_or_max()

# get variables from constraints
extractor = parser.VariableExtractor(constraint_list)
variable_list = extractor.extract_variables()

fail_count = 0


# set starting point, value at point and radius
starting_point = points.generate_starting_point(variable_list, STARTING_RADIUS)
current_radius = STARTING_RADIUS
current_best_point, current_best_value = starting_point, None
points_queue = multiprocessing.JoinableQueue()
valid_points = multiprocessing.Queue()
parsers = []
processes = []

for i in range(NUMBER_OF_PROCESSES):
    parsers.append(parser.PointParser())

while True:
    try:
        points.fill_queue_with_points(points_queue, POINTS_PER_ITERATION,
                                      current_best_point, current_radius, variable_list)

        for i in range(NUMBER_OF_PROCESSES):
            process = multiprocessing.Process(target=check_point,
                                              args=(points_queue, valid_points, parsers[i],
                                                    constraint_list, goal_function))
            processes.append(process)
            process.start()

        points_queue.join()
        time.sleep(0.01)

        try:
            current_step_best_point, current_step_best_value = points.get_best_point_and_value(valid_points, objective)

            if current_best_value is None:
                current_best_point = current_step_best_point
                current_best_value = current_step_best_value

            elif (objective == "max" and current_step_best_value > current_best_value)\
                    or (objective == "min" and current_step_best_value < current_best_value):

                differences = solver_utils.calculate_differences(current_best_value, current_step_best_value)
                current_radius = points.choose_new_radius(current_radius, current_best_point, current_step_best_point)
                current_best_point = current_step_best_point
                current_best_value = current_step_best_value
                print(current_best_value)

                if solver_utils.stop_condition(
                        RELATIVE_DIFFERENCE_THRESHOLD,
                        ABSOLUTE_DIFFERENCE_THRESHOLD,
                        differences):
                    break

        except points.QueueEmptyException:
            fail_count += 1
            if fail_count >= MAX_NUMBER_OF_RETRIES:
                break

    except KeyboardInterrupt:
        break


points.present(current_best_point, variable_list, current_best_value)

for p in multiprocessing.active_children():
    p.terminate()
