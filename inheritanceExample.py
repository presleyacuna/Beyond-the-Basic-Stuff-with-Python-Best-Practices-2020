#! python3

class ParentClass:
    def printHello(self):
        print('Hello, world!')

class ChildClass(ParentClass):
    def someNewMethod(self):
        print('ParentClass objects don\'t have this method.')

class GrandchildClass(ChildClass):
    def anotherNewMethod(self):
        print('Only GrandchildClass objects have this method.')

print('Create a ParentClass object and call its methods:')
parent = ParentClass()
parent.printHello()

print('Create a ChildClass object and call its methods:')
child = ChildClass()
child.printHello()
child.someNewMethod()

print('Create a GrandchildClass object and call its methods:')
grandchild = GrandchildClass()
grandchild.printHello()
grandchild.someNewMethod()
grandchild.anotherNewMethod()

print('An error:')
parent.someNewMethod()
