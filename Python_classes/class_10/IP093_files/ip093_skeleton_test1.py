# Read the input and change the following global variables
def read():
    global r, k, line
    r, k = map(int, input().split())
    line = input()

# Return a list of the 8 bits of rule r
def rule_to_8bits(r):
    r_8bits = [0] * 8
    for i in range(8):
        r_8bits[i] = r % 2
        r = r // 2
    return r_8bits

# Return the number that represents a triplet (string of 3 chars)
def str_to_number(triplet):
    mapping = {'.': '0', '#': '1'}
    binary_str = ''.join(mapping[char] for char in triplet)
    return int(binary_str, 2)

# Return a new character (# or .) according to the current triplet
def calculate(rule, triplet):    
    return "#" if rule[str_to_number(triplet)] == 1 else '.'

# Generate and return a new line
def create(rule, line):
    # Add sentinels
    extended_line = '.' + line + '.'
    new_line = []  # Use a list for better performance
    
    # Calculate the new line
    for i in range(1, len(extended_line) - 1):
        triplet = extended_line[i-1:i+2]
        new_line.append(calculate(rule, triplet))
    
    return ''.join(new_line)  # Join the list into a string at the end

# Simulate the game
def simulate():
    global r, line
    rules = rule_to_8bits(r)
    
    for _ in range(k):
        # Surround the current line with '.' for output
        print(f".{line}.")
        line = create(rules, line)
    
    # Add a blank line at the end
    print()

# Main code: read the input and simulate the automaton
read()
simulate()
