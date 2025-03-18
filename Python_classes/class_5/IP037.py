'''Write a function palindrome(word) that given a string word constituted 
by lower case letters, returns True if the word is a palindrome and
False if it isn't.'''

def palindrome(word):
    word = str(word)
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("wow"))
print(palindrome("racecar"))
print(palindrome("python"))
print(palindrome("abcdba"))
print(palindrome("UAU"))