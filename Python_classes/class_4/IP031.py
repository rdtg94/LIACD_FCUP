def factorial(n):
    if n == 0: 
        return 1
    else:
        return n * factorial(n-1)  

def combination(n, k):
    if n < k:
        return "NA"
    else:
        return (factorial(n)) // (factorial(k) * factorial(n - k))

print(combination(6, 2))
print(combination(15, 9))
print(combination(100, 4))
print(combination(3, 9))
print(combination(4, 10))