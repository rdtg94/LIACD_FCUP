def unique(lst):
    resultado = []
    for i in lst:  # percorrer 1x para ...
        aparicoes = 0  # ... inicializar quantos vezes aparece na lista cada "i"
        for j in lst: #percorrer 2a vez para...
            if i == j: # se 1 elemento for igual a outro
                aparicoes += 1  # adicionar 1 aparição, se ele aparecer mais de 1x, será incrementado
        if aparicoes == 1: 
            resultado.append(i)
    return resultado



print(unique(["bart","lewis","bart", "martin", "bart", "nelson","martin"]))
print(unique(['a','b','c','d']))
print(unique([True, False, True, False]))
print(unique(['f', 'o', 'r', 't', 'y', 't', 'w', 'o']))