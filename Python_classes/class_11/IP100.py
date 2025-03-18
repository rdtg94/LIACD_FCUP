import random

def find_exit(connections, check_booth, seed):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Create a copy of connections to modify
    modified_connections = {}

    # Iterate through the booths and randomly decide whether to keep them
    for booth, instruction in connections.items():
        if random.random() >= 0.3:  # 70% chance to keep the booth
            modified_connections[booth] = instruction

    # Check if the specified booth is still available
    if check_booth in modified_connections:
        return modified_connections[check_booth]
    else:
        return "Compromised booth! Aborting connection."

connections = {
    "B1": "Go to the red door in the hallway and turn left.",
    "B2": "Head over to the back alley and find the hidden key.",
    "B3": "Find the elevator and press the secret button.",
    "B4": "Turn left at the second street and look for the green sign.",
    "B5": "Follow the alley until you see a blue dumpster, then turn right.",
    "B6": "Look for a door with a glowing symbol and open it.",
    "B7": "Enter the subway station, go down the stairs, and find the secret passage.",
    "B8": "Turn around and go through the abandoned building entrance.",
    "B9": "Find the underground tunnel entrance near the library.",
    "B10": "Go straight ahead, take the first right, and find the hidden hatch."
}

print(find_exit(connections, "B1", 42))
print(find_exit(connections, "B4", 42))
print(find_exit(connections, "B9", 123))
