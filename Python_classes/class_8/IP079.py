def csv_change(text, a, b):
    text = text.split(sep=",")
    #print(text)
    index_a = a - 1
    index_b = b - 1
    temp = text[index_a]
    text[index_a] = text[index_b]
    text[index_b] = temp
    new_text = ','.join(text)
    return new_text

print(csv_change("attack,the,starks,dawn,at", 4, 5))
print(csv_change("reason,is,more,powerful,than,love", 1, 6))
print(csv_change("That's, what, I, do, I, drink, and, I, know, things", 6, 4))