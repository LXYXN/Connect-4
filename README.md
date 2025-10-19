# 🔴🔵 Connect Four (Text-Based Python)

A classic two-player connection game implemented as a terminal-based application in Python. 
Play against a randomized computer opponent on the standard 6x7 grid.

## ⭐ Features

This implementation includes robust logic for the core game mechanics:

* **Standard 6x7 Grid**: The classic game board is represented and printed directly to the console.

* **Player vs. Computer**: The primary gameplay mode pits the user (🔵) against a random-move computer opponent (🔴).

* **Gravity Simulation**: The `gravityChecker` ensures that discs correctly fall to the lowest available spot in the chosen column.

* **Win Detection**: Comprehensive checks for four consecutive discs are performed horizontally, vertically, and diagonally.

* **User Input Handling**: A custom `coordParser` handles column-row inputs (e.g., `C3`) and includes basic error handling for invalid coordinates.

## 🚀 Getting Started

### Prerequisites

You only need Python installed on your system. This code was written and tested with Python 3.

### Running the Game

1. **Save the Code**: Save the provided Python code as a file named `connect_four.py`.

2. **Run from Terminal**: Navigate to the directory where you saved the file and execute it:

`python connect_four.py`


## 🕹️ How to Play

1. **The Goal**: Be the first player to get four of your colored discs (🔵) in a row—horizontally, vertically, or diagonally.

2. **Input Format**: When prompted, enter a valid column letter followed by the row number (0-5).
  * Example: To drop a chip into the column **C** at row **4**, enter `C4`.

3. **Game Flow**: The game will alternate turns between you (🔵) and the computer (🔴) until a winner is declared or the board is full.

## 🪜 Project Structure (Key Functions)

The game is built around several dedicated functions, as outlined in the project report:

`printboard()` Displays the current state of the 6x7 grid using emojis.

`modifyArray()` Updates the internal board matrix after a move is made.

`checkWin()` The core logic for detecting a four-in-a-row winning condition.

`coordParser()` Translates user input (e.g., A0) into zero-indexed row/column coordinates.

`gravityChecker()` Verifies that a move is valid by ensuring the space below is occupied or it's the bottom row.

## 💡 Future Development

Your project report identified several excellent opportunities for enhancement, which could be tracked here as a roadmap:

1. **Graphical User Interface (GUI)**: Transition from the text-based interface to a visual one using libraries like Tkinter or Pygame.

2. **Advanced AI**: Improve the computer opponent's intelligence beyond random moves with algorithms like Minimax.

3. **Game Statistics**: Implement tracking for win/loss records and game history.
