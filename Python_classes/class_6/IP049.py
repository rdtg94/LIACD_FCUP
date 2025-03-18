def fibonacci(a, b, n):
    lst = [a, b]
    for i in range(2, n):
        next_num = lst[i - 2] + lst[i - 1]
        lst.append(next_num)
    return lst

print(fibonacci(0,1,13))
print(fibonacci(2,4,10))
print(fibonacci(1,3,12))