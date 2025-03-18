def largest_sequence(num):
    num_str = str(num)
    max_count = 0
    current_count = 1

    for i in range(1, len(num_str)):
        if num_str[i] > num_str[i - 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1

    max_count = max(max_count, current_count)
    return max_count

print(largest_sequence(129643457))
print(largest_sequence(1213478911))
print(largest_sequence(123123412345)) 