#! python3
# pythonicCodeExamples.py - examples of writing good pythonic code

import this

# ENUMERATION ====================================
print("\n\nLoops using enumerate()")
animals = ['cat', 'dog', 'moose']
for i, animal in enumerate(animals): # instead of range(len(animals))
    print(i, animal)

# LIST COMPREHENSION =============================
# OLD WAY:
spam = []
for number in range(100):
    if number % 5 != 0:
    spam.append(str(number))
spam
# gives:
'''
['1', '2', '3', '4', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17',
--snip--
'86', '87', '88', '89', '91', '92', '93', '94', '96', '97', '98', '99']
'''
# NEW WAY:
spam = [str(number) for number in range(100) if number % 5 != 0]
spam
# gives:
'''
['1', '2', '3', '4', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17',
--snip--
'86', '87', '88', '89', '91', '92', '93', '94', '96', '97', '98', '99']
'''

# INTERESTING TECHNIQUE FOR GETTING BOOLEANS USING LIST COMPREHENSION
spam = [67,39,20,55,13,45,44]
[i > 42 for i in spam]
# [True, False, False, True, False, True, True] # cool way to get Booleans from a list

# 'WITH OPEN' AS CODE BLOCKS =========================
# use "with" to make code blocks that auto close files you have opened upon completion of code block
# Instead of:
fileObj = open('spam.txt', 'w')
fileObj.write('Hello, world!')
fileObj.close()
# Do it this way:
with open('spam.txt', 'w') as fileObj:
    fileObj.write('Hello World')

# RAW STRINGS =======================================
# use raw 'r' strings to avoid excessive back-slashing (escape characters)
print(r'The file is in C:\Users\Al\Desktop\Info\Archive\Spam')
# instead of
# print('The file is in C:\\Users\\Al\\Desktop\\Info\\Archive\\Spam')

# F STRINGS =========================================
# use f strings for printing variables intermingled with literal strings
name, day, weather = 'Al', 'Sunday', 'sunny'
# both of these work, below - note these are curly braces
f'Hello, {name}. Today is {day} and it is {weather}.'
print(f'Hello, {name}. Today is {day} and it is {weather}.')

# DEFAULTS WITH DICTIONARIES - dictionaryName.get('non-existent-key','default value')
numberOfPets = {'dogs':2}
print('I have',numberOfPets.get('cats',0),'cats.')
# prints 'I have 0 cats', because ',0' specifies default value of 0 for non-matches
# You can also use setdefauilt() to add a key with a default initial value if that key is
# not found
numberOfPets={'dogs',2}
numberOfPets.setdefault('cats',0) # does nothing if 'cats' exists but add 'cats' key with value of 0 if it doesn't

# COLLECTIONS ====================================
#  Another way to do this is with the collections module.  It automates the setting of default
# keys and values so you don't need to set defaults on the fly.  You start by passing it a
# default data type.
# Like this:
import collections
scores = collections.defaultdict(int)
scores
# gives: defaultdict(<class 'int'>, {})
scores['Al'] += 1
scores
# gives: defaultdict(<class 'int'>, {'Al': 1})
scores['Zophie'] # No need to set a value
# gives: 0
scores
# gives: defaultdict(<class 'int'>, {'Al': 1, 'Zophie': 0})
# you can also make the data type 'list' with the collections module, like this:
booksReadBy = collections.defaultdict(list)
booksReadBy['Al'].append('Oryx and Crake')
booksReadBy['Al'].append('American Gods')
len(booksReadBy['Al'])
# gives: 2
booksReadBy
# gives: defaultdict(<class 'list'>, {'Al': ['Oryx and Crake', 'American Gods']})
booksReadBy['Kimberly']
[] # default is an empty lis
booksReadBy
# gives: defaultdict(<class 'list'>, {'Al': ['Oryx and Crake', 'American Gods'], 'Kimberly': []})

# USE DICTIONARIES INSTEAD OF A SWITCH STATEMENT ======================
# OLD WAY
season="Summer"
if season == 'Winter':
    holiday = 'New Year\'s Day'
elif season == 'Spring':
    holiday = 'May Day'
elif season == 'Summer':
    holiday = 'July 4th'
elif season == 'Fall':
    holiday = 'Halloween'
else:
    holiday = 'Personal day off'
