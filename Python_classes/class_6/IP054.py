def middle(lst):
    # ordenar a lista
    sorted_list = sorted(lst)
    # declarar o len da sorted list
    n = len(sorted_list)
    # se n div 2 é impar
    if n % 2 != 0:
        # devolver uma lista com a posição de n div inteira por 2
        return [sorted_list[n // 2]] #dá o elemento do meio
    else:
        # retorna o valor antes do meio e depois do meio
        return sorted_list[(n // 2) - 1 : (n // 2) + 1]

print(middle(['StAndrew','StJames','StJohn','StPeter','StPhilip']))
print(middle([1,2,3,4,5,6,7,8]))
print(middle([1,9,3,5,7]))
print(middle([8,4,6,2,12,10]))