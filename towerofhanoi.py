"""THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com
A stack moving game."""

import copy
import sys

TOTAL_DISKS = 5 # More disks means a more difficult puzle

# Start with all the disks in tower A:
SOLVED_TOWER = list(range(TOTAL_DISKS,0, -1)) # range(start, stop, step)

def main():
    '''Runs a single game of The Tower of Hanoi.'''
    print(
        '''THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com

        Move the tower of disks, one disk at a time, to another tower.
        Larger disks cannot rest on top of a smaller disk.

        More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
        '''
    )
    """The towers dictionary has keys "A", "B", and "C" and values
that are lists representing a tower of disks. The list contains
integers representing disks of different sizes, and the start of
the list is the bottom of the tower. For a game with 5 disks,
the list [5, 4, 3, 2, 1] represents a completed tower. The blank
list [] represents a tower of no disks. The list [1, 3] has a
larger disk on top of a smaller disk and is an invalid
configuration. The list [3, 1] is allowed since smaller disks
can go on top of larger ones."""
    towers = {"A":copy.copy(SOLVED_TOWER), "B":[], "C":[]}

    while True: # Run a single turn on each iteration of this loop.
        # Display the towers and disks:
        displayTowers(towers)

        # Ask the user for a move:
        fromTower, toTower = getPlayerMove(towers)

        # Move the top disk from fromTower to toTOwer:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # Check if the user has solved the puzzle
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers) # Display the towers on last time
            print("You have solved the upzzle! Well done!")
            sys.exit()

def getPlayerMove(towers):
    '''Asks the player for a move.  Returns (fromTower, toTower).'''

    while True: # Keep asking player until the enter a valid move
        print('Enter the letter of "from" and "to" towers, or QUIT.')
        print("(e.g., AB to move a disk from tower A to tower B.)")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        # Make sure the user entered valid towqer letters:
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter one of AB, AC, BA, BC, CA or CB.")
            continue # As player again for their move

        # Use more descriptive variable names:
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # The "from" Tower cannot be an empty tower:
            print("You selected a tower with no disks.")
            continue # Ask player again for their move
        elif len(towers[toTower]) == 0:
            # Any disk can be moved into an empty "to" tower:
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("Can't put larger disks on top of smaller ones.")
            continue # Ask player sgain for their move:
        else:
            # This is a valid move, so return the selected towers:
            '''
            In Python, return statements always return a single value. Although this
return statement looks like it returns two values, Python actually returns a
single tuple of two values, which is equivalent to return (fromTower, toTower).
            '''
            return fromTower, toTower

def displayTowers(towers):
    '''Display the three towers with their disks.'''

    # Display the three towers:
    for level in range(TOTAL_DISKS, -1, -1): # range(start, stop, step)
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0) # Display the bare pole with no disk.
            else:
                displayDisk(tower[level]) # Display the disk
        print()

    # Display the tower labels A, B and C:
    emptySpace = " " * (TOTAL_DISKS)
    '''
    In the line of code below, the format() string method puts whatever is in between
    the parens into the curly brace placeholders of the print statement.  The '0' inside
    each curly brace is a positional number placeholder.  So if format() had more than
    one value inside its parens, that number wuld tell you which value to drop in.

    example:
    print('{1} and {0}'.format('spam', 'eggs'))
    eggs and spam

    '''
    print("{0} A{0}{0} B{0}{0} C\n".format(emptySpace))
    '''
    This is what prints when you run the game:

     ||          ||          ||
    @_1@         ||          ||
   @@_2@@        ||          ||
  @@@_3@@@       ||          ||
 @@@@_4@@@@      ||          ||
@@@@@_5@@@@@     ||          ||
      A           B           C

    The emptySpace variable is set to the number of spaces to place in between
    each label, which is based on TOTAL_DISKS Rather than use an f-string, as in
    print(f'{emptySpace} A{emptySpace}{emptySpace} B{emptySpace}{emptySpace} C\n').
    We use the format() string method instead. This allows us to use the same emptySpace
    argument wherever {0} appears in the associated string, producing shorter
    and more readable code than the f-string version.
'''


def displayDisk(width):
    '''Display a disk of the given width.  A width of 0 means no disk.'''
    emptySpace = " " * (TOTAL_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk:
        print(f"{emptySpace}||{emptySpace}", end="") # no carriage return
    else:
        # Display the disk:
        disk = "@" * width
        numLabel = str(width).rjust(2, "_") # example: if width = 1, this gives '_1'
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")

# if this program was run (instead of imported), run the game:
if __name__ == "__main__":
    '''
    Python automatically sets the __name__ variable to '__main__' if a player
    runs the towerofhanoi.py program directly. But if someone imports the program
    as a module using import towerofhanoi, then __name__ would be set to
    'towerofhanoi'. The if __name__ == '__main__': line will call the main() function
    if someone runs our program, starting a game of Tower of Hanoi. But
    if we simply want to import the program as a module so we could, say, call
    the individual functions in it for unit testing, this condition will be False
    and main() won’t be called
    '''
    main()






