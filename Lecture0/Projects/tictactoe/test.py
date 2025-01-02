from tictactoe import initial_state, player, actions, winner, terminal, utility, minimax, result

board = initial_state()
# print(winner(board))
# print(terminal(board))
# print(terminal(board))
board[0][0] = 'X'
board[0][-1] = 'X'
board[0][-2] = 'O'
print(result(board,(0,-4)))
# board[1][0] = 'O'
# board[1][1] = 'X'
# board[1][2] = 'X'
# board[2][0] = 'X'
# board[2][1] = 'O'
# board[2][2] = 'O'
# print(terminal(board))
# print(player(board))
# print(actions(board))
# print(winner(board))
print(board)
# print(minimax(board))
# XOO
# OXX
# XOO



# ox#
##o
#x#