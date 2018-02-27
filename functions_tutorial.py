# declaration
def function_name_lower_snake_case(param1, param2):
    print(param1, param2)
    return param1 + param2


# support for unknown number of positional arguments
def some_function(param1, *args):
    print('param1 =', param1)
    # the args come in as an tuple
    # args can be named whatever we want (*other, *anything, etc)
    print('remaing args = ', args)


# call function
some_function('test', 'another', 'value', 123, True)
# some_function() -> need at least one param otherwise youre gonna blow up
some_function('this will work with only one arg')


# support for keyword arguments
def other_function(param1, param2, **kwargs):
    print('param1 =', param1)
    print('param2 =', param2)
    print(kwargs)


# call function
other_function('sample', 'pretty', donkey='lobster', trout='turkey')
# this blow up will
# other_function('sample', 'neat', 'third')


# required THAN defaults THAN *args THAN **kwargs
def default_function(first, second='second', *args, **kwargs):
    print('first = ', first)
    print('second = ', second)
    print('args = ', *args)
    print('kwargs = ', **kwargs)


default_function('hello')
default_function('hello', 'third')
