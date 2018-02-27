# declaration
def function_name_lower_snake_case(param1, param2):
    print(param1, param2)
    return param1 + param2


# support for unknown number of positional arguments
def some_function(param1, *args):
    print('param1 =', param1)
    print(args)


# call function
some_function('test', 'another', 'value', 123, True)


# support for keyword arguments
def other_function(param1, param2, **kwargs):
    print('param1 =', param1)
    print('param2 =', param2)
    print(kwargs)


# call function
other_function('sample', 'pretty', donkey='lobster', trout='turkey')

# you can also pass dicts for parameter