# Wood Block Puzzle with Multiple Difficulty Levels

This game is an implementation of a wood block puzzle with different difficulty levels and various Artificial Intelligence algorithms.

## Main Features

- 4 difficulty levels with progressively increasing board sizes
- Multiple game modes: manual, with AI suggestions, or fully automated
- Comparison of 8 different AI algorithms to solve the puzzle
- Game boards that adapt to the difficulty level
- More complex pieces at higher difficulty levels

## Difficulty Levels

1. **Easy** - 4x4 Board
   - Ideal for beginners
   - Simple pieces
   - Initial score: 100 points

2. **Medium** - 5x5 Board
   - Moderate difficulty
   - Includes additional L-shaped pieces
   - Initial score: 200 points

3. **Hard** - 6x6 Board
   - For experienced players
   - Includes more complex pieces
   - Initial score: 300 points

4. **Expert** - 7x7 Board
   - The greatest challenge
   - Includes all pieces, including T and Z shapes
   - Initial score: 400 points

## Game Modes

### 1. Normal Game

In this mode, you play manually on the chosen board. The goal is to complete lines and columns to earn points and capture diamonds.

### 2. Game with AI Help

You play manually, but can request move suggestions from the AI before each move. You can choose from different algorithms to get the suggestion.

Available algorithms:
- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- UCS (Uniform Cost Search)
- DLS (Depth-Limited Search)
- IDS (Iterative Deepening Search)
- Greedy (Greedy Search)
- A* (A-Star)
- Weighted A* (Weighted A-Star)

### 3. Automatic Game with AI

The AI plays automatically using the chosen algorithm. You simply observe how it solves the puzzle.

### 4. Algorithm Comparison

This mode runs all AI algorithms on the same initial board and compares their performance in terms of:
- Execution time
- States explored
- Length of path found
- Whether it found a solution or not

## How to Play

### Basic Rules

1. You start with an initial score that depends on the difficulty level
2. Each move costs points (more points at higher difficulty levels)
3. Completing lines or columns earns points
4. Capturing diamonds earns additional points
5. The game ends when you run out of points

### Commands

- To place a piece, enter the coordinates as "row column" (ex: "2 3")
- To request a new piece, type "R" (you will lose some points)
- To exit the game and return to the main menu, type "q" at any time
- To exit the game completely, type "q" in the main menu

## Installation and Execution

1. Make sure you have Python 3.6 or higher installed
2. Clone or download the files `NOME DO FICHEIRO FINAL.py` and `NOME DO FICHEIRO FINAL DOS ALGORITMOS.py`
3. Run the game with the command:

```
python NOME DO FICHEIRO FINAL.py
```

## Strategic Tips

- At higher difficulty levels, consider asking for help from the A* or Weighted A* algorithm for optimal moves
- Try to complete lines or columns containing diamonds to maximize your score
- Avoid requesting new pieces unnecessarily, as this decreases your score
- On larger boards, start filling from the corners to increase your chances of completing multiple lines/columns
