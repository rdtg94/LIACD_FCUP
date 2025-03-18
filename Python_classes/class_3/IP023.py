n = int(input())

for i in range(1, n + 1):
    # Imprime espaços antes dos numeros
    for j in range(n - i):
        print(" ", end="")
    
    # IMprime numeros ordem crescente
    # de 1 a i + 1
    for j in range(1, i + 1):
        print(j, end="")
    
    # Imprime numeros ordem decrescente
    # de i - 1  para não repetir valor inicial da seq
    # 0 indica a paragem
    # -1 indica ordem reversa
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    # Imprime prox linha
    print()