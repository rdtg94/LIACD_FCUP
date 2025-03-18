'''Write a function first_last(word) that given a string word returns
a tuple containing (a,b,c) where a is its first character,
b is its last character and 
c is the remainder of the word without the first and last characters.'''
def first_last(word):
    a = str(word[0])
    b = str(word[-1])
    c = str(word[1:-1])
    return a, b, c

print(first_last("python"))
print(first_last("oh"))
print(first_last("123456"))

