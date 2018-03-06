# Pickling in Python is the equivalent of serializing and deserializing objects
import pickle

def write_file(filename,*args):
    # This with block is much like "try with resources"
    # Regardless of an exception being thrown, Python will close the file when done
    # Think of the cleanup as something being executed in finally
    # This happens without your needing to close it
    with open(filename) as the_file:
        the_file.write('Testing ')

def write_and_append_to_file(filename, *args):
    try:
        the_file = open(filename, 'a')
        the_file.write('Testing ')
        the_file.close()
    except Exception as exp:
        print('Trouble writing the file: ' + str(exp))


def print_to_file(filename,*args):
    the_file = open(filename, 'w')
    print('Testing redirecting output',file=the_file)
    the_file.close()

def print_and_append_to_file(filename,*args):
    the_file = open(filename, 'a')
    print('Testing redirecting output',file=the_file)
    the_file.close()

def read_file(filename,*args):
    the_file = open(filename,'r')
    lines = the_file.readlines()
    print(lines)
    the_file.close()

def write_pickled_object(filename, collection_to_pickle, mode = 'write', *args):
    the_file = open(filename,'wb') #wb = write bytes
    pickle.dump(collection_to_pickle,the_file)
    the_file.close()

def read_unpickled_object(filename,*args):
    the_file = open(filename, 'rb') # rb = read bytes
    unpickled_item = pickle.load(the_file)
    the_file.close()
    print('Unpickled item: ')
    print(unpickled_item)


# If this file doesn't exist, it will be created
write_file('test1.txt')
# If this file exists, it will be overwritten
print_to_file('test1.txt')

# If this file doesn't exist, it will be created
write_and_append_to_file('test2.txt')
# If this file exists, it will be appended to
print_and_append_to_file('test2.txt')

# Read an existing file
read_file('test1.txt')
# Read a non-existing file - hmm... maybe we should handle this exception
read_file('idontexist.txt')

# Pickling items
# After running the write, look at pythoncohort201802.pkl
my_python_cohort = ['Ishaan','Jeremiah','Bobby','Sam','Mason']
write_pickled_object('pythoncohort201802.pkl',my_python_cohort)
# Now read that file and write out the output
read_unpickled_object('pythoncohort201802.pkl')

# Other methods to know
# read(n) - # of characters to read (optional)
# seek(n) - reposition the cursor to a byte position
# tell() - identify current byte position

# readline()
# readlines()

# Note: The file stream object has an iterator, so you can use a for loop to iterate through the stream without
# calling read
line_number = 0
with open('zen.txt','r') as my_zen:
    for zen_line in my_zen:
        line_number+= 1
        print("="*78 if zen_line.strip() == "" else zen_line.strip() )

# Note - EOF may return an empty string