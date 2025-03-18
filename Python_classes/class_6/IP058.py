def pascal(n):
    row = [1]
    for k in range(1, n):
        next_number = row[-1] * (n - k) // k
        row.append(next_number)
    return row
    

print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
print(pascal(5))