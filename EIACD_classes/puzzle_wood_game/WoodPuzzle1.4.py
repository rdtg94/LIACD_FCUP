import random
from AI_algorithms_1_4 import get_ai_move, play_with_ai, GameState, compare_algorithms

class WoodBlockPuzzle:
    def __init__(self, difficulty=1):
        """
        Initialize the Wood Block Puzzle game with different difficulty levels.
        
        Args:
            difficulty (int): Difficulty level from 1 to 4
                1 - Easy (4x4 board)
                2 - Medium (5x5 board)
                3 - Hard (6x6 board)
                4 - Expert (7x7 board)
        """
        # Set board size based on difficulty
        self.difficulty = min(max(difficulty, 1), 4)  # Ensure difficulty is between 1 and 4
        self.board_size = 3 + self.difficulty  # Board sizes: 4x4, 5x5, 6x6, 7x7
        
        # Initialize the board based on difficulty
        self.board = self._create_initial_board()
        
        # Initial score - higher for more difficult levels
        self.score = 100 * self.difficulty
        self.current_piece = self.generate_piece()
    
    def _create_initial_board(self):
        """Create the initial board based on the difficulty level."""
        # Start with an empty board
        board = [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]
        
        # Place diamonds and obstacles in a pattern that scales with board size
        # The pattern is similar across all difficulty levels, just scaled
        
        # Place diamonds (approximately 25% of board size squared)
        num_diamonds = max(3, round(0.15 * self.board_size * self.board_size))
        diamond_positions = []
        
        # Fixed diamond in top-right quadrant
        board[self.board_size // 4][self.board_size - 2] = "D"
        diamond_positions.append((self.board_size // 4, self.board_size - 2))
        
        # Fixed diamond in bottom-left quadrant
        board[self.board_size - 2][self.board_size // 4] = "D"
        diamond_positions.append((self.board_size - 2, self.board_size // 4))
        
        # Fixed diamond in middle-right area
        board[self.board_size // 2][self.board_size - 1] = "D"
        diamond_positions.append((self.board_size // 2, self.board_size - 1))
        
        # Add remaining diamonds randomly
        while len(diamond_positions) < num_diamonds:
            x, y = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
            if board[x][y] == " " and (x, y) not in diamond_positions:
                board[x][y] = "D"
                diamond_positions.append((x, y))
        
        # Place obstacles (approximately 15% of board size squared)
        num_obstacles = max(2, round(0.1 * self.board_size * self.board_size))
        obstacle_positions = []
        
        # Fixed obstacle in top-right corner
        board[0][self.board_size - 1] = "#"
        obstacle_positions.append((0, self.board_size - 1))
        
        # Fixed obstacle in bottom-right corner
        board[self.board_size - 1][self.board_size - 1] = "#"
        obstacle_positions.append((self.board_size - 1, self.board_size - 1))
        
        # Add remaining obstacles randomly, but don't place them adjacent to diamonds
        while len(obstacle_positions) < num_obstacles:
            x, y = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
            if board[x][y] == " " and not self._is_adjacent_to_diamond(x, y, diamond_positions):
                board[x][y] = "#"
                obstacle_positions.append((x, y))
        
        return board
    
    def _is_adjacent_to_diamond(self, x, y, diamond_positions):
        """Check if a position is adjacent to any diamond."""
        for dx, dy in diamond_positions:
            if abs(x - dx) <= 1 and abs(y - dy) <= 1:
                return True
        return False
    
    def generate_piece(self):
        """Generate a random piece based on difficulty level."""
        # Basic shapes available at all difficulty levels
        basic_shapes = [
            [[1, 1]],      # 2-block horizontal
            [[1], [1]],    # 2-block vertical
            [[1, 1, 1]],   # 3-block horizontal
            [[1], [1], [1]] # 3-block vertical
        ]
        
        # Medium shapes (available at difficulty 2+)
        medium_shapes = [
            [[1, 1], [1, 1]],  # 2x2 square
            [[1, 1], [1, 0]],  # L shape
            [[1, 1], [0, 1]],  # Reversed L shape
            [[1, 0], [1, 1]]   # L shape rotated
        ]
        
        # Hard shapes (available at difficulty 3+)
        hard_shapes = [
            [[1, 1, 1], [1, 0, 0]],  # L shape long
            [[1, 1, 1], [0, 0, 1]],  # Reversed L shape long
            [[1, 0], [1, 0], [1, 1]] # L shape rotated long
        ]
        
        # Expert shapes (only at difficulty 4)
        expert_shapes = [
            [[1, 1, 1], [0, 1, 0]],  # T shape
            [[0, 1, 0], [1, 1, 1]],  # Inverted T shape
            [[1, 1, 0], [0, 1, 1]]   # Z shape
        ]
        
        # Combine shapes based on difficulty
        available_shapes = basic_shapes.copy()
        if self.difficulty >= 2:
            available_shapes.extend(medium_shapes)
        if self.difficulty >= 3:
            available_shapes.extend(hard_shapes)
        if self.difficulty >= 4:
            available_shapes.extend(expert_shapes)
        
        return random.choice(available_shapes)
    
    def display_board(self):
        """Display the current state of the board."""
        print(f"\nDifficulty: {['Easy', 'Medium', 'Hard', 'Expert'][self.difficulty-1]}")
        print(f"Board Size: {self.board_size}x{self.board_size}")
        
        # Print column numbers
        print("   " + " ".join(str(i) for i in range(self.board_size)))
        print("  +" + "-" * (self.board_size * 2 - 1) + "+")
        
        # Print rows with row numbers
        for i, row in enumerate(self.board):
            print(f"{i} |" + "|".join(cell for cell in row) + "|")
            if i < self.board_size - 1:
                print("  +" + "-" * (self.board_size * 2 - 1) + "+")
        
        print("  +" + "-" * (self.board_size * 2 - 1) + "+")
        print(f"Score: {self.score}\n")
    
    def place_piece(self, x, y):
        """
        Place the current piece on the board at position (x, y).
        
        Args:
            x (int): Row index
            y (int): Column index
            
        Returns:
            bool: True if the piece was successfully placed, False otherwise
        """
        piece = self.current_piece
        piece_height, piece_width = len(piece), len(piece[0])
        
        # Check if the piece is out of bounds
        if x + piece_height > self.board_size or y + piece_width > self.board_size:
            print("Invalid move! Out of bounds.")
            return False
        
        # Check if the piece can be placed (no collisions)
        for i in range(piece_height):
            for j in range(piece_width):
                if piece[i][j] == 1 and (self.board[x + i][y + j] != " "):
                    print("Cannot place piece here! The space is occupied.")
                    return False
        
        # Place the piece on the board
        for i in range(piece_height):
            for j in range(piece_width):
                if piece[i][j] == 1:
                    self.board[x + i][y + j] = "#"
        
        # Penalty for making a move (scaled by difficulty)
        self.score -= 10 * self.difficulty // 2
        self.current_piece = self.generate_piece()
        return True
    
    def check_full_lines_and_columns(self):
        """Check for complete lines and columns, and clear them."""
        lines_cleared = 0
        columns_cleared = 0
        diamonds_captured = 0
        
        # Check complete rows
        for i in range(self.board_size):
            if all(cell == "#" or cell == "D" for cell in self.board[i]):
                lines_cleared += 1
                # Count diamonds and clear the row
                for j in range(self.board_size):
                    if self.board[i][j] == "D":
                        diamonds_captured += 1
                self.board[i] = [" " for _ in range(self.board_size)]
        
        # Check complete columns
        for j in range(self.board_size):
            if all(self.board[i][j] == "#" or self.board[i][j] == "D" for i in range(self.board_size)):
                columns_cleared += 1
                # Count diamonds and clear the column
                for i in range(self.board_size):
                    if self.board[i][j] == "D":
                        diamonds_captured += 1
                    self.board[i][j] = " "
        
        # Calculate score based on clears and difficulty
        if lines_cleared > 0 or columns_cleared > 0:
            base_points = 50 * self.difficulty
            self.score += base_points * (lines_cleared + columns_cleared)
            self.score += 100 * self.difficulty * diamonds_captured
            
            print(f"Cleared {lines_cleared} lines and {columns_cleared} columns!")
            if diamonds_captured > 0:
                print(f"Captured {diamonds_captured} diamonds!")
    
    def get_new_piece(self):
        """Request a new piece with a score penalty."""
        penalty = 10 * self.difficulty // 2
        self.score -= penalty
        if self.score < 0:
            self.score = 0
        self.current_piece = self.generate_piece()
        print(f"You lost {penalty} points for getting a new piece.")
    
    def play(self):
        """Play the game in normal mode."""
        print(f"\nStarting a new game on {['Easy', 'Medium', 'Hard', 'Expert'][self.difficulty-1]} difficulty")
        print(f"Board size: {self.board_size}x{self.board_size}")
        print("Place pieces to complete lines and columns and capture diamonds.")
        print("Press 'q' at any time to return to the main menu.")
        print("The game ends when you run out of points.")
        
        while self.score > 0:
            self.display_board()
            print("Current Piece:")
            for row in self.current_piece:
                print(" ".join("#" if cell == 1 else " " for cell in row))
            
            user_input = input("Enter position (row col), 'R' for new piece, or 'q' to quit: ").strip().lower()
            
            if user_input == 'q':
                print("Returning to main menu...")
                return  # Exit the game and return to menu
            elif user_input == 'r':
                self.get_new_piece()
            else:
                try:
                    x, y = map(int, user_input.split())
                    if self.place_piece(x, y):
                        self.check_full_lines_and_columns()
                except ValueError:
                    print("Invalid input. Enter two numbers separated by space (row col).")
        
        print("Game Over! You ran out of points.")
        print(f"Final Score: {self.score}")
    
    def play_with_ai_help(self):
        """Play with AI suggestions."""
        print(f"\nStarting a new game on {['Easy', 'Medium', 'Hard', 'Expert'][self.difficulty-1]} difficulty")
        print(f"Board size: {self.board_size}x{self.board_size}")
        print("You can ask for AI suggestions before making each move.")
        print("Press 'q' at any time to return to the main menu.")
        
        while self.score > 0:
            self.display_board()
            print("Current Piece:")
            for row in self.current_piece:
                print(" ".join("#" if cell == 1 else " " for cell in row))
            
            # Ask if the player wants an AI suggestion
            ai_help = input("Want AI suggestion? (y/n/q): ").strip().lower()
            
            if ai_help == 'q':
                print("Returning to main menu...")
                return  # Exit the game and return to menu
                
            if ai_help == 'y':
                # Ask which algorithm to use
                print("\nChoose AI algorithm:")
                print("1 - BFS (Breadth-First Search)")
                print("2 - DFS (Depth-First Search)")
                print("3 - UCS (Uniform Cost Search)")
                print("4 - DLS (Depth-Limited Search)")
                print("5 - IDS (Iterative Deepening Search)")
                print("6 - Greedy (Greedy Search)")
                print("7 - A* (A-Star)")
                print("8 - Weighted A* (Weighted A-Star)")
                print("q - Cancel AI suggestion")
                
                algo_choice = input("Enter your choice (1-8, q): ").strip().lower()
                
                if algo_choice == 'q':
                    continue
                
                algorithms = {
                    '1': 'bfs',
                    '2': 'dfs',
                    '3': 'ucs',
                    '4': 'dls',
                    '5': 'ids',
                    '6': 'greedy',
                    '7': 'astar',
                    '8': 'wastar'
                }
                
                if algo_choice in algorithms:
                    algorithm = algorithms[algo_choice]
                    print(f"Using {algorithm.upper()} to find the best move...")
                    
                    # Adjust time limit based on board size
                    time_limit = 5 + self.difficulty  # 6-9 seconds depending on difficulty
                    
                    # Get AI suggestion
                    move = get_ai_move(self, algorithm, 500 * self.difficulty, time_limit)
                    
                    if move:
                        if move == 'R':
                            print("AI suggests: Get a new piece (R)")
                        else:
                            x, y = move
                            print(f"AI suggests: Place piece at position ({x}, {y})")
                    else:
                        print("AI couldn't find a good move in the time limit.")
                else:
                    print("Invalid choice. No AI suggestion provided.")
            
            # The player makes their move
            user_input = input("Enter position (row col), 'R' for new piece, or 'q' to quit: ").strip().lower()
            
            if user_input == 'q':
                print("Returning to main menu...")
                return  # Exit the game and return to menu
            elif user_input == 'r':
                self.get_new_piece()
            else:
                try:
                    x, y = map(int, user_input.split())
                    if self.place_piece(x, y):
                        self.check_full_lines_and_columns()
                except ValueError:
                    print("Invalid input. Enter two numbers separated by space (row col).")
        
        print("Game Over! You ran out of points.")
        print(f"Final Score: {self.score}")


def compare_ai_algorithms(difficulty=1):
    """
    Compare all AI algorithms on the same problem with the selected difficulty.
    
    Args:
        difficulty (int): Difficulty level from 1 to 4
    
    Returns:
        dict: Results of algorithm comparison
    """
    # Create a new game with the selected difficulty
    game = WoodBlockPuzzle(difficulty)
    
    # Display the initial state
    print(f"Initial game state (Difficulty: {['Easy', 'Medium', 'Hard', 'Expert'][difficulty-1]}):")
    game.display_board()
    print("Current Piece:")
    for row in game.current_piece:
        print(" ".join("#" if cell == 1 else " " for cell in row))
    
    # Ask if the user wants to proceed or quit
    print("\nComparing all AI algorithms can take several minutes, especially at higher difficulties.")
    choice = input("Press Enter to continue, or 'q' to return to the main menu: ").strip().lower()
    
    if choice == 'q':
        print("Returning to main menu...")
        return None
    
    # Create initial state to pass to the algorithms
    initial_state = GameState(game.board, game.current_piece, game.score)
    
    # Adjust time limit and target score based on difficulty
    time_limit = 20 + 10 * difficulty  # 30-60 seconds per algorithm
    target_score = 500 * difficulty    # 500-2000 target score
    
    # Compare all algorithms
    results = compare_algorithms(initial_state, target_score, time_limit)
    
    # Wait for user input before returning to the menu
    input("\nPress Enter to return to the main menu...")
    
    return results


if __name__ == "__main__":
    running = True
    
    while running:
        print("\n===== Welcome to Wood Block Puzzle! =====")
        print("1 - Play normal game")
        print("2 - Play with AI help")
        print("3 - Let AI play automatically")
        print("4 - Compare AI algorithms")
        print("q - Quit game")
        
        choice = input("Enter your choice (1-4, q): ").strip().lower()
        
        if choice == 'q':
            print("Thanks for playing! Goodbye.")
            running = False
            continue
        
        # Select difficulty level for any mode
        if choice in ['1', '2', '3', '4']:
            print("\nSelect difficulty level:")
            print("1 - Easy (4x4 board)")
            print("2 - Medium (5x5 board)")
            print("3 - Hard (6x6 board)")
            print("4 - Expert (7x7 board)")
            print("q - Back to main menu")
            
            diff_choice = input("Enter difficulty (1-4, q): ").strip().lower()
            
            if diff_choice == 'q':
                continue  # Go back to main menu
                
            try:
                difficulty = int(diff_choice)
                if difficulty < 1 or difficulty > 4:
                    print("Invalid difficulty. Using Easy (level 1) as default.")
                    difficulty = 1
            except ValueError:
                print("Invalid input. Using Easy (level 1) as default.")
                difficulty = 1
        else:
            print("Invalid choice. Please try again.")
            continue
        
        if choice == '1':
            game = WoodBlockPuzzle(difficulty)
            game.play()
        elif choice == '2':
            game = WoodBlockPuzzle(difficulty)
            game.play_with_ai_help()
        elif choice == '3':
            game = WoodBlockPuzzle(difficulty)
            
            print("\nChoose AI algorithm:")
            print("1 - BFS (Breadth-First Search)")
            print("2 - DFS (Depth-First Search)")
            print("3 - UCS (Uniform Cost Search)")
            print("4 - DLS (Depth-Limited Search)")
            print("5 - IDS (Iterative Deepening Search)")
            print("6 - Greedy (Greedy Search)")
            print("7 - A* (A-Star)")
            print("8 - Weighted A* (Weighted A-Star)")
            print("q - Back to main menu")
            
            algo_choice = input("Enter your choice (1-8, q): ").strip().lower()
            
            if algo_choice == 'q':
                continue  # Go back to main menu
                
            algorithms = {
                '1': 'bfs',
                '2': 'dfs',
                '3': 'ucs',
                '4': 'dls',
                '5': 'ids',
                '6': 'greedy',
                '7': 'astar',
                '8': 'wastar'
            }
            
            if algo_choice in algorithms:
                algorithm = algorithms[algo_choice]
                # Adjust parameters based on difficulty
                target_score = 500 * difficulty
                time_limit = 10 * difficulty
                play_with_ai(game, algorithm, target_score, time_limit)
            else:
                print("Invalid choice. Using BFS as default.")
                target_score = 500 * difficulty
                time_limit = 10 * difficulty
                play_with_ai(game, 'bfs', target_score, time_limit)
        elif choice == '4':
            compare_ai_algorithms(difficulty)
