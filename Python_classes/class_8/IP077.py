def count_words(text):
    text = text.strip()
    text = text.lower()
    text = text.split(sep =  " ")
    # print(text)
    count = 0
    non_rep_words = []
    for word in text:
        if word == "":
            continue
        if word not in non_rep_words:
            non_rep_words.append(word)
            count += 1
        
    return count

"""
VERSÃO Otimizada:

def count_words(text):
    words = set(text.lower().split())
    return len(words)



"""
print(count_words("winter is coming"))
print(count_words("to be or not to be that is the question"))
print(count_words("Can you can a Can as a canner can can a Can"))

print(count_words("what  What  wHaT is love baby dont hurt me"))
print(count_words("  "))
print(count_words(" abc abC aBc aBC Abc AbC ABc ABC "))
print(count_words("Fuzzy Wuzzy was a bear Fuzzy Wuzzy had no hair Fuzzy Wuzzy wasnt fuzzy was he"))
print(count_words("You know New York you need New York you know you need unique New York"))
print(count_words("Which witch is which"))
print(count_words(" all    your    base    belong   to   us  "))