# [IP093] The Mysteries of Cellular Automata
# Example skeleton code for student
# (exemplifying the usage of global variables)

# read the input and change the following global variables
# - r: integer rule
# - k: number of iterations
# - line: the initial generation
def read():
    global r, k, line
    r, k = map(int, input().split())
    line = input()

# return a list of the 8 bits of rule r
def rule_to_8bits(r):
    r_8bits = [0] * 8
    for i in range(8):
        r_8bits[i] = r % 2
        r = r // 2
    return r_8bits

# return the number that represented a triplet (string of 3 chars)
def str_to_number(triplet):
    mapping = {'.': '0', '#': '1'}
    binary_str = ''
    for char in triplet:
        binary_str += mapping[char]
    return int(binary_str, 2)


# return a new character (# or .) according to the current triplet
# - rules: the set of rules as a list of 8 bits
# - triplet: a string with 3 chars - LEFT CENTER RIGHT
def calculate(rule, triplet):    
    if rule[str_to_number(triplet)] == 1: return "#"
    return '.'

# generate and return a new line:
# - rules: the set of rules as a list of 8 bits
# - line: the current line from which to generate the next one
def create(rule, line):
    # Add sentinels 
    extended_line = '.' + line + '.'
    new_line = ''
    
    # Calculate the new line
    for i in range(1, len(extended_line) - 1):
        triplet = extended_line[i-1:i+2]
        new_line += calculate(rule, triplet)
    return new_line

# simulate the game
# cycle trough the number of generations and for each one:
# - create the new generation (calling create)
# - update and print the current line
def simulate():
    global r, line
    rules = rule_to_8bits(r)
    for i in range(k):
        line = create(rules, line)
        print(line) 
    
# Main code: read the input and the simulate the automaton
read()

# print(f'{r=}, {k=}, {line=}')

# print(f'{rule_to_8bits(30)=}')
# print(f'{rule_to_8bits(128)=}')
# print(f'{rule_to_8bits(42)=}')

# print(f'{str_to_number("...")=}')
# print(f'{str_to_number("..#")=}')
# print(f'{str_to_number(".#.")=}')
# print(f'{str_to_number(".##")=}')
# print(f'{str_to_number("#..")=}')
# print(f'{str_to_number("#.#")=}')
# print(f'{str_to_number("##.")=}')
# print(f'{str_to_number("###")=}')

# rules = rule_to_8bits(30)
# print(f'{calculate(rules, "...")=}')
# print(f'{calculate(rules, "..#")=}')
# print(f'{calculate(rules, ".#.")=}')
# print(f'{calculate(rules, ".##")=}')
# print(f'{calculate(rules, "#..")=}')
# print(f'{calculate(rules, "#.#")=}')
# print(f'{calculate(rules, "##.")=}')
# print(f'{calculate(rules, "###")=}')

# rule = rule_to_8bits(30)
# line = "#..#.#..##......###...###"
# new_line = create(rule, line)
# print(new_line)

simulate()