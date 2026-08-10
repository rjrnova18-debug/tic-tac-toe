from board import create_board, display_board, place_mark, check_winner, check_draw 

def main():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)
        move = input(f"Player {current_player}, enter your move (row,col): ")
        try:
            row, col = move.split(",")
            row = int(row) - 1
            col = int(col) - 1
        except ValueError:
            print("Invalid format. Please enter row,col (e.g., 1,2). \n")
            continue

        if not place_mark(board, row, col, mark=current_player):
            print("Invalid move. Try again. \n")
            continue

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()