import string

def caesar_cipher(text, k):
    text = text.lower()
    result = ""
    for i in text:
        if i in string.ascii_lowercase:
            result += chr((ord(i) - ord('a') + k) % 26 + ord('a'))
        else:
            result += i
    return result


print(caesar_cipher("attack the starks", 10))
print(caesar_cipher("winteriscoming", 23))
print(caesar_cipher("tfkqbofpzljfkd", 3))