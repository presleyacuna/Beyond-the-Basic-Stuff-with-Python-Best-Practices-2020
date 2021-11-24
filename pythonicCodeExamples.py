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
'''
OLD WAY:
print('Hello, %s. Today is %s and it is %s.' % (name, day, weather))
'''
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

# USE OF * AND ** WHEN PASSING ARGUMENTS TO FUNCTIONS (*args and **kwargs)============
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
printLower('Hello,', name) # name is an arg too.
# gives: hello, albert

# In this version, name would have been a kwarg:
printLower{'Hello', name='Albert'}
# gives: TypeError: 'name' is an invalid keyword argument for print() because the
# kwarg is passed literally without conversion to strings or encased in quotes

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

# DOCSTRINGS ==========================================================
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

# DIR - to get list of all methods in a module or a clasa
from requests import sessions
dir(sessions)

# USING DOCSTRINGS to get structured help file - help(modulename)
'''
You can put docstrings throughout your program (after each function def line, for example)
and then get a structured help file by importing your module name into your python console,
and typing help(modulename).

example: you have some code named towerofhanoi.py

import towerofhanoi
help(towerofhanoi)
gives:
Help on module towerofhanoi:

NAME
    towerofhanoi

DESCRIPTION
    THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com
    A stack moving game.

FUNCTIONS
    displayDisk(width)
        Display a disk of the given width.  A width of 0 means no disk.

    displayTowers(towers)
        Display the threww towers with their disks.

    getPlayerMove(towers)
        Asks the player for a move.  Returns (fromTower, toTower).

    main()
        Runs a single game of The Tower of Hanoi.

DATA
    SOLVED_TOWER = [5, 4, 3, 2, 1]
    TOTAL_DISKS = 5

FILE
    c:\users\presley\pycharmprojects\beyond the basic stuff with python best practices 2020\towerofhanoi.py
'''

# CLASSES ================================================================

# Methods are functions associated with objects of a particular class
# Methods come after the object: the correct code is 'Hello'.lower(), not lower('Hello').

'''
We create objects by calling the class name as a function.
This function is referred to as a constructor function (or
constructor because it constructs a new object.
We also say the constructor instantiates a new instance of the class.

The __init__() method is where you commonly set the initial values of attributes

Example:
class Wizcoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def value(self):
        """The value (in knuts) of all the coins in thie WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

Notice how this is different from a function, which might look like this:
    def Wizcoin(galleons, sickles, knuts):

Python creates a new WizCoin object and then passes three arguments
to an __init__() call. But the __init__() method has four parameters: self,
galleons, sickles, and knuts. The reason is that all methods have a first
parameter named self. When a method is called on an object, the object is
automatically passed in for the self parameter. The rest of the arguments
are assigned to parameters normally.

When you’re reading code, the presence of self as the first parameter is the
quickest way you can distinguish methods from functions.

Example:
import wizcoin # a module we created, wizcoin.py, which contains the class WizCoin()
purse = wizcoin.Wizcoin(2,5,99)

In this example where we create an new object, purse, from the WizCoin class.
Note that the 2, 5, and 99 arguments passed to WizCoin aren’t automatically
assigned to the new object’s attributes; we need the three assignment statements
in __init__() to do this.

The presence of self in self.galleons indicates
that it’s an attribute of the object, whereas galleons is a parameter. This storing
of the constructor’s arguments in the object’s attributes is a common
task for a class’s __init__() method.

Attributes - any name following a dot.  this includes attributes that are passed
as arguments to a class, as well as the methods of the class.

Example:
coinJar = wizcoin.WizCoin(13,0,0)
print(coinJar)
print('G:', coinJar.galleons, 'S:', coinJar.sickles, 'K:', coinJar.knuts)
print('Total value:', coinJar.value())
print('Weight:', coinJar.weightInGrams(), 'grams')

WHEN TO USE A CLASS:
When several functions in the code all operate on the same data structure,
it’s usually best to group them together as the methods and attributes
of a class.

CLASS INHERITANCE
Example:
class ParentClass:
    def printHello(self):
        print('Hello, world!')

class ChildClass(ParentClass):
    def someNewMethod(self):
        print('ParentClass objects don\'t have this method.')

class GrandchildClass(ChildClass):
    def anotherNewMethod(self):
        print('Only GrandchildClass objects have this method.')

The child and grandchild classes inherit all the methods from the parental
class but also have methods of their own which are unknown to the parental classes.
ParentClass() does not know about anotherNewMethod() but GrandchildClass() does know
about printHello().

CLASSES CAN ALSO OVERRIDE METHODS FROM THE PARENT.
Example:
class MiniBoard(TTTBoard):  # overrides getBoardStr() method from parent class TTTBoard().
    def getBoardStr(self):
        """Return a tniy text-representation of the board."""
        # Change blank spaces to a '.'
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                self._spaces[space] = '.'

        boardStr = f"""
            {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
            {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
            {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9"""

TTT Board() has a different text representation of the TicTacToe board - bigger.

USE OF super() FUNCTION
super() function can be used inside a overriding sub-class to execute the parent class'
method instead of having to retype it, if most of the code is going to be the same.
For example, if your overriding sub-class is going to just append code to the parent
method, use super().parentmethod() where parentmethod is the name of the
parent class' method, then append the new code after this line.

'''
