# tentei fazer com valores mas não dá para usar com strings,
# então usar enumerar para trablhar com as posições

def odd_even(tup):
    odd_positions = []
    even_positions = []
    
    for index, value in enumerate(tup):
        if index % 2 != 0:
            even_positions.append(value)
        else:
            odd_positions.append(value)
    
    final_tup = tuple(odd_positions + even_positions)
    return final_tup

print(odd_even((1, 2, 3, 4, 5, 6, 7, 8, 9)))  # Saída: (1, 3, 5, 7, 9, 2, 4, 6, 8)
print(odd_even((1, 2, 3, 4, 5, 6, 7, 8)))     # Saída: (1, 3, 5, 7, 2, 4, 6, 8)
print(odd_even(("a", "b", "c", "d", "e")))    # Saída: ('a', 'c', 'e', 'b', 'd')
print(odd_even(("hello", 42, "oh no", 2.0, 14)))  # Saída: ('hello', 'oh no', 14, 42, 2.0)
