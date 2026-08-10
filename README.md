# Tic Tac Toe (CLI)

A text-based, two-player Tic Tac Toe game built in Python. Players take turns entering their move using row and column coordinates, with full input validation, win detection, and draw detection.

This is the second project in a Python portfolio series focused on writing clean, well-structured, and idiomatic Python code.

## Features

- Two-player local gameplay (Player X vs Player O)
- Move input via row and column coordinates (e.g. `1,3`)
- Input validation for both malformed input and illegal moves (out-of-bounds or occupied cells)
- Win detection across all rows, columns, and both diagonals
- Draw detection when the board is full with no winner
- Clean separation between board logic and game flow

## Demo

```
  |   |
-----------
  | X |
-----------
  |   | O
```

## Technologies

- Python 3
- Standard library only (no external dependencies)

## Project Structure

```
tic-tac-toe/
├── board.py    # Board creation, display, and game rules
├── main.py     # Game loop and turn handling
└── README.md
```

The project separates **board mechanics** (`board.py`) from **game flow** (`main.py`). This keeps the win/draw/validation logic isolated and reusable — for example, it could be tested independently or reused by a future AI opponent without touching the game loop.

## How to Run

```bash
python main.py
```

Enter your move as `row,column` using 1-based indexing (e.g. `2,2` for the center cell). Players alternate turns automatically after each valid move.

## What I Learned

This project reinforced several Python idioms and design patterns:

- **List comprehensions** for building 2D data structures safely, avoiding shared-reference bugs (`[[x] * n] * n`)
- **Generator expressions** combined with `all()` for concise, short-circuiting condition checks
- **The "loop and a half" pattern** (`while True` + `break`) for loops whose exit condition is only known partway through an iteration
- **Specific exception handling** (`except ValueError`) instead of bare `except` clauses, to avoid silently swallowing unrelated bugs
- That most design decisions (data structure choices, validation placement, error handling strategy) have more than one valid answer — the right one depends on trade-offs, not a single "correct" rule

## Possible Improvements

- Replace the CLI interface with a graphical version (planned as a future iteration)
- Add a single-player mode against a simple AI opponent
- Add a "play again" loop instead of exiting after one game

## Author

[Your Name] — Part of a 10-project Python portfolio series.
