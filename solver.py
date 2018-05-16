from parser import Parser
import speaker
import solver_utils
import points


# magical numbers
POINTS_PER_ITERATION = 10000
STARTING_RADIUS = 1000

RELATIVE_DIFFERENCE_THRESHOLD = 0.005
ABSOLUTE_DIFFERENCE_THRESHOLD = 0.001
MAX_NUMBER_OF_RETRIES = 20


# get data from user
variable_list = speaker.get_variables()
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
    try:
        points_queue = points.generate_queue_of_points(POINTS_PER_ITERATION, current_best_point,
                                                       current_radius, variable_list)
        valid_points = []

        while not points_queue.empty():
            point = points_queue.get()
            if points.check_point_for_constraints(new_parser, point, constraint_list) is True:
                goal_function_value_at_point = new_parser.evaluate(goal_function, point)
                valid_points.append((point, goal_function_value_at_point))

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

        except points.ListEmptyError:
            fail_count += 1
            if fail_count >= MAX_NUMBER_OF_RETRIES:
                break
    except KeyboardInterrupt:
        break


points.present(current_best_point, variable_list, current_best_value)
