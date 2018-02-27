import traceback

def divide_by_zero():
    return 5 / 0


# blank exception without fetching exception object
try:
    divide_by_zero()
except:
    print('something happened')

# catching exception by type
try:
    divide_by_zero()
except Exception:
    print('exception was thrown')

# catching exception with content
try:
    divide_by_zero()
except ZeroDivisionError:
    print('Quit dividing by zero')
except Exception as exp:
    print('Not gonna hit this')

# catching exception with content and cleanup
try:
    divide_by_zero()
except Exception as exp:
    print(exp)
finally:
    print('this will clean up when it fails')

# no need to catch exception. cleanup runs anyways
try:
    divide_by_zero()
    print('no exception')
except Exception as exp:
    traceback.print_stack()
finally:
    print('this will clean up when it succeeds')
