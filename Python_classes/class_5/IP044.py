def swap(word):
    new_word = ""
    i = 0
    while i < len(word) - 1:
        new_word = new_word + word[i + 1]
        new_word = new_word + word[i]
        i = i + 2
    if len(word) % 2 != 0:
        new_word = new_word + word[-1]
    return new_word

print(swap("python"))
print(swap("hello"))
print(swap("programming"))