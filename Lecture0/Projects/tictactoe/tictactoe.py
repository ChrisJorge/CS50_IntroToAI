"""
Tic Tac Toe Player
"""

import math
import copy

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
    if action not in actions(board): # Check if the action is one of the possible actions
        raise Exception('Move is not valid') # Raise an exception if the action is not valid
    NewBoard = copy.deepcopy(board) # Create a deep copy of the board so that the original board (The one seen on screen) is not modified
    row,column = action # Get the row and column to place
    NewBoard[row][column] = player(board) # Add the corresponding players character (X or O) into the spot on the board
    return NewBoard # Return the modified board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if ((board[0][0] == board[0][1] == board[0][2]) and (board[0][0] is not None and board[0][1] is not None and board[0][2] is not None)): # Check first row
        print('row 1 returning true')
        return board[0][0]
    elif(board[1][0] == board[1][1] == board[1][2] and (board[1][0] is not None and board[1][1] is not None and board[1][2] is not None)): # Check second row
        print('row 2 returning true')
        return board[1][0]
    elif(board[2][0] == board[2][1] == board[2][2] and (board[2][0] is not None and board[2][1] is not None and board[2][2] is not None)): # Check third row
        print('row 3 returning true')
        return board[2][0]
    elif(board[0][0] == board[1][0] == board[2][0] and (board[0][0] is not None and board[1][0] is not None and board[2][0] is not None)): # Check first column
        print('column 1 returning true')
        return board[0][0]
    elif(board[0][1] == board[1][1] == board[2][1]and (board[0][1] is not None and board[1][1] is not None and board[2][1] is not None)): # Check second column
        print('column 2 returning true')
        return board[0][1]
    elif(board[0][2] == board[1][2] == board[2][2]and (board[0][2] is not None and board[1][2] is not None and board[2][2] is not None)): # Check third column
        print('column 3 returning true')
        return board[0][2]
    elif(board[0][0] == board[1][1] == board [2][2]and (board[0][0] is not None and board[1][1] is not None and board[2][2] is not None)): # Check first diagonal (top left to bottom right)
        print('diagonal 1 returning true')
        return board[0][0]
    elif(board[0][2] == board[1][1] == board[2][0]and (board[0][2] is not None and board[1][1] is not None and board[2][0] is not None)): # Check second diagonal (top right to bottom left)
        print('diagonal 2 returning true')
        return board[0][2]
    elif(len(actions(board)) == 0):
        return None
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    won = winner(board) # Check if a winner has been declared
    PossibleMovesLeft = len(actions(board)) # Check how many possible moves are left (Used to determine if a tie)
    if won or PossibleMovesLeft == 0: # Check if a player won the game or if a tie has occured
        return True # Return true if game is over
    else:
        return False # Return false if game is still occurring
   


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board) # Get the winner from the game
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
    if(terminal(board)): # Check if the game is already over
        return None 
    
    CurrentPlayer = player(board) # Get the current player
    if CurrentPlayer == 'X':
        # Functions output is (Score,Action) the score has an _ as it is not needed outside of MaxValue and MinValue
        _ , OptimalAction = MaxValue(board) # If the current player is X (Max player) call the MaxValue function
    elif CurrentPlayer == 'O':
        # Functions output is (Score,Action) the score has an _ as it is not needed outside of MaxValue and MinValue
        _ , OptimalAction = MinValue(board) # If the current player is O (Min Player) call the MinValue function
    return OptimalAction
    

def MaxValue(board):
    if terminal(board): # Check if the game is over
        return utility(board), None # Return utility and None as the return values for the Max and min function are score, action
    
    v = float('-inf') # Used to determine score of moves (1, 0, -1)
    BestMove = None # Used to hold the best move for the computer to make
    for action in actions(board): # Get all possible actions 
        score, _ = MinValue(result(board,action)) # Send all the actions to the MinValue function
        if score > v: # Check if the returned score is higher than the current score of V
            v = score # Set v to the score
            BestMove = action # Set the BestMove equal to the action
        if v == 1: # Check If the moves result in the MaxPlayer victory (X)
            return v, BestMove # return the score and the BestMove
    return v, BestMove

def MinValue(board):
    if terminal(board): # Check if game is over
        return utility(board), None # Return utility and None as the return values for the Max and min function are score, action
    
    v = float('inf') # Used to determine score of moves (1, 0, -1)
    BestMove = None # Used to hold the best move for the computer to make
    for action in actions(board): # Get all possible actions 
        score, _ = MaxValue(result(board,action)) # Send all the actions to the MaxValue function
        if score < v:  # Check if the returned score is lower than the current score of V
            v = score # Set v to the score
            BestMove = action # Set the BestMove equal to the action
        if v == -1: # Check if the moves result in a MinPlayer victory (O)
            return v, BestMove # return the score and the BestMove
    return v, BestMove
