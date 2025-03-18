def binary(a, b, k):
    result = []

    def generate_binary(current_string, length, ones_count):
        """
        Helper function to recursively generate binary strings.

        Args:
            current_string: The binary string being built.
            length: The desired length of the binary string.
            ones_count: The number of 1's in the current string.
        """
        if len(current_string) == length:
            if ones_count <= k:
                result.append(current_string)
            return

        # Add '0' and recurse (no change in ones_count)
        generate_binary(current_string + "0", length, ones_count)

        # Add '1' and recurse (increment ones_count if within limit)
        if ones_count < k:
            generate_binary(current_string + "1", length, ones_count + 1)

    for length in range(a, b + 1):
        generate_binary("", length, 0)

    return result

output = binary(1, 2, 3)
print(sorted(output))

print()

output = binary(2, 4, 2)
print("output is of type", type(output))
print("output has size:", len(output))
for x in sorted(output):
    print(x)
