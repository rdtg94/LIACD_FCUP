"""
AI_algorithms.py - Implementation of search algorithms for the WoodBlockPuzzle game
This module contains implementations of various search algorithms:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform Cost Search
- Depth-Limited Search
- Iterative Deepening Search
- Greedy Search
- A* (A-Star) Search
- Weighted A* Search

Modified to support multiple board sizes based on difficulty levels
"""

import copy
import heapq
from collections import deque
import time

class GameState:
    """
    Class that represents a state of the WoodBlockPuzzle game.
    Stores the current board, current piece, score, and the path of moves made.
    """
    def __init__(self, board, current_piece, score, path=None):
        """
        Initializes a new game state.
        
        Args:
            board (list): A board matrix representing the current state.
            current_piece (list): A matrix representing the current piece.
            score (int): The current player's score.
            path (list, optional): A list of moves that led to this state.
        """
        self.board = copy.deepcopy(board)  # Makes a deep copy to avoid accidental modifications
        self.current_piece = copy.deepcopy(current_piece)
        self.score = score
        self.path = path if path is not None else []
        # Calculate board size dynamically rather than hardcoding
        self.board_size = len(board)
    
    def __eq__(self, other):
        """
        Compares two states to check if they are equal.
        Two states are considered equal if they have the same board and the same current piece.
        
        Args:
            other (GameState): The other state to compare with.
            
        Returns:
            bool: True if the states are equal, False otherwise.
        """
        return (self.board == other.board and 
                self.current_piece == other.current_piece)
    
    def __hash__(self):
        """
        Calculates a hash value for the state, allowing its use in sets and dictionaries.
        
        Returns:
            int: A unique hash value for this state.
        """
        # Converts the board and current piece into tuples to make them hashable
        board_tuple = tuple(tuple(row) for row in self.board)
        piece_tuple = tuple(tuple(row) for row in self.current_piece)
        return hash((board_tuple, piece_tuple, self.score))
    
    def __lt__(self, other):
        """
        Defines the comparison order between two states.
        Used by the priority queue in uniform cost search.
        
        Args:
            other (GameState): The other state to compare with.
            
        Returns:
            bool: True if this state has a higher score, False otherwise.
        """
        # In uniform cost search, we want to maximize the score
        return self.score > other.score

def get_valid_moves(state):
    """
    Gets all valid moves from a state.
    A move can be placing the current piece in a valid position or requesting a new piece.
    
    Args:
        state (GameState): The current game state.
        
    Returns:
        list: A list of tuples (x, y) representing valid positions or 'R' to request a new piece.
    """
    valid_moves = []
    piece = state.current_piece
    piece_height, piece_width = len(piece), len(piece[0])
    board_size = state.board_size
    
    # Checks all possible positions on the board
    for x in range(board_size - piece_height + 1):
        for y in range(board_size - piece_width + 1):
            valid = True
            
            # Checks if the piece fits in this position
            for i in range(piece_height):
                for j in range(piece_width):
                    if piece[i][j] == 1 and state.board[x + i][y + j] != " ":
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                valid_moves.append((x, y))
    
    # Adds the option to request a new piece
    valid_moves.append('R')
    
    return valid_moves

def apply_move(state, move):
    """
    Applies a move to a state and returns the resulting new state.
    
    Args:
        state (GameState): The current game state.
        move: A tuple (x, y) to place the piece or 'R' to request a new piece.
        
    Returns:
        GameState: The new state after applying the move.
    """
    # Creates a copy of the current state
    new_state = GameState(state.board, state.current_piece, state.score, state.path + [move])
    board_size = new_state.board_size
    
    # Determine the difficulty level based on the board size
    difficulty = board_size - 3  # 4x4 → 1, 5x5 → 2, etc.
    
    if move == 'R':
        # Request a new piece
        new_state.score -= 10 * difficulty // 2  # Scaled penalty based on difficulty
        if new_state.score < 0:
            new_state.score = 0
        # Simulates generating a new piece (in practice, this would be random)
        # Here, we use a simple 1x1 piece to simplify
        new_state.current_piece = [[1]]
    else:
        # Place the piece at position (x, y)
        x, y = move
        piece = new_state.current_piece
        piece_height, piece_width = len(piece), len(piece[0])
        
        # Places the piece on the board
        for i in range(piece_height):
            for j in range(piece_width):
                if piece[i][j] == 1:
                    new_state.board[x + i][y + j] = "#"
        
        new_state.score -= 10 * difficulty // 2  # Scaled penalty based on difficulty
        
        # Checks and clears complete lines and columns
        check_full_lines_and_columns(new_state)
        
        # Simulates generating a new piece
        new_state.current_piece = [[1]]
    
    return new_state

