def duplicate(tup):
    res = []   #append só funcioa com listas
    for i in tup:
        res.append(i) #adiciona o elemento i a lista res
        res.append(i) #adiciona o elemento i a lista res
    return tuple(res) # converte e retorna a lista res em tuplo

print(duplicate( (1,2,3) ))
print(duplicate( ("python","rocks") ))
print(duplicate( (1.0, True, 4, "a") ))