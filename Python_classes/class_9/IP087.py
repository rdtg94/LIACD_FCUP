def weekends(n, planets_list):
    if n == 0:
        return [[]]
    else:
        smaller_sequences = weekends(n - 1, planets_list)
        sequences = []
        for seq in smaller_sequences:
            for planet in planets_list:
                new_seq = seq + [planet]
                sequences.append(new_seq)
        return sequences


output = weekends(2, ["earth", "neptune"])
print(sorted(output))

print()

output = weekends(3, ["earth", "mars", "saturn"])
print("output is of type", type(output))
print("output has size:", len(output))
for x in sorted(output):
    print(x)