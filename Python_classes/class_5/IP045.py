def substring(needle, haystack):
    # criar indice para iterar
    n_idx = 0 
    h_idx = 0

    while n_idx < len(needle) and h_idx < len(haystack): # corre ate terminar needle e haystack
        if needle[n_idx] == haystack[h_idx]:
            n_idx += 1 # se o caracter em needle for igual ao caracter em haystack, avança para o proximo caracter de needle
        h_idx += 1  # avança sempre 1 caracter em haystack

    # quando needle termina, significa que todos os caracteres foram encontrados em ordem
    return n_idx == len(needle)

print(substring("omg", "oh my god"))
print(substring("abc", "abracadabra"))
print(substring("my", "me, myself and irene"))
print(substring("lol", "lllllooooo"))
print(substring("no", "yes"))