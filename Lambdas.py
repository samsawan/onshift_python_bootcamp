# Note: Python moved reduce to functools in 3.2
# Guido didn't want it in the core
# https://www.artima.com/weblogs/viewpost.jsp?thread=98196
from functools import reduce

# Lambdas - single expression, can be multi variables, can call functions, done on one line
# Used for readability, not necessary though
# No arrows -> =>
# Actually just a keyword

# Is x greater than y?
gt_y = lambda x, y: x > y
print(gt_y(2, 5))
print(gt_y(32, 2))

s = reduce(lambda x, y: x - y, range(1, 6))
print(s)

# Lambdas with filter - selecting based on an expression
for x in filter(lambda x: x % 4 == 0, range(2, 21, 2)):
    print(x)


# Lambdas can call functions as well
def factorial(n):
    if n < 1:   # Anything less than 1 is 1
        return 1
    else:
        return_number = n * factorial(n - 1)  # recursive call
        return return_number


factorial_nums = map(lambda x: factorial(x), range(1, 6))
for num in factorial_nums:
    print(num)


# get odd numbers
odd_list = list(filter(lambda x: (x % 2 == 1), range(0, 20)))
print(odd_list)
