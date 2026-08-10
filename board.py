# Create a new empty 3x3 Tic Tac Toe board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Print the board to the console in a readable grid format
def display_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)

# Check if a move is legal: in bounds and on an empty cell
def is_valid_move(board, row, col):
    if row not in range(3) or col not in range(3):
        return False
    return board[row][col] == " "

# Try to place a mark on the board, validating the move first
def place_mark(board, row, col, mark):
    if not is_valid_move(board, row, col):
        return False
    board[row][col] = mark
    return True

# Check if the given mark has a winning row, column, or diagonal
def check_winner(board, mark):

    # Check rows
    for row in board:
        if all(cell == mark for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == mark for i in range(3)):
        return True

    if all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False

# Check if the board is full (call this only after check_winner)
def check_draw(board):
    return all(cell != " " for row in board for cell in row)