# ALTERNATIVE WAY:
season="Summer"
holiday = {'Winter': 'New Year\'s Day','Spring': 'May Day','Summer': 'July 4th',\
           'Fall': 'Halloween'}.get(season, 'Personal day off')
'''
The code above is a single assignment statement. The value stored in holiday
is the return value of the get() method call, which returns the value for the key
that season is set to. If the season key doesn’t exist, get() returns 'Personal day
off' because it is set as the default value
'''

# USE OF * AND ** WHEN PASSING ARGUMENTS TO FUNCTIONS (*args and **kwargs)========
'''
*ARGS - YOU CAN USE THE '*' TO INTERPRET ITEMS IN A LIST (OR ANY OTHER ITERABLE DATA TYPE)
as individual positional arguments in function calls.
* can also be used in function definitions.  More on that later.
'''
args = ['cat', 'dog', 'moose']
print(*args)
# gives: cat dog moose
# Note that print(args) gives ['cat','dog','mouse']
'''
The * syntax allows you pass the list items to a function individually, no
matter how many items are in the list.

*KWARGS - YOU CAN USE  '**'  TO PASS MAPPING DATA TYPES (SUCH AS DICTIONARIES)
as individual keyword arguments to functions. Keyword arguments are preceded by a
parameter name and equal sign. For example, the print() function has a sep
keyword argument that specifies a string to put in between the arguments it
displays. It’s set to a single space string ' ' by default. You can assign a keyword
argument to a different value using either an assignment statement or the '**'
syntax.
'''
print('cat', 'dog', 'moose', sep='-')
# gives: cat-dog-moose
kwargsForPrint = {'sep': '-'}
print('cat', 'dog', 'moose', **kwargsForPrint)
# gives: cat-dog-moose

# *ARGS - '*' CAN ALSO BE USED IN FUNCTION DEFS TO SPECIFY VARYING NUMBER OF POSITIONAL ARGS.
def product(*args):
    result = 1
    for num in args:
    result *= num
    return result
product(3, 3)
# gives 9
product(2, 1, 2, 3)
# gives 12

# **KWARGS - JUST LIKE '*', '**" CAN ALSO BE USED IN FUNCTION DEFINITIONS.
# The '**' syntax represents a varying number of optional keyword arguments.
def formMolecules(**kwargs):
    if len(kwargs) == 2 and kwargs['hydrogen'] == 2 and kwargs['oxygen'] == 1:
    return 'water'
    # (rest of code for the function goes here)
formMolecules(hydrogen=2, oxygen=1)
# gives: 'water'
'''
USING * AND ** TO CREATE WRAPPER FUNCTIONS
which can pass arguments to another function and return that function’s return value.
For example, we can create a printLowercase() function that wraps the built-in
print() function. It relies on print() to do the real work but converts the string
arguments to lowercase first:
'''
def printLower(*args, **kwargs):
    args = list(args) # make a list out of the args tuple
    for i, value in enumerate(args):
        args[i] = str(value).lower() # convert to lower case
        return print(*args, **kwargs)

name = 'Albert'
printLower('Hello,', name)
# gives: hello, albert
printLower('DOG', 'CAT', 'MOOSE', sep=', ')
# gives: dog, cat, moose # separated by commas
'''
The printLower() function uses the * syntax to accept a varying
number of positional arguments in a tuple assigned to the args parameter,
whereas the ** syntax assigns any keyword arguments to a dictionary in the
kwargs parameter.
'''
# GLOBAL VARIABLES =======================================
TOTAL = 0
def addToTotal(amount):
    global TOTAL #<===GLOBAL VARIABLE INSIDE A FUNCTION
    TOTAL += amount
    return TOTAL


addToTotal(10)
# gives 10
addToTotal(10)
# gives 20
addToTotal(9999)
# gives 10019
TOTAL
# gives 10019

# DOCSTRINGS
'''
You can retrieve the docstring for a module, class, function, or
method by checking the respective object’s __doc__ attribute. For example,
here we examine the docstrings to find out more about the sessions module,
the Session class, and the get() method:
'''
from requests import sessions
sessions.__doc__
# gives: '\nrequests.session\n~~~~~~~~~~~~~~~~\n\nThis module provides a Session object
# to manage and persist settings across\nrequests (cookies, auth, proxies).\n'