def check_full_lines_and_columns(state):
    """
    Checks if there are complete lines or columns on the board and clears them.
    Also captures diamonds and adds points.
    
    Args:
        state (GameState): The current game state.
    """
    board_size = state.board_size
    difficulty = board_size - 3  # Determine difficulty from board size
    
    lines_cleared = 0
    columns_cleared = 0
    diamonds_captured = 0
    
    # Checks complete rows
    for i in range(board_size):
        if all(cell == "#" or cell == "D" for cell in state.board[i]):
            lines_cleared += 1
            # Count and process diamonds
            for j in range(board_size):
                if state.board[i][j] == "D":
                    diamonds_captured += 1
                    state.board[i][j] = " "
            state.board[i] = [" " for _ in range(board_size)]
    
    # Checks complete columns
    for j in range(board_size):
        if all(state.board[i][j] == "#" or state.board[i][j] == "D" for i in range(board_size)):
            columns_cleared += 1
            # Count and process diamonds
            for i in range(board_size):
                if state.board[i][j] == "D":
                    diamonds_captured += 1
                    state.board[i][j] = " "
            # Clears the column
            for i in range(board_size):
                state.board[i][j] = " "
    
    # Add points based on difficulty
    if lines_cleared > 0 or columns_cleared > 0:
        base_points = 50 * difficulty
        state.score += base_points * (lines_cleared + columns_cleared)
        state.score += 100 * difficulty * diamonds_captured

def is_goal_state(state, target_score=500):
    """
    Checks if a state is a goal state.
    In this case, a goal state is one where the score reaches or exceeds a target value.
    
    Args:
        state (GameState): The state to be checked.
        target_score (int, optional): The target score to consider a state as a goal.
        
    Returns:
        bool: True if the state is a goal state, False otherwise.
    """
    return state.score >= target_score

