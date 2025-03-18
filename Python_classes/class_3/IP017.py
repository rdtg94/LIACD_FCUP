n = int(input())

for i in range(1, 101):
    # Verifica se o valor de i é divisível por n
    if i % n == 0:
        # Se i for 100 ou se o próximo múltiplo de n for maior que 100
        if i == 100 or (i + n) > 100:
            print(i)
        else:
            print(i, end=' ')