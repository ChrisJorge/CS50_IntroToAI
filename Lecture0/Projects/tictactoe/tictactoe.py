"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
 

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    NumberOfEmptySpots = 0 # Initialize Variable for the number of empty spots on the board
    for row in range(len(board)): # iterate through all of the rows
        for column in range(len(board[0])): # iterate through the columns
            if board[row][column] == None: # Check if the spot on the board is empty
                NumberOfEmptySpots += 1 # Increase the number of empty spots by one
    
    if NumberOfEmptySpots % 2 == 0: # Check if the number of empty spots is even
        return O # If it is even, return O
    else:
        return X # If the number of empty spots is odd, return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    PossibleActions = set() # Initialize an empty set of all possible actions
    for row in range(len(board)): # iterate through all of the rows
        for column in range(len(board[0])): # iterate through the columns
            if board[row][column] == None: # Check if a spot on the board is empty
                PossibleActions.add((row,column)) # Add that row, column combination into the possible actions set
    return PossibleActions # Return all of the possible actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == board[0][1] == board[0][2]): # Check first row
        return board[0][0]
    elif(board[1][0] == board[1][1] == board[1][2]): # Check second row
        return board[1][0]
    elif(board[2][0] == board[2][1] == board[2][2]): # Check third row
        return board[2][0]
    elif(board[0][0] == board[1][0] == board[2][0]): # Check first column
        return board[0][0]
    elif(board[0][1] == board[1][1] == board[2][1]): # Check second column
        return board[0][1]
    elif(board[0][2] == board[1][2] == board[2][2]): # Check third column
        return board[0][2]
    elif(board[0][0] == board[1][1] == board [2][2]): # Check first diagonal (top left to bottom right)
        return board [0][0]
    elif(board[0][2] == board[1][1] == board[3][0]): # Check second diagonal (top right to bottom left)
        return board[0][0]
    else:
        return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    won = winner(board) # Check if a winner has been declared
    if won: # Check if a value other than False has been given
        return True
    else:
        return False
   


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    match (won):
        case 'X':
            return 1
        case 'O':
            return -1
        case _:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
