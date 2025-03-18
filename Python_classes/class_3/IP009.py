## Write a program that, given a number n, prints its absolute value

num = float(input())

if num >= 0:
    print(num)
else:
    num = num * (-1)
    print(num)