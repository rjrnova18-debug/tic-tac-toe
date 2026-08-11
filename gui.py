import tkinter as tk
from tkinter import messagebox
from board import create_board, place_mark, check_winner, check_draw

# Game state (persists across button clicks, unlike the CLI's local variables)
board = create_board()
current_player = "X"


# Handle a click on a specific board cell
def on_click(row, col):
    global current_player

    if not place_mark(board, row, col, mark=current_player):
        return

    buttons[row][col].config(text=current_player)

    if check_winner(board, current_player):
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        disable_all_buttons()
        return

    if check_draw(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        disable_all_buttons()
        return

    current_player = "O" if current_player == "X" else "X"

# Disable every cell button once the game has ended
def disable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state=tk.DISABLED)

# Reset the board and buttons to start a new game
def reset_game():
    global board, current_player
    board = create_board()
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn.config(text="", state=tk.NORMAL)


# Main window setup
root = tk.Tk()
root.title("Tic Tac Toe")

# Create the 3x3 grid of cell buttons
buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range (3):
        btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                        command=lambda r=row, c=col: on_click(r, c))

        btn.grid(row=row, column=col)
        buttons[row][col] = btn

# Reset button, spanning the full width of the grid
reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")


root.mainloop()