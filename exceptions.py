# blank exception without fetching exception obeject
try:
    support = 0
    test = 5 / support
except:
    print('something happened')

# catching exception by type
try:
    support = 0
    test = 5 / support
except Exception:
    print('exception was thrown')

# catching exception with content
try:
    support = 0
    test = 5 / support
except Exception as exp:
    print(exp)

# catching exception with content and cleanup
try:
    support = 0
    test = 5 / support
except Exception as exp:
    print(exp)
finally:
    print('this will clean up when it fails')

# no need to catch exception. cleanup runs anyways
try:
    support = 1
    test = 5 / support
    print('no exception')
except Exception as exp:
    print(exp)
finally:
    print('this will clean up when it succeeds')