import math


def stop_condition(relative_diff_threshold, absolute_diff_threshold, differences):
    absolute_difference, relative_difference = differences

    if absolute_difference < absolute_diff_threshold or relative_difference < relative_diff_threshold:
        return True


def calculate_differences(val1, val2):
    absolute_difference = math.fabs(val1 - val2)
    relative_difference = absolute_difference/math.fabs(val1)

    return absolute_difference, relative_difference
