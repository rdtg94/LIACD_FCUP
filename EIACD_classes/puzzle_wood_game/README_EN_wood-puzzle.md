# Wood Block Puzzle

## English (US)

### Overview
Wood Block Puzzle is a Python-based puzzle game where players place wooden blocks on a grid to complete lines and columns. The game features multiple difficulty levels, AI-assisted gameplay, and several AI algorithms that can be used for automated play or comparison.

### Features
- Multiple difficulty levels (Easy, Medium, Hard, Expert)
- Variable board sizes (4x4, 5x5, 6x6, 7x7)
- Different piece shapes based on difficulty
- Diamonds for bonus points
- Line and column clearing mechanics
- Multiple game modes:
  - Normal gameplay
  - AI-assisted gameplay
  - AI automatic play
  - AI algorithm comparison

### Installation
1. Make sure you have Python 3.x installed
2. Download the game files:
   - `WoodPuzzle_1_4.py` - Main game file
   - `AI_algorithms_1_4.py` - AI implementation file
3. No additional dependencies required for basic gameplay

### Game Rules
- Start with an empty board with some obstacles and diamonds
- Place pieces on the board to complete lines and columns
- When a line or column is completely filled, it gets cleared and you earn points
- Capturing diamonds in cleared lines/columns gives bonus points
- Each move costs points based on difficulty level
- You can request a new piece at the cost of points
- The game ends when your score reaches zero

### How to Play
1. Run the game by executing: `python WoodPuzzle_1_4.py`
2. From the main menu, select one of the following options:
   - Play normal game
   - Play with AI help
   - Let AI play automatically
   - Compare AI algorithms
3. Select a difficulty level (1-4)
4. Follow the on-screen prompts to play

#### Normal Game Controls
- Enter row and column coordinates (e.g., `2 3`) to place a piece
- Enter `R` to request a new piece
- Enter `q` to quit to the main menu

### Difficulty Levels
1. **Easy (4x4 board)**
   - Simple piece shapes
   - Lower penalties for moves
   - Smaller board
2. **Medium (5x5 board)**
   - More complex pieces available
   - Increased penalties
3. **Hard (6x6 board)**
   - Even more complex pieces
   - Higher penalties
   - Larger board
4. **Expert (7x7 board)**
   - All piece shapes available
   - Maximum penalties
   - Largest board size

### Scoring System
- Starting score depends on difficulty (100-400 points)
- Each move costs points (scaled by difficulty)
- Requesting a new piece costs points
- Clearing lines and columns earns points
- Capturing diamonds gives bonus points

### AI Algorithms
The game features several AI search algorithms for automated play:

1. **Breadth-First Search (BFS)**
   - Explores all states at the same depth before moving deeper
   - Guarantees finding the shortest path to the goal
   
2. **Depth-First Search (DFS)**
   - Explores a branch to the end before backtracking
   - May find a solution quickly but not necessarily optimal
   
3. **Uniform Cost Search (UCS)**
   - Expands states in order of lowest cost
   - Guarantees finding the optimal solution
   
4. **Depth-Limited Search (DLS)**
   - DFS with a maximum depth limit
   - Avoids infinite search paths
   
5. **Iterative Deepening Search (IDS)**
   - Combines advantages of BFS and DFS
   - Guarantees finding the shortest path while using less memory
   
6. **Greedy Search**
   - Uses a heuristic to estimate distance to goal
   - Prioritizes states that seem closest to solution
   
7. **A* (A-Star) Search**
   - Combines path cost and heuristic
   - Guarantees optimal solution if heuristic is admissible
   
8. **Weighted A* Search**
   - Variation of A* that gives more weight to the heuristic
   - May find a solution faster at the cost of optimality

### Playing with AI Help
1. Select "Play with AI help" from the main menu
2. Choose a difficulty level
3. At each turn, you can request an AI suggestion
4. Select which algorithm you want to use for the suggestion
5. The AI will recommend a move that you can choose to follow or ignore

### Letting AI Play Automatically
1. Select "Let AI play automatically" from the main menu
2. Choose a difficulty level
3. Select which algorithm you want the AI to use
4. Watch as the AI plays the game automatically
5. Press Enter to advance to the next move or 'q' to quit

### Comparing AI Algorithms
1. Select "Compare AI algorithms" from the main menu
2. Choose a difficulty level
3. The program will run all AI algorithms on the same puzzle
4. Results show which algorithms found solutions, path lengths, states explored, and time taken

