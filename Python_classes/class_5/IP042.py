def count(word, letters):
    sum = 0
    for i in word:
        if i in letters:
            sum += 1
    return sum

print(count("madame", "aeiou"))
print(count("1forty40two2", "0123456789"))
print(count("introduction to programming", "prt"))