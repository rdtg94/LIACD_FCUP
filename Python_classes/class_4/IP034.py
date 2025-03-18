def collatz(n):
    if n == 1:
        return "1"
    elif n % 2 == 0:
        return f"{n}, {collatz(n // 2)}"
    else:
        return f"{n}, {collatz(3 * n + 1)}"

print(collatz(1))
print(collatz(3))
print(collatz(12))