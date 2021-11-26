#! python3
''' Python supports multiple parent classes by offering a feature called multiple inheritance.
For example, we can have an Airplane class with a flyInTheAir() method and a Ship class with a
floatOnWater() method. We could then create a FlyingBoat class that inherits from both
Airplane and Ship by listing both in the class statement, separated by commas.'''

class Airplane:
    def flyInTheAir(self):
        print('Flying...')

class Ship:
    def floatOnWater(self):
        print('Floating...')

class FlyingBoat(Airplane, Ship):
    pass

#from multipleInheritanceExample import *
seaDuck = FlyingBoat()
seaDuck.flyInTheAir()
seaDuck.floatOnWater()