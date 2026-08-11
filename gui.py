import tkinter as tk
from tkinter import messagebox
from board import create_board, place_mark, check_winner, check_draw, get_winning_cells

# ---------- Theme (centralized so the whole look can be tweaked from one place) ----------
BG_COLOR = "#F5F5F5"     # light background (window, frames)
CELL_BG = "#303841"      # dark charcoal, default cell background
CELL_HOVER = "#3f4750"   # slightly lighter charcoal, derived for hover feedback
ACCENT_X = "#76ABAE"     # teal, Player X + Restart button
ACCENT_O = "#FF5722"     # orange, Player O
WIN_COLOR = "#8FBC94"    # added: soft sage green, reads as "success" for the winning line
DARK_TEXT = "#303841"    # dark charcoal text on light backgrounds
LIGHT_TEXT = "#F5F5F5"   # light text on dark cell backgrounds
 
FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_STATUS = ("Segoe UI", 12)
FONT_CELL = ("Segoe UI", 28, "bold")

# ---------- Game state ----------
board = create_board()
current_player = "X"


# Handle a click on a specific board cell
def on_click(row, col):
    global current_player

    if not place_mark(board, row, col, mark=current_player):
        return

    color = ACCENT_X if current_player == "X" else ACCENT_O
    buttons[row][col].config(text=current_player, fg=color, disabledforeground=color)

    if check_winner(board, current_player):
        highlight_winning_cells(current_player)
        status_label.config(text=f"Player {current_player} wins!", fg=DARK_TEXT)
        disable_all_buttons()
        return

    if check_draw(board):
        status_label.config(text="It's a draw!", fg=DARK_TEXT)
        disable_all_buttons()
        return

    current_player = "O" if current_player == "X" else "X"
    update_status()


# Refresh the status label to reflect whose turn it is
def update_status():
    color = ACCENT_X if current_player == "X" else ACCENT_O
    status_label.config(text=f"Player {current_player}'s turn", fg=color)

# Change the background of the winning cells to make the win visible at a glance
def highlight_winning_cells(mark):
    winning_cells = get_winning_cells(board, mark)
    if winning_cells:
        for row, col in winning_cells:
            buttons[row][col].config(bg=WIN_COLOR)

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
            btn.config(text="", state=tk.NORMAL, bg=CELL_BG)
    root.update_idletasks()
    update_status()

# Lighten a cell's background when the mouse enters it (only if still playable)
def on_hover(event):
    if event.widget["state"] == tk.NORMAL:
        event.widget.config(bg=CELL_HOVER)
 
 
# Restore a cell's background when the mouse leaves it
def on_leave(event):
    if event.widget["state"] == tk.NORMAL:
        event.widget.config(bg=CELL_BG)

# Main window setup
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

main_frame = tk.Frame(root, bg=BG_COLOR, padx=40, pady=20)
main_frame.pack()

title_label = tk.Label(main_frame, text="TIC TAC TOE", font=FONT_TITLE,
                        fg=DARK_TEXT, bg=BG_COLOR)
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 6))
 
status_label = tk.Label(main_frame, text="Player X's turn", font=FONT_STATUS,
                         fg=ACCENT_X, bg=BG_COLOR)
status_label.grid(row=1, column=0, columnspan=3, pady=(0, 12))
 
board_frame = tk.Frame(main_frame, bg=BG_COLOR)
board_frame.grid(row=2, column=0, columnspan=3)

# Create the 3x3 grid of cell buttons
buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range (3):
        btn = tk.Button(
            board_frame, text="", font=FONT_CELL, width=4, height=2,
            bg=CELL_BG, fg=LIGHT_TEXT, activebackground=CELL_HOVER,
            relief="flat", bd=0,
            command=lambda r=row, c=col: on_click(r, c)
        )
        btn.grid(row=row, column=col, padx=4, pady=4)
        btn.bind("<Enter>", on_hover)
        btn.bind("<Leave>", on_leave)
        buttons[row][col] = btn

# Reset button, spanning the full width of the grid
reset_button = tk.Button(
    main_frame, text="Restart", font=FONT_STATUS, bg=ACCENT_X, fg=DARK_TEXT,
    activebackground="#5c5c80", relief="flat", bd=0, command=reset_game
)
reset_button.grid(row=3, column=0, columnspan=3, pady=(16, 0), sticky="we")


root.mainloop()