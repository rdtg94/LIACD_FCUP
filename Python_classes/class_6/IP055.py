def matrix_to_list(m):
    new_list = []
    for linha in m: # itera sobre as listas dentro da lista
        for elemento in linha:  # itera sobre os valores dentro das listas
            new_list.append(elemento)
    return new_list

print(matrix_to_list([ [1,2,3], [4,5,6], [7,8,9] ]))
print(matrix_to_list([ [9,8,7,6,5], [4,3,2,1,0] ]))