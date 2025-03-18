def word_types(lst):
    count_lower = 0
    count_upper = 0
    count_other = 0
    for word in lst:
        if word.islower():
            count_lower += 1
        elif word.isupper():
            count_upper += 1
        else:
            count_other += 1
    return (count_lower, count_upper, count_other)


print(word_types(["Winter","IS","coming","WALL","CASTLE"]))
print(word_types(["stark","Lannister","TaRgArYeN", "ARRYN","tully"]))
print(word_types(["Robb", "Sansa", "Arya", "Bran", "Rickon", "Jon"]))