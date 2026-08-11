# Tic Tac Toe

A two-player Tic Tac Toe game built in Python, available in two versions: a command-line interface and a graphical interface built with Tkinter.

This is the second project in a Python portfolio series focused on writing clean, well-structured, and idiomatic Python code.

## Features

- Two-player local gameplay (Player X vs Player O)
- Win detection across all rows, columns, and both diagonals
- Draw detection when the board is full with no winner
- Clean separation between board logic and presentation layer (CLI or GUI)

### CLI version

- Move input via row and column coordinates (e.g. `1,3`)
- Input validation for malformed input and illegal moves

### GUI version (Tkinter)

- Clickable 3x3 grid of buttons with a custom color theme
- Hover feedback on playable cells
- Winning line highlighted in a distinct color when the game ends
- Dynamic status label showing whose turn it is, instead of interrupting pop-ups
- Reset button to start a new game without restarting the program

## Technologies

- Python 3
- Tkinter (GUI version) — included in Python's standard library
- No external dependencies

## Project Structure

```
tic-tac-toe/
├── board.py    # Board creation, display, and game rules (shared by both versions)
├── main.py     # CLI game loop and turn handling
├── gui.py      # Tkinter GUI version
└── README.md
```

`board.py` contains all the game rules — win detection, draw detection, move validation, and identifying the winning line — completely independent of how the game is presented to the player. This is what let the GUI version reuse the same logic without duplicating it: only the presentation layer (`main.py` vs `gui.py`) differs between versions.

## How to Run

**CLI version:**

```bash
python main.py
```

Enter your move as `row,column` using 1-based indexing (e.g. `2,2` for the center cell).

**GUI version:**

```bash
python gui.py
```

Click any empty cell to make your move. Use the Reset button to start a new game.

## What I Learned

Building and later redesigning the GUI version covered a real shift in programming model, plus several Tkinter-specific techniques:

- **Event-driven programming**: moving from a `while True` loop that controls the flow, to callback functions that Tkinter calls in response to user actions, with `mainloop()` handing control over to the framework
- **Closures and late binding**: why `lambda r=row, c=col: on_click(r, c)` is necessary inside a loop — without capturing `row`/`col` as default arguments, every button would end up calling `on_click` with the loop's final values instead of the value at creation time
- **`global` for reassignment vs. mutation**: `board` doesn't need `global` because it's mutated in place by `place_mark`, but `current_player` and `board = create_board()` in `reset_game()` are full reassignments and do require it
- **No hoisting in Python**: unlike JavaScript, function definitions aren't hoisted — a function must be defined before it's referenced directly (e.g. `command=reset_game`)
- **Event binding beyond `command`**: `.bind("<Enter>", ...)` / `.bind("<Leave>", ...)` react to mouse movement, not just clicks, enabling hover feedback
- **Forcing a redraw with `update_idletasks()`**: Tkinter batches visual updates instead of applying them instantly; forcing an idle-task flush avoided a stale button color after resetting the game
- **Centralized color theming**: defining a palette as named constants at the top of the file, and deriving interaction states (hover, etc.) from a base color instead of hardcoding unrelated values
- **Extending shared logic without duplicating it**: adding `get_winning_cells()` to `board.py` (alongside the existing `check_winner()`) so the GUI could report _where_ a win happened, without re-implementing the win-checking rules in the presentation layer

## Possible Improvements

- Add a single-player mode against a simple AI opponent
- Track and display a running score across multiple rounds
- Add subtle animations or sound effects on win/draw

## Author

[Your Name] — Part of a 10-project Python portfolio series.
