num = int(input())

# Converter o número para uma string para facilitar iteração entre os dígitos
num_str = str(num)

# variaveis para fazer check da ordem
is_ascending = True
is_descending = True
is_equal = True # para verificar se forem iguais

# Vai percorrer a lista de numeros e comparar se o numero atual é menor do que o seguinte
# se for menor, não estará em ordem descendente - muda is_descending para False
# depois verifica se o numero atual é maior do que o seguinte,
# se for maior, não estará em ordem crescente - muda is_ascending para False
# no final, apenas ficará True a variavel para correta
for i in range(len(num_str) - 1): 
    # sem o -1 dá erro de index out of range, porque index começa em 0 e range(len) dá o num de caracteres (neste caso 4)
    if num_str[i] < num_str[i + 1]:
        is_descending = False
        is_equal = False
    elif num_str[i] > num_str[i + 1]:
        is_ascending = False
        is_equal = False
    else:
        is_ascending = False
        is_descending = False

# Determinar a ordem dos dígitos e imprimir a mensagem correspondente
if is_equal:
    print("The number is not ordered.")
elif is_ascending:
    print("The number is in ascending order.")
elif is_descending:
    print("The number is in descending order.")
else:
    print("The number is not ordered.")