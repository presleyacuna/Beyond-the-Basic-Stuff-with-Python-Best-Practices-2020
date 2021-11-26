#! python3
'''A class attribute is a variable that belongs to the class rather than to an object.
We create class attributes inside the class but outside all methods,
just like we create global variables in a .py  file but outside all functions.
Here’s an example of a class attribute named count,
which keeps track of how many CreateCounter objects have been created:'''

class CreateCounter:
    count = 0  # This is a class attribute.

    def __init__(self):
        CreateCounter.count += 1

print('Objects created:', CreateCounter.count)  # Prints 0.
a = CreateCounter()
b = CreateCounter()
c = CreateCounter()
print('Objects created:', CreateCounter.count)  # Prints 3.