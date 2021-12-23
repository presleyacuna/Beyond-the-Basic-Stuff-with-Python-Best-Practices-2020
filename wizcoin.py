#! /usr/bin/python3

import collections.abc
import operator

class WizCoinException(Exception):
    '''The wizcoin module raises this when a module is misused.'''
    pass

class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new WizCoin object with galleons, sickles and knuts."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # NOTE: __init__() methods NEVER have a return statement

    def total(self): # so, if purse=Wizcoin(2,5,9), you can use purse.total()
        """The value (in knuts) of all the coins in thie WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    # demonstrate how the total2 method could be rendered as an RO property
    # (no getter or setter methods - see wizcoinexample.py)
    @property
    def total2(self):
        """The value (in knuts) of all the coins in thie WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

    @property
    def galleons(self):
        '''Returns the number of galleon coins in this object.'''
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            # demonstrate how setter method can be used for error/type checking
            raise WizCoinException('galleons attr must be set to an int, not ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('galleons must be a positive int, not a negative' + value.__class__.__qualname__)
        self._galleons = value # modify the original object with the new value

    @property
    def sickles(self):
        '''Returns the number of sickles coins in this object.'''
        return self._sickles

    @sickles.setter
    def sickles(self, value):
        if not isinstance(value, int):
            raise WizCoinException('sickles attr must be set to an int, not ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('sickles must be a positive int, not a negative' + value.__class__.__qualname__)
        self._sickles = value

    @property
    def knuts(self):
        '''Returns the number of knuts coins in this object.'''
        return self._knuts

    @knuts.setter
    def knuts(self, value):
        if not isinstance(value, int):
            raise WizCoinException('knuts attr must be set to an int, not ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('knuts must be a positive int, not a negative' + value.__class__.__qualname__)
        self._knuts = value

    # Dunder methods - (double underscore methods)
    # We overload these bujilt-in methods so they recognize WizCoin objects
    def __repr__(self): # handles things like repr(purse)
        """Returns a string of an expression that re-creates this object."""
        return f'{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})'

    def __str__(self): # handles things like str(purse)
        """Returns a human-readable string representation of this object."""
        return f'{self.galleons}g, {self.sickles}s, {self.knuts}k'

    def __add__(self,other):
        """Adds the coin amounts in two WizCoin objects together."""
        if not isinstance(other,WizCoin): #The isinstance() function returns True if the specified object is of the
            # specified type, otherwise False.
                return NotImplemented
        return WizCoin(other.galleons + self.galleons, other.sickles + self.sickles, other.knuts + self.knuts)

    def __sub__(self,other):
        """Subtracts the coin amounts in two WizCoin objects together."""
        if not isinstance(other,WizCoin): #The isinstance() function returns True if the specified object is of the
            # specified type, otherwise False.
                return NotImplemented
        return WizCoin(self.galleons - other.galleons, self.sickles - other.sickles, self.knuts - other.knuts)

    def __mul__(self, other):
        """Multiplies the coin amounts by a non-negative integer."""
        if not isinstance(other, int): #The isinstance() function returns True if the specified object is of the
            # specified type, otherwise False.
            return NotImplemented
        if other < 0:
        # Multiplying by a negative int results in negative
        #  amounts of coins, which is invalid.
            raise WizCoinException('cannot multiply with negative integers')
        return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

    # for Reflected Dunder methods -> when wizcoin object is on right side of the operator
    # (example: 10 * purse). Since multiplication is cummutative (works the same
    # whether expression is reversed or not; 2*3 is the same as 3*2), return the
    # result of a normal __mul__ override as the result.
    def __rmul__(self,other):
        """Multiplies the coin amounts by a non-negative integer when wizcoin object on right side of operator."""
        return self.__mul__(other)
    """Keep in mind that in the expression 10 * purse, Python first calls the
int class’s __mul__() method to see whether integers can be multiplied with
WizCoin objects. Of course, Python’s built-in int class doesn’t know anything
about the classes we create, so it returns NotImplemented. This signals to Python
to next call WizCoin class’s __rmul__(), and if it exists, to handle this operation.
If the calls to the int class’s __mul__() and WizCoin class’s __rmul__() both
return NotImplemented, Python raises a TypeError exception."""

    def __iadd__(self,other):
        """Add the amounts in another Wizcoin object to this object."""
        if not isinstance(other,WizCoin): #The isinstance() function returns True if the
            # specified object is of the specified type, otherwise False.
            return NotImplemented

        # We modify the 'self' object in place:
        self.galleons += other.galleons
        self.sickles += other.sickles
        self.knuts += other.knuts
        return self # In place dunder methods almost awyas return self.


    def __imul__(self, other):
        """Multiply the amount of galleons, sickles, and knuts in this object
        by a non-negative integer amount."""
        if not isinstance(other,int): #The isinstance() function returns True
            # if the specified object is of the specified type, otherwise False.
            return NotImplemented
        if other < 0:
            raise WizCoinException('cannot multiply with negative integers')

        # The Wizcoin class creates mutable objects, so do NOT create a
        # new object like this commented-out code:
        #return Wizcoin(self.galleons * other, self.sickles * other, self.knuts * other)

        # We modify the 'self' object in place:
        self.galleons *= other
        self.sickles *= other
        self.knuts *= other
        return self # In-place dunder methods almost always return self.

    # Study of overloading comparison operators ('>', '<', '>=', etc...) to
    # handle wizcoin objects.  To accomplish this, we
    # import the operator module which has functions that perform these comparison
    # operations (operator.eq, operator.ne, etc...)
    def comparisonOperatorHelper(self, operatorFunc, other): # operatorFunc is a
        # function that is passed as an argument to this method
        """A helper method for our comparison dunder methods."""

        if isinstance(other, WizCoin):
            return operatorFunc(self.total(), other.total())
        elif isinstance(other, (int, float)):
            return operatorFunc(self.total(), other)
        elif isinstance(other,collections.abc.Sequence):
            otherValue = (other[0] * 17 *29) + (other[1] * 29) + other[2]
            return operatorFunc(self.total(), otherValue)
        elif operatorFunc == operator.eq:
            return False
        elif operatorFunc == operator.ne:
            return True
        else:
            return NotImplemented

    # overload the standard operator functions with wizcoin specific code
    def __eq__(self,other): # eq is "Equal"
        return self.comparisonOperatorHelper(operator.eq,other) # the operator.eq
        # function is passed into comparisonOperatorHelper() as operatorFunc
    def __ne__(self, other): # ne is "Not Equal"
        return self.comparisonOperatorHelper(operator.ne,other)
    def __lt__(self, other): # lt is "Less Than"
        return self.comparisonOperatorHelper(operator.lt,other)
    def __le__(self, other): # le is "Less Than or Equal"
        return self.comparisonOperatorHelper(operator.le,other)
    def __gt__(self, other): # gt is "Greater Than"
        return self.comparisonOperatorHelper(operator.gt,other)
    def __ge__(self, other): # ge is "Greater than or Equal"
        return self.comparisonOperatorHelper(operator.ge,other)


