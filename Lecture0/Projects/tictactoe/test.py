from tictactoe import initial_state, player, actions, winner, terminal, utility

board = initial_state()
# print(winner(board))
# print(terminal(board))
print(utility(board))
board[0][0] = 'X'
board[0][1] = 'O'
board[0][2] = 'X'
# print(terminal(board))
# print(player(board))
# print(actions(board))
# print(winner(board))
print(utility(board))