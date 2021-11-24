#! python3
# a demonstration of class methods

class AsciiArt:
    def __init__(self, characters):
        self._characters = characters
        print("init print\n", self._characters)

    @classmethod
    def fromFile(cls, filename):
        with open(filename) as fileObj:
            characters = fileObj.read()
            print("fromFile print\n", characters)
            return cls(characters)

    def fromFile2(self, filename):
        with open(filename) as fileObj:
            characters = fileObj.read()
            print("fromFile2 print\n", self._characters)
            return (characters)

    def display(self):
        print("display print\n", self._characters)

    # Other AsciiArt methods wold go here....

face1 = AsciiArt(' _______\n' +
'|  . .  |\n' +
'| \\___/ |\n' +
'|_______|')

face1.display()

face2 = AsciiArt.fromFile('face.txt')
face2.display()

face3 = AsciiArt.fromFile2('face.txt')
face3.display()
