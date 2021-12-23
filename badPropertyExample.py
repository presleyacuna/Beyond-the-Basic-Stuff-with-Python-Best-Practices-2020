#! python3

class ClassWithBadProperty:
    def __init__(self):
        self.someAttribute = 'some initial value'

    @property
    def someAttribute(self): # This is the 'getter' method.
        # We forgot to _ underscore in 'self._someAttribute here' causing
        # us to use the property and call the getter method again:
        return self.someAttribute # This call the getter again!
    ''' Should be:
    @property
    def someAttribute(self): # This is the 'getter' method.
        return self._someAttribute
        '''

    @someAttribute.setter
    def someAttribute(self,value): # This is the 'setter' method.
        self._someAttribute = value

obj = ClassWithBadProperty()
print(obj.someAttribute) # Error because getter call the getter