def remove_all(word, ch):
    final_word = ""
    for i in word:
        if i != ch:
            final_word = final_word + i
    return final_word
        
print(remove_all("suspect", "s"))
print(remove_all("metallica", "l"))
print(remove_all("abracadabra", "a"))
