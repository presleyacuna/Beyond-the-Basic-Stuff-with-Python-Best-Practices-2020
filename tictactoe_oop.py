#! python3
# tictactoe_oop.py, an object-oriented tic-tac-toe game.

import copy

ALL_SPACES = list('123456789') # The keys to a TTT board dictionary
X, O, BLANK = 'X', 'O', ' ' # Constants for string values

def main():
    """Runs a game of tci-tac-toe."""
    print('Welcome to tic-tac-toe!')

    if input('Use mini board? Y/N: ').lower().startswith('y'):
        gameBoard = MiniBoard() # Create a MiniBoard object
    elif input('Use hint board? Y/N: ').lower().startswith('y'):
        gameBoard = HintBoard() # Create a Hintboard object.
    else:
        gameBoard = TTTBoard() # Create a TTTboard object.

    currentPlayer, nextPlayer = X, O #  X goes first, O goes next.

    while True:
        print(gameBoard.getBoardStr()) # Display the board on the screen.

        # Keep asking the player until they enter a number 1-9:
        move = ' '
        while not gameBoard.isValidSpace(move):
            print(f'What is {currentPlayer}\'s move? (1-9)')
            move = input()
        gameBoard.updateBoard(move, currentPlayer) # Make the move.

        # Check if game is over:
        if gameBoard.isWinner(currentPlayer): # Check first for victory.
           print(gameBoard.getBoardStr())
           print(currentPlayer + ' has won the game!')
           break
        elif gameBoard.isBoardFull(): # Next check for a tie.
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer # Swap turns.
    print('Thanks for playing!')

class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """Create a new, blank tic-tac-toe board."""
        self._spaces = {} # The board is represented as a Python dictionary.
        for space in ALL_SPACES:
            self._spaces[space] = BLANK # All spaces start as blank.

    def getBoardStr(self):
        """Return a text-representation of the board."""
        return f"""
            {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
             -+-+-
            {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
            -+-+-
            {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9"""

    def isValidSpace(self, space):
        """Returns true if the space on the board is a valid space number
        and the space is blank."""
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def isWinner(self, player):
        """Return True if player is a winner on this TTTBoard."""
        s, p = self._spaces, player # Shorter names as "syntactic sugar".
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
        return ((s['1'] == s['2'] == s['3'] == p) or # Across the top
                (s['4'] == s['5'] == s['6'] == p) or # Across the middle
                (s['7'] == s['8'] == s['9'] == p) or # Across the bottom
                (s['1'] == s['4'] == s['7'] == p) or # Down the left
                (s['2'] == s['5'] == s['8'] == p) or # Down the middle
                (s['3'] == s['6'] == s['9'] == p) or # Down the right
                (s['3'] == s['5'] == s['7'] == p) or # Diagonal
                (s['1'] == s['5'] == s['9'] == p))    # Diagonal

    def isBoardFull(self):
        """Return True if every space on the board has been taken."""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False # If a single space is blank return False.
        return True # No spaces are blank, so return True.

    def updateBoard(self, space, player):
        """Sets the space on the voard to player."""
        self._spaces[space] = player

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

        # Change '.' back to blank spaces
        for space in ALL_SPACES:
            if self._spaces[space] == '.':
                self._spaces[space] = BLANK
        return boardStr

class HintBoard(TTTBoard): # example of using super() function
    def getBoardStr(self):
        """Return a text-representation of the board with hints."""
        boardStr = super().getBoardStr() # Call getBoardStr() from TTTBoard() class

        xCanWin = False
        oCanWin = False
        originalSpaces = self._spaces # Backup _spaces.
        for space in ALL_SPACES: # Check each space:
            # Simulate X moving onto this spaces:
            self._spaces = copy.copy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.isWinner(X):
                xCanWin = True
            # Simulate O moving onto this space:
            self._spaces = copy.copy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.isWinner(O):
                oCanWin = True
        if xCanWin:
            boardStr += '\nX can win in one more move.'
        if oCanWin:
            boardStr += '\nO can win in one more move.'
        self._spaces = originalSpaces
        return boardStr

if __name__ == '__main__':
    main() # call main() if this module is run, but not when imported.