def bfs(initial_state, target_score=500, time_limit=30):
    """
    Implements the Breadth-First Search (BFS) algorithm.
    BFS explores all nodes at a level before moving to the next level.
    Guarantees finding the shortest path to the goal, if it exists.
    
    Args:
        initial_state (GameState): The initial game state.
        target_score (int, optional): The target score to consider a state as a goal.
        time_limit (int, optional): Time limit in seconds for the search.
        
    Returns:
        tuple: (path_found, explored_states, elapsed_time)
            - path_found is a list of moves or None if no solution is found
            - explored_states is the number of states explored
            - elapsed_time is the elapsed time in seconds
    """
    print("Starting Breadth-First Search (BFS)...")
    start_time = time.time()
    
    # Queue of states to be explored (FIFO - First In, First Out)
    queue = deque([initial_state])
    
    # Set of already visited states to avoid cycles
    visited = set()
    visited.add(hash(initial_state))
    
    # Counter of explored states
    explored_states = 0
    
    while queue and time.time() - start_time < time_limit:
        # Removes the first state from the queue
        current_state = queue.popleft()
        explored_states += 1
        
        # Checks if it's a goal state
        if is_goal_state(current_state, target_score):
            elapsed_time = time.time() - start_time
            print(f"Solution found! Explored states: {explored_states}")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            return current_state.path, explored_states, elapsed_time
        
        # Generates all valid moves
        valid_moves = get_valid_moves(current_state)
        
        # For each valid move, generates a new state and adds it to the queue
        for move in valid_moves:
            new_state = apply_move(current_state, move)
            new_state_hash = hash(new_state)
            
            # Checks if the state has already been visited
            if new_state_hash not in visited:
                queue.append(new_state)
                visited.add(new_state_hash)
    
    # If it exited the loop, it did not find a solution or exceeded the time limit
    elapsed_time = time.time() - start_time
    if time.time() - start_time >= time_limit:
        print(f"Time limit exceeded! Explored states: {explored_states}")
    else:
        print(f"Solution not found! Explored states: {explored_states}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    return None, explored_states, elapsed_time

def dfs(initial_state, target_score=500, time_limit=30):
    """
    Implements the Depth-First Search (DFS) algorithm.
    DFS explores a branch to the end before backtracking.
    May find a solution more quickly in certain cases, but does not guarantee the optimal solution.
    
    Args:
        initial_state (GameState): The initial game state.
        target_score (int, optional): The target score to consider a state as a goal.
        time_limit (int, optional): Time limit in seconds for the search.
        
    Returns:
        tuple: (path_found, explored_states, elapsed_time)
            - path_found is a list of moves or None if no solution is found
            - explored_states is the number of states explored
            - elapsed_time is the elapsed time in seconds
    """
    print("Starting Depth-First Search (DFS)...")
    start_time = time.time()
    
    # Stack of states to be explored (LIFO - Last In, First Out)
    stack = [initial_state]
    
    # Set of already visited states to avoid cycles
    visited = set()
    visited.add(hash(initial_state))
    
    # Counter of explored states
    explored_states = 0
    
    while stack and time.time() - start_time < time_limit:
        # Removes the last state from the stack
        current_state = stack.pop()
        explored_states += 1
        
        # Checks if it's a goal state
        if is_goal_state(current_state, target_score):
            elapsed_time = time.time() - start_time
            print(f"Solution found! Explored states: {explored_states}")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            return current_state.path, explored_states, elapsed_time
        
        # Generates all valid moves
        valid_moves = get_valid_moves(current_state)
        
        # For each valid move, generates a new state and adds it to the stack
        # Traverses the moves in reverse order so that the first move is explored last
        for move in reversed(valid_moves):
            new_state = apply_move(current_state, move)
            new_state_hash = hash(new_state)
            
            # Checks if the state has already been visited
            if new_state_hash not in visited:
                stack.append(new_state)
                visited.add(new_state_hash)
    
    # If it exited the loop, it did not find a solution or exceeded the time limit
    elapsed_time = time.time() - start_time
    if time.time() - start_time >= time_limit:
        print(f"Time limit exceeded! Explored states: {explored_states}")
    else:
        print(f"Solution not found! Explored states: {explored_states}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    return None, explored_states, elapsed_time

def uniform_cost_search(initial_state, target_score=500, time_limit=30):
    """
    Implements the Uniform Cost Search algorithm.
    This algorithm expands nodes in ascending order of cost (or descending order of score, in this case).
    Guarantees finding the optimal solution in terms of score.
    
    Args:
        initial_state (GameState): The initial game state.
        target_score (int, optional): The target score to consider a state as a goal.
        time_limit (int, optional): Time limit in seconds for the search.
        
    Returns:
        tuple: (path_found, explored_states, elapsed_time)
            - path_found is a list of moves or None if no solution is found
            - explored_states is the number of states explored
            - elapsed_time is the elapsed time in seconds
    """
    print("Starting Uniform Cost Search...")
    start_time = time.time()
    
    # Priority queue ordered by score (highest score first)
    # Format: (negative score, counter, state)
    # We use negative score because heapq orders by the lowest value
    # Counter to break ties between states with the same score
    priority_queue = [(initial_state.score * -1, 0, initial_state)]
    heapq.heapify(priority_queue)
    
    # Counter to break ties between states with the same score
    counter = 1
    
    # Set of already visited states to avoid cycles
    visited = set()
    visited.add(hash(initial_state))
    
    # Counter of explored states
    explored_states = 0
    
    while priority_queue and time.time() - start_time < time_limit:
        # Removes the state with the highest score (lowest negative) from the queue
        _, _, current_state = heapq.heappop(priority_queue)
        explored_states += 1
        
        # Checks if it's a goal state
        if is_goal_state(current_state, target_score):
            elapsed_time = time.time() - start_time
            print(f"Solution found! Explored states: {explored_states}")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            return current_state.path, explored_states, elapsed_time
        
        # Generates all valid moves
        valid_moves = get_valid_moves(current_state)
        
        # For each valid move, generates a new state and adds it to the queue
        for move in valid_moves:
            new_state = apply_move(current_state, move)
            new_state_hash = hash(new_state)
            
            # Checks if the state has already been visited
            if new_state_hash not in visited:
                heapq.heappush(priority_queue, (new_state.score * -1, counter, new_state))
                counter += 1
                visited.add(new_state_hash)
    
    # If it exited the loop, it did not find a solution or exceeded the time limit
    elapsed_time = time.time() - start_time
    if time.time() - start_time >= time_limit:
        print(f"Time limit exceeded! Explored states: {explored_states}")
    else:
        print(f"Solution not found! Explored states: {explored_states}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    return None, explored_states, elapsed_time

def depth_limited_search(initial_state, depth_limit=10, target_score=500, time_limit=30):
    """
    Implements the Depth-Limited Search algorithm.
    It's a variation of DFS that limits the depth of the search.
    
    Args:
        initial_state (GameState): The initial game state.
        depth_limit (int, optional): The maximum depth of the search.
        target_score (int, optional): The target score to consider a state as a goal.
        time_limit (int, optional): Time limit in seconds for the search.
        
    Returns:
        tuple: (path_found, explored_states, elapsed_time)
            - path_found is a list of moves or None if no solution is found
            - explored_states is the number of states explored
            - elapsed_time is the elapsed time in seconds
    """
    print(f"Starting Depth-Limited Search (limit={depth_limit})...")
    start_time = time.time()
    
    # Implements the depth-limited search recursively
    def recursive_dls(state, depth, visited):
        nonlocal explored_states
        
        # Checks if it exceeded the time limit
        if time.time() - start_time >= time_limit:
            return None
        
        # Increments the explored states counter
        explored_states += 1
        
        # Checks if it's a goal state
        if is_goal_state(state, target_score):
            return state.path
        
        # Reached the depth limit
        if depth <= 0:
            return None
        
        # Generates all valid moves
        valid_moves = get_valid_moves(state)
        
        # For each valid move, generates a new state and does the recursive search
        for move in valid_moves:
            new_state = apply_move(state, move)
            new_state_hash = hash(new_state)
            
            # Checks if the state has already been visited
            if new_state_hash not in visited:
                visited.add(new_state_hash)
                result = recursive_dls(new_state, depth - 1, visited)
                
                # If a solution was found, returns it
                if result is not None:
                    return result
                
                # Removes the state from the visited set to allow exploring it in another path
                visited.remove(new_state_hash)
        
        # No solution found in this branch
        return None
    
    # Counter of explored states
    explored_states = 0
    
    # Starts the recursive search
    visited = set([hash(initial_state)])
    result = recursive_dls(initial_state, depth_limit, visited)
    
    # Calculates the elapsed time
    elapsed_time = time.time() - start_time
    
    if result is not None:
        print(f"Solution found! Explored states: {explored_states}")
    elif time.time() - start_time >= time_limit:
        print(f"Time limit exceeded! Explored states: {explored_states}")
    else:
        print(f"Solution not found within the depth limit! Explored states: {explored_states}")
    
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    return result, explored_states, elapsed_time

def iterative_deepening(initial_state, max_depth=20, target_score=500, time_limit=30):
    """
    Implements the Iterative Deepening algorithm.
    Combines the advantages of BFS and DFS, guaranteeing to find the shortest path
    to the goal, if it exists, using memory space similar to DFS.
    
    Args:
        initial_state (GameState): The initial game state.
        max_depth (int, optional): The maximum depth to increment to.
        target_score (int, optional): The target score to consider a state as a goal.
        time_limit (int, optional): Time limit in seconds for the search.
        
    Returns:
        tuple: (path_found, explored_states, elapsed_time)
            - path_found is a list of moves or None if no solution is found
            - explored_states is the total number of states explored
            - elapsed_time is the elapsed time in seconds
    """
    print("Starting Iterative Deepening...")
    start_time = time.time()
    
    # Total counter of explored states
    total_explored_states = 0
    
    # For each depth from 1 to max_depth
    for depth in range(1, max_depth + 1):
        print(f"Trying depth {depth}...")
        
        # Checks if it exceeded the time limit
        if time.time() - start_time >= time_limit:
            elapsed_time = time.time() - start_time
            print(f"Time limit exceeded! Total explored states: {total_explored_states}")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            return None, total_explored_states, elapsed_time
        
        # Executes the depth-limited search for this depth
        result, explored_states, _ = depth_limited_search(
            initial_state, depth, target_score, time_limit - (time.time() - start_time)
        )
        
        # Adds the explored states to the total
        total_explored_states += explored_states
        
        # If a solution was found, returns it
        if result is not None:
            elapsed_time = time.time() - start_time
            print(f"Solution found at depth {depth}!")
            print(f"Total explored states: {total_explored_states}")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            return result, total_explored_states, elapsed_time
    
    # If it got here, no solution was found up to the maximum depth
    elapsed_time = time.time() - start_time
    print(f"Solution not found up to depth {max_depth}!")
    print(f"Total explored states: {total_explored_states}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    return None, total_explored_states, elapsed_time

# Heuristics for informed algorithms

def heuristic_score_potential(state, target_score=500):
    """
    Heuristic that estimates the scoring potential of a state.
    The closer to the target_score, the better the state.
    
    Args:
        state (GameState): The state to evaluate.
        target_score (int, optional): The target score to consider a state as a goal.
        
    Returns:
        float: A lower value for more promising states (heuristic for minimization).
    """
    # The closer the state is to the target_score, the lower the returned value
    return max(0, target_score - state.score)

def heuristic_board_potential(state):
    """
    Heuristic that evaluates the potential of the board to score.
    Counts the number of filled cells in each row and column and estimates
    how close the board is to completing rows or columns.
    
    Args:
        state (GameState): The state to evaluate.
        
    Returns:
        float: A lower value for more promising states (heuristic for minimization).
    """
    board = state.board
    board_size = state.board_size
    
    # Counts the number of filled cells in each row and column
    row_fill = [sum(1 for cell in row if cell == "#" or cell == "D") for row in board]
    col_fill = [sum(1 for row in board if row[j] == "#" or row[j] == "D") for j in range(board_size)]
    
    # Counts the number of diamonds in each row and column
    row_diamonds = [sum(1 for cell in row if cell == "D") for row in board]
    col_diamonds = [sum(1 for row in board if row[j] == "D") for j in range(board_size)]
    
    # Calculates the scoring potential
    # For each nearly complete row/column, we give a higher bonus
    row_potential = sum((board_size - count) * (count > 0) for count in row_fill)
    col_potential = sum((board_size - count) * (count > 0) for count in col_fill)
    
    # Bonus for rows/columns with diamonds
    diamond_potential = sum(row_diamonds) + sum(col_diamonds)
    
    # The lower the potential, the more promising the state
    # We use a negative value so that it's a minimization heuristic
    return -(row_potential + col_potential + 3 * diamond_potential)

def greedy_search(initial_state, target_score=500, time_limit=30):
    """
    Implements the Greedy Search algorithm.
    This algorithm uses a heuristic to estimate how close each state is to the goal,
    and always chooses the state that seems closest to the goal.
    
    Args:
        initial_state (GameState): The initial game state.
        target_score (int, optional): The target score to consider a state as a goal.
        time_limit (int, optional): Time limit in seconds for the search.
        
    Returns:
        tuple: (path_found, explored_states, elapsed_time)
            - path_found is a list of moves or None if no solution is found
            - explored_states is the number of states explored
            - elapsed_time is the elapsed time in seconds
    """
    print("Starting Greedy Search...")
    start_time = time.time()
    
    # Priority queue ordered by heuristic (lowest value first)
    # Format: (heuristic, counter, state)
    priority_queue = [(heuristic_score_potential(initial_state, target_score), 0, initial_state)]
    heapq.heapify(priority_queue)
    
    # Counter to break ties between states with the same heuristic
    counter = 1
    
    # Set of already visited states to avoid cycles
    visited = set()
    visited.add(hash(initial_state))
    
    # Counter of explored states
    explored_states = 0
    
    while priority_queue and time.time() - start_time < time_limit:
        # Removes the state with the lowest heuristic value from the queue
        _, _, current_state = heapq.heappop(priority_queue)
        explored_states += 1
        
        # Checks if it's a goal state
        if is_goal_state(current_state, target_score):
            elapsed_time = time.time() - start_time
            print(f"Solution found! Explored states: {explored_states}")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            return current_state.path, explored_states, elapsed_time
        
        # Generates all valid moves
        valid_moves = get_valid_moves(current_state)
        
        # For each valid move, generates a new state and adds it to the queue
        for move in valid_moves:
            new_state = apply_move(current_state, move)
            new_state_hash = hash(new_state)
            
            # Checks if the state has already been visited
            if new_state_hash not in visited:
                h_value = heuristic_score_potential(new_state, target_score)
                heapq.heappush(priority_queue, (h_value, counter, new_state))
                counter += 1
                visited.add(new_state_hash)
    
    # If it exited the loop, it did not find a solution or exceeded the time limit
    elapsed_time = time.time() - start_time
    if time.time() - start_time >= time_limit:
        print(f"Time limit exceeded! Explored states: {explored_states}")
    else:
        print(f"Solution not found! Explored states: {explored_states}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    return None, explored_states, elapsed_time

def a_star_search(initial_state, target_score=500, time_limit=30):
    """
    Implements the A* (A-Star) algorithm.
    This algorithm combines the cost of the path so far with a heuristic
    to estimate the remaining cost to the goal.
    
    Args:
        initial_state (GameState): The initial game state.
        target_score (int, optional): The target score to consider a state as a goal.
        time_limit (int, optional): Time limit in seconds for the search.
        
    Returns:
        tuple: (path_found, explored_states, elapsed_time)
            - path_found is a list of moves or None if no solution is found
            - explored_states is the number of states explored
            - elapsed_time is the elapsed time in seconds
    """
    print("Starting A* (A-Star) Search...")
    start_time = time.time()
    
    # Priority queue ordered by the function f(n) = g(n) + h(n)
    # g(n) is the cost so far (represented by the score)
    # h(n) is the heuristic (estimate of the remaining cost)
    # Format: (f_value, counter, state)
    
    # We calculate the f(n) function as a combination of cost and heuristic
    # We want to maximize the score, so g(n) = score
    # And we want to minimize the distance to the goal, so h(n) = heuristic
    initial_h = heuristic_score_potential(initial_state, target_score)
    initial_g = initial_state.score
    initial_f = initial_h - initial_g  # We minimize f = h - g
    
    priority_queue = [(initial_f, 0, initial_state)]
    heapq.heapify(priority_queue)
    
    # Counter to break ties between states with the same f value
    counter = 1
    
    # Set of already visited states to avoid cycles
    visited = set()
    visited.add(hash(initial_state))
    
    # Counter of explored states
    explored_states = 0
    
    while priority_queue and time.time() - start_time < time_limit:
        # Removes the state with the lowest f value from the queue
        _, _, current_state = heapq.heappop(priority_queue)
        explored_states += 1
        
        # Checks if it's a goal state
        if is_goal_state(current_state, target_score):
            elapsed_time = time.time() - start_time
            print(f"Solution found! Explored states: {explored_states}")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            return current_state.path, explored_states, elapsed_time
        
        # Generates all valid moves
        valid_moves = get_valid_moves(current_state)
        
        # For each valid move, generates a new state and adds it to the queue
        for move in valid_moves:
            new_state = apply_move(current_state, move)
            new_state_hash = hash(new_state)
            
            # Checks if the state has already been visited
            if new_state_hash not in visited:
                h_value = heuristic_score_potential(new_state, target_score)
                g_value = new_state.score
                f_value = h_value - g_value  # We minimize f = h - g
                
                heapq.heappush(priority_queue, (f_value, counter, new_state))
                counter += 1
                visited.add(new_state_hash)
    
    # If it exited the loop, it did not find a solution or exceeded the time limit
    elapsed_time = time.time() - start_time
    if time.time() - start_time >= time_limit:
        print(f"Time limit exceeded! Explored states: {explored_states}")
    else:
        print(f"Solution not found! Explored states: {explored_states}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    return None, explored_states, elapsed_time

def weighted_a_star(initial_state, weight=1.2, target_score=500, time_limit=30):
    """
    Implements the Weighted A* algorithm.
    This algorithm gives more weight to the heuristic, speeding up the search,
    but potentially sacrificing the optimality of the solution.
    
    Args:
        initial_state (GameState): The initial game state.
        weight (float, optional): The weight given to the heuristic (w > 1).
        target_score (int, optional): The target score to consider a state as a goal.
        time_limit (int, optional): Time limit in seconds for the search.
        
    Returns:
        tuple: (path_found, explored_states, elapsed_time)
            - path_found is a list of moves or None if no solution is found
            - explored_states is the number of states explored
            - elapsed_time is the elapsed time in seconds
    """
    print(f"Starting Weighted A* Search with weight {weight}...")
    start_time = time.time()
    
    # Priority queue ordered by the function f(n) = g(n) + w*h(n)
    # g(n) is the cost so far (represented by the score)
    # h(n) is the heuristic (estimate of the remaining cost)
    # w is the weight given to the heuristic
    # Format: (f_value, counter, state)
    
    initial_h = heuristic_score_potential(initial_state, target_score)
    initial_g = initial_state.score
    initial_f = weight * initial_h - initial_g  # We minimize f = w*h - g
    
    priority_queue = [(initial_f, 0, initial_state)]
    heapq.heapify(priority_queue)
    
    # Counter to break ties between states with the same f value
    counter = 1
    
    # Set of already visited states to avoid cycles
    visited = set()
    visited.add(hash(initial_state))
    
    # Counter of explored states
    explored_states = 0
    
    while priority_queue and time.time() - start_time < time_limit:
        # Removes the state with the lowest f value from the queue
        _, _, current_state = heapq.heappop(priority_queue)
        explored_states += 1
        
        # Checks if it's a goal state
        if is_goal_state(current_state, target_score):
            elapsed_time = time.time() - start_time
            print(f"Solution found! Explored states: {explored_states}")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            return current_state.path, explored_states, elapsed_time
        
        # Generates all valid moves
        valid_moves = get_valid_moves(current_state)
        
        # For each valid move, generates a new state and adds it to the queue
        for move in valid_moves:
            new_state = apply_move(current_state, move)
            new_state_hash = hash(new_state)
            
            # Checks if the state has already been visited
            if new_state_hash not in visited:
                h_value = heuristic_score_potential(new_state, target_score)
                g_value = new_state.score
                f_value = weight * h_value - g_value  # We minimize f = w*h - g
                
                heapq.heappush(priority_queue, (f_value, counter, new_state))
                counter += 1
                visited.add(new_state_hash)
    
    # If it exited the loop, it did not find a solution or exceeded the time limit
    elapsed_time = time.time() - start_time
    if time.time() - start_time >= time_limit:
        print(f"Time limit exceeded! Explored states: {explored_states}")
    else:
        print(f"Solution not found! Explored states: {explored_states}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    return None, explored_states, elapsed_time

# Function to compare all algorithms on the same problem
def compare_algorithms(initial_state, target_score=500, time_limit=30):
    """
    Compares the performance of all implemented algorithms on the same problem.
    
    Args:
        initial_state (GameState): The initial game state.
        target_score (int, optional): The target score to consider a state as a goal.
        time_limit (int, optional): Time limit in seconds for each algorithm.
    
    Returns:
        dict: A dictionary with the results of each algorithm.
    """
    results = {}
    
    print("\n" + "="*50)
    print("ALGORITHM COMPARISON")
    print("="*50 + "\n")
    
    # BFS
    print("\n" + "-"*50)
    path_bfs, explored_bfs, time_bfs = bfs(initial_state, target_score, time_limit)
    results['BFS'] = {
        'path': path_bfs,
        'path_length': len(path_bfs) if path_bfs else None,
        'explored_states': explored_bfs,
        'time': time_bfs
    }
    
    # DFS
    print("\n" + "-"*50)
    path_dfs, explored_dfs, time_dfs = dfs(initial_state, target_score, time_limit)
    results['DFS'] = {
        'path': path_dfs,
        'path_length': len(path_dfs) if path_dfs else None,
        'explored_states': explored_dfs,
        'time': time_dfs
    }
    
    # Uniform Cost
    print("\n" + "-"*50)
    path_ucs, explored_ucs, time_ucs = uniform_cost_search(initial_state, target_score, time_limit)
    results['Uniform Cost'] = {
        'path': path_ucs,
        'path_length': len(path_ucs) if path_ucs else None,
        'explored_states': explored_ucs,
        'time': time_ucs
    }
    
    # Depth Limited
    print("\n" + "-"*50)
    depth_limit = 10
    path_dls, explored_dls, time_dls = depth_limited_search(initial_state, depth_limit, target_score, time_limit)
    results['Depth Limited'] = {
        'path': path_dls,
        'path_length': len(path_dls) if path_dls else None,
        'explored_states': explored_dls,
        'time': time_dls
    }
    
    # Iterative Deepening
    print("\n" + "-"*50)
    path_ids, explored_ids, time_ids = iterative_deepening(initial_state, 20, target_score, time_limit)
    results['Iterative Deepening'] = {
        'path': path_ids,
        'path_length': len(path_ids) if path_ids else None,
        'explored_states': explored_ids,
        'time': time_ids
    }
    
    # Greedy Search
    print("\n" + "-"*50)
    path_greedy, explored_greedy, time_greedy = greedy_search(initial_state, target_score, time_limit)
    results['Greedy Search'] = {
        'path': path_greedy,
        'path_length': len(path_greedy) if path_greedy else None,
        'explored_states': explored_greedy,
        'time': time_greedy
    }
    
    # A* Search
    print("\n" + "-"*50)
    path_astar, explored_astar, time_astar = a_star_search(initial_state, target_score, time_limit)
    results['A* Search'] = {
        'path': path_astar,
        'path_length': len(path_astar) if path_astar else None,
        'explored_states': explored_astar,
        'time': time_astar
    }
    
    # Weighted A* Search
    print("\n" + "-"*50)
    path_wastar, explored_wastar, time_wastar = weighted_a_star(initial_state, 1.5, target_score, time_limit)
    results['Weighted A* Search'] = {
        'path': path_wastar,
        'path_length': len(path_wastar) if path_wastar else None,
        'explored_states': explored_wastar,
        'time': time_wastar
    }
    
    # Prints a summary of the results
    print("\n" + "="*50)
    print("RESULTS SUMMARY")
    print("="*50)
    
    print(f"{'Algorithm':<20} {'Found solution':<20} {'Path length':<20} {'Explored states':<20} {'Time (s)':<15}")
    print("-"*95)
    
    for algo, result in results.items():
        found = "Yes" if result['path'] else "No"
        path_length = result['path_length'] if result['path_length'] else "-"
        print(f"{algo:<20} {found:<20} {path_length:<20} {result['explored_states']:<20} {result['time']:.2f}")
    
    return results

# Helper functions for integration with the main game

def get_ai_move(game, algorithm='bfs', target_score=500, time_limit=10):
    """
    Gets the next recommended move from the chosen AI algorithm.
    
    Args:
        game (WoodBlockPuzzle): The current game instance.
        algorithm (str, optional): The algorithm to use (bfs, dfs, ucs, dls, ids, greedy, astar, wastar).
        target_score (int, optional): The target score for the search.
        time_limit (int, optional): Time limit in seconds for the search.
        
    Returns:
        move: The recommended move or None if no solution is found.
    """
    # Creates the initial state from the current game
    initial_state = GameState(game.board, game.current_piece, game.score)
    
    # Executes the chosen algorithm
    if algorithm.lower() == 'bfs':
        path, _, _ = bfs(initial_state, target_score, time_limit)
    elif algorithm.lower() == 'dfs':
        path, _, _ = dfs(initial_state, target_score, time_limit)
    elif algorithm.lower() == 'ucs':
        path, _, _ = uniform_cost_search(initial_state, target_score, time_limit)
    elif algorithm.lower() == 'dls':
        path, _, _ = depth_limited_search(initial_state, 10, target_score, time_limit)
    elif algorithm.lower() == 'ids':
        path, _, _ = iterative_deepening(initial_state, 20, target_score, time_limit)
    elif algorithm.lower() == 'greedy':
        path, _, _ = greedy_search(initial_state, target_score, time_limit)
    elif algorithm.lower() == 'astar':
        path, _, _ = a_star_search(initial_state, target_score, time_limit)
    elif algorithm.lower() == 'wastar':
        path, _, _ = weighted_a_star(initial_state, 1.5, target_score, time_limit)
    else:
        # Algorithm not recognized, uses BFS as default
        print(f"Algorithm '{algorithm}' not recognized. Using BFS as default.")
        path, _, _ = bfs(initial_state, target_score, time_limit)
    
    # If a path was found, returns the first move
    if path and len(path) > 0:
        return path[0]
    
    # No solution found
    return None

def play_with_ai(game, algorithm='bfs', target_score=500, time_limit=10):
    """
    Plays a game automatically using the chosen AI algorithm.
    
    Args:
        game (WoodBlockPuzzle): The current game instance.
        algorithm (str, optional): The algorithm to use (bfs, dfs, ucs, dls, ids, greedy, astar, wastar).
        target_score (int, optional): The target score for the search.
        time_limit (int, optional): Time limit in seconds for each move.
        
    Returns:
        int: The final score obtained.
    """
    print(f"Playing automatically with algorithm {algorithm.upper()}...")
    print(f"Board size: {game.board_size}x{game.board_size}")
    print(f"Difficulty: {['Easy', 'Medium', 'Hard', 'Expert'][game.difficulty-1]}")
    print(f"Target score: {target_score}")
    print("Press 'q' at any time to return to the main menu.")
    
    max_moves = 100  # Move limit to avoid infinite loops
    moves_count = 0
    
    while game.score > 0 and moves_count < max_moves:
        # Shows the current game state
        game.display_board()
        print("Current Piece:")
        for row in game.current_piece:
            print(" ".join("#" if cell == 1 else " " for cell in row))
        
        # Gets the next move from the AI
        move = get_ai_move(game, algorithm, target_score, time_limit)
        
        if move is None:
            print("The AI could not find a valid move.")
            break
        
        # Applies the move
        if move == 'R':
            print("The AI decided to request a new piece.")
            game.get_new_piece()
        else:
            x, y = move
            print(f"The AI decided to place the piece at position ({x}, {y}).")
            if game.place_piece(x, y):
                game.check_full_lines_and_columns()
            else:
                print("Invalid move! Something went wrong.")
                break
        
        moves_count += 1
        
        # Pause for visualization with option to quit
        user_input = input("Press Enter to continue, or 'q' to quit: ").strip().lower()
        if user_input == 'q':
            print("Returning to main menu...")
            return game.score
    
    # Shows the final result
    game.display_board()
    print(f"Game ended after {moves_count} moves.")
    print(f"Final score: {game.score}")
    
    return game.score
