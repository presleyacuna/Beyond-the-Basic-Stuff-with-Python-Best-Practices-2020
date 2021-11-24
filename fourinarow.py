#! python3
'''Four-in-a-Row, by AL swiegart al@inventwithpython.com
A tile-dropping game to get four-in-a-row, similar to Connect Four.'''

import sys

# Constants used for displaying the board:
EMPTY_SPACE = "." # a period is easier to count than a space.
PLAYER_X = "X"
PLAYER_O = "O"

# Note: Update BOARD_TEMPLATE & COLUMN_LABELS if BOARD_WIDTH is changed.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# The template string for displaying the board:
BOARD_TEMPLATE = """
 1234567
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
+-------+"""

def main():
    """Runs a single game of Four-in-a-Row."""
    print(
        """Four-in-a-Row, by Al Sweigart al@inventwithpython.com

        Two players take turns dropping tiles into one of seven columns, trying
        to make Four-in-a-Row horizontally, vertically or diagonally.
        """
        )

    # Set up a new game:
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    while True: # Run a player's turn.
        # Display the board and get player's move:
        displayBoard(gameBoard)
        playerMove = getPlayerMove(playerTurn, gameBoard) # playerMove is the tuple of the
        # position on the board that the tiled was placed into.
        gameBoard[playerMove] = playerTurn # assign an 'X' or 'O' to the tuple on the board
        # that was selected in getPlayeMove()

        # Check for a win or a tie:
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard) # Display the board one last time.
            print("Player {} has won!".format(playerTurn))
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard) # Display the board one last time.
            print("There is a tie!")
            sys.exit()

        # Switch turns to other player:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X

def getNewBoard():
    """Returns a dictionary that represents a Four-in-a-Row board.

    The keys are (columnIndex, rowIndex) tuples of two integers, and the
    values are one of the "X", "O" or "." (empty space) strings."""

    board = {}
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            board[(columnIndex,rowIndex)] = EMPTY_SPACE
            ''' Square brackets are used in dictionaries for referencing keys and
            in this case the key is a tuple '''
    return board

def displayBoard(board):
    """Display the board and its tiles on the screen."""

    # Prepare a list to pass to the format() string method for the board
    # template.  The list holds all the board's tiles (and empty
    # spaces) going left to right, top to bottom:
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex,rowIndex)])
            ''' You use square brackets to reference keys in a dictionary,
            and in this case the key is a 2 integer tuple, thus the format
            dictionary_name[(tuple)] '''
    # Display the board:
    print(BOARD_TEMPLATE.format(*tileChars))
    ''' the string.format() method works by putting in one or more replacement fields into
    placeholders which are defined by a pair of curly braces {}. So, in this
    case we are replacing the curly braces in BOARD_TEMPLATE with the values in the list
    tilechars[], which are the current state of the board.'''

def getPlayerMove(playerTile, board):
    '''Let a player select a coluumn on the board to drop a tile into.
        Returns a tuple of the (column, row) that the tile falls into.'''
    while True: # Keep asking player until the they enter a valid move.
        print(f"Player {playerTile}, enter 1 to {BOARD_WIDTH} or QUIT:")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in COLUMN_LABELS:
            print(f"Enter a number from 1 to {BOARD_WIDTH}.")
            continue # Ask player again for their move.

        columnIndex = int(response) - 1 # -1 for 0-based column indexes

        # if the column is full, ask for a move again.
        if board[(columnIndex,0)] != EMPTY_SPACE:
            print("That column is full, select another one.")
            continue # Ask player again for their move.

        # Starting from the bottom, find the first empty space.
        for rowIndex in range(BOARD_HEIGHT - 1, 1, -1): # start, stop, step or 5,1,-2
            # remember, arrays start counting at 0 thus, BOARD_HEIGHT -1
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return(columnIndex, rowIndex)

def isFull(board):
    '''Returns True if the 'board' has no empty spaces, otherwise
        returns False.'''
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False # Found an empty space, so return False.
    return True # All spaces are full.

def isWinner(playerTile, board):
    '''Returns True if 'playerTile' has four tiles in a row on 'board'.
    otherwise returns False.'''
    # Go through the entire board, checking for four-in-a-row:

    # check for horizontal four-in-a-row
    for columnIndex in range(BOARD_WIDTH - 3): # because you need to spot 4 in a row
        # and you need to check across four columns (+1, +2, +3), so iterate from 1 to 3
        for rowIndex in range(BOARD_HEIGHT):
            # Check for four-in-a-row going across to the right:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    # check for vertical four-in-a-row
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Check for four-in-a-row going down:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    # check for diagonal four-in-a-row
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Check for four-in-a-row going right-down diagonal:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

            # Check for four-in-a-row going left-down diagonal:
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False

# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    main()
