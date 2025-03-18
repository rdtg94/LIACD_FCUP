def list_to_matrix(lst, r, c):
    matriz = []

    # variavel para acompanhar posição atual na lista
    indice = 0

    # loop para cada linha
    for i in range(r):
        linha = []
        # loop para cada coluna
        for j in range(c):
            # adicionar elemento à linha
            linha.append(lst[indice])
            # incrementar o índice para o próximo elemento
            indice += 1
        # adicionar a linha completa à matriz
        matriz.append(linha)

    return matriz

print(list_to_matrix([1,2,3,4,5,6,7,8,9], 3, 3))
print(list_to_matrix([9,8,7,6,5,4,3,2,1,0], 2, 5))