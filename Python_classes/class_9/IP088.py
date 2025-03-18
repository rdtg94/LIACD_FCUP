def quantities(coins):
    def find_sums(index, current_sum, result):
        if index == len(coins):
            result.add(current_sum)
            return
        find_sums(index + 1, current_sum, result)
        find_sums(index + 1, current_sum + coins[index], result)

    result = set()
    find_sums(0, 0, result)
    return result


output = quantities([10, 50, 100])
print(sorted(output))

print()

output = quantities([1, 1, 5, 5, 12])
print("output is of type", type(output))
print("output has size:", len(output))
for x in sorted(output): print(x)