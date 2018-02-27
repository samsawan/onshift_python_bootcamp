# This is our introduction to collections

# Lists
my_music_collection = "Lindsey Stirling,David Garrett,2CELLOS,Dave Matthews Band,Alexey Igudesman,Brigid's Cross"
my_music_artists = my_music_collection.split(",")
print(type(my_music_artists))

# Using a for loop to iterate through the collection
# Similar to a foreach in C# or enhanced for loop in Java
for music_artist in my_music_artists:
    print(music_artist)

# Another sample list
sample_list = [1, 42, 'Mario','Luigi']
type(sample_list)

# Creating lists
new_list = list()
type(new_list)

# Notice the square brackets - list!
new_list2 = []
type(new_list2)

# If we want to remove the whole list, we can
del new_list
del new_list2

# How do we get the third element?
sample_list[___]

# Let's change the third element
sample_list[___] = 'Wario'
sample_list

# Let's change the last element with negative indexes
sample_list[-1] = "Waluigi"
sample_list

# Slicing Lists
sample_list[2:]
sample_list[-3:]

# To get rid of elements individually
del sample_list[0]

# Converting sequences to lists
large_list = [i for i in range(1,20)]
type(large_list)

large_list[-3:] # Last three elements of the list

large_list[5:] # Everything starting at the 6th element (0-based index) until the end
large_list[1::3] # Starting at the 2nd element, getting every 3rd element
large_list[:-20] # What if we go out of range?
large_list[20:] # What if we go out of range?
large_list[2:10:4] # Starting at the 3rd element, stopping at the 11th element, getting every 4th element
large_list[::1] # Starting at the beginning of the list, stopping at the end, get every element
large_list[::-1] # Traverse the list backwards
large_list[::-3] # Traverse backwards, getting every 3rd element

# Tuples
# We saw this in Session 1 when we passed a tuple of parameters to use with string formatting in the old style.
formatted_string = f"My name is %s, and my favorite %s is %s." % ("Sarah","musical instrument","double bass")
print(formatted_string)

# Sample tuple
sample = (123,'test',123.456)
sample
type(sample)

# Creating tuples
new_tup = tuple()
type(new_tup)

# Pay close attention -these are parens.
new_tup2 = ()
type(new_tup2)

# If we do not want these tuples anymore, we can remove them
del new_tup
del new_tup2

# Fun with repetition and concatenation
really_funny = ('NA',)*8 + (' batman',)
really_funny

# Check membership
'ha' in really_funny # This is a boolean expression

for word in really_funny:
    print(word)

# Compare tuples
fruit_basket1 = ('apples','pears','blueberries')
fruit1, fruit2, fruit3 = fruit_basket1 #unpack a tuple into single variables
print(fruit1)
print(fruit2)
print(fruit3)
fruit_basket2 = ('apples','oranges','blueberries')
fruit_basket3 = ('apples','pears','blueberries')

# Compare two with known same elements
print("Basket 1 == Basket 3? ", fruit_basket1 == fruit_basket3)

# Compare two with known differing elements
print("Basket 1 == Basket 2? ",fruit_basket1 == fruit_basket2)

# If we wanted to get the 2nd element of sample, what do we use?
sample[___]

# Can we add scalar values to our tuple?
sample = sample + 'more related data'

# What about this way?
sample = sample + ('more related data',) # That ending comma makes a difference
sample

# Let's add more
sample += (12.3, True, 1e08, 'test') # We can use the += shorthand as seen in C# or Java
sample

# Can we change the tuple's elements?
sample[1] = (False,)

# Tuples can be sliced just like lists
# This makes it easier to create new tuples

# Large tuples
large_tuple = (i for i in range(30))
large_tuple
large_tuple = (i for i in range(30),)
large_tuple = tuple([i for i in range(30)])
large_tuple
large_tuple[1::2]
_list = [1,2,3,5,6]
_list.append(9)
_list
large_tuple.append(9)
dir(tuple)
large_tuple.__add__(9)

# Tuple math
ta = (1,2,3)
tb = (4,5,6)
ta + tb

# Sequences and Ranges
[for i in range(0,20)]
[i for i in range(0,20)]
[i+2 for i in range(0,20)]
my_list = []
for i in range(0,20):
  my_list.append(i)
my_list
[i for i in range(0,20)]
[i*2+1 for i in range(0,20)]

# Dictionaries - C# Dictionaries, Java HashMaps
_dict = {}
_dict[ta+tb] = 5
_dict
_dict[_list] = 5
_dict[(1,2,3,4,5,6)]
_dict.keys()
_dict.keys()[0]
_dict.keys()
_dict.keys().iterable()
[ i for i in _dict.keys()][0]

# Named Tuples
# Allows us to use names for indexes with our tuples
from collections import namedtuple
# Parameters - name of class, space delimited elements
Person = namedtuple('Person', 'name fave_thing fave_thing_value')

print('Type of Person:', type(Person))
# Show the help (Intellisense) from PyCharm here!
ilya = Person(name='Ilya', fave_thing="animal", fave_thing_value="donkeylobster")
print('\nRepresentation:', ilya)

sarah = Person(name='Sarah', fave_thing="football team", fave_thing_value="Cleveland Browns")
print('\nGetting a field\'s value:', sarah.fave_thing)

print('\nFields by index:')
for p in [ ilya,sarah ]:
    print('%s has a favorite %s which is %s' % p)
