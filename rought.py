# board = []
# for _ in range(3):
#     board.append(list(input().strip()))

# def transpose(board):
#     for i in range(3):
#         for j in range(i + 1, 3):
#             board[i][j], board[j][i] = board[j][i], board[i][j]

# transpose(board)

# for row in board:
#     print("".join(row))

# board = []
# for _ in range(3):
#     row = input().strip()
#     board.append(row)


# board = []
# for _ in range(3):
#     board.append(input().strip())

# def transpose(board):
#     return [
#         "".join(board[j][i] for j in range(3))
#         for i in range(3)
#     ]

# board = transpose(board)

# for row in board:
#     print(row)


board = ['X..', '.X.', '..X']

# for i in range(len(board)):
#     if (board[i] == board[i][0]*3) and (str(board[i][0]) != "."):
#             print(". ki maa ki chut")  


if "".join(board[i][j] for i,j in [(0,0), (1,1), (2,2)]) == str(board[0][0]*3): win = board[0][0]; print(win)
elif "".join(board[i][j] for i,j in [(0,2), (1,1), (2,0)]) == str(board[0][2]*3): win = board[0][2]; print(win)
