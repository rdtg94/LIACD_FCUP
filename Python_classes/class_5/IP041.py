def extremes(words):
    # converte cada palavra no seu comprimento e guarda numa lista
    words = [len(word) for word in words] 
    return min(words), max(words) # retorna o minimo e o maximo da lista

print(extremes( ("Alberto", "Francesco", "Miriam", "Pedro", "Tadeu") ))
print(extremes( ("c/c++", "java", "python", "prolog", "haskell",) ))
print(extremes( ("portugal", "spain", "italy") ))