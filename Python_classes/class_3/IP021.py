num = int(input())

sum_of_digits = 0

for digit in str(num):
    sum_of_digits = sum_of_digits + int(digit)

print(sum_of_digits)