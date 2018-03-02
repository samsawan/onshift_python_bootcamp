# Sample decorator from Ilya in a past bootcamp

import time

current_time_milliseconds = lambda: int(round(time.time() * 1000))


def performance_timer(func):
    def lets_time(*args, **kwargs):
        print(*args)
        print(func)
        start = current_time_milliseconds()
        result = func(*args, **kwargs)
        end = current_time_milliseconds()
        print('function duration:', end - start, 'milliseconds')
        return result

    return lets_time


@performance_timer
def loop_a_while(count):
    for i in range(0, count):
        123.456 * 789.0112


loop_a_while(100000000)
