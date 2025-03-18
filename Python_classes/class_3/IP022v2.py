num = int(input())
# lista para armazenar divisores proprios
divisores_proprios = []

"""analizar os numeros de 1 até ao numero que queremos, excluindo o proprio numero
senão irá somar 1 nos divisores proprios e nunca dará numero perfeito"""
for i in range(1, num):
    if num % i == 0:
        divisores_proprios.append(i)   #append adiciona o valor de i à lista


soma_divisores = sum(divisores_proprios)

if soma_divisores == num:   
    print(f"{num} is a perfect number")
    
    # ' ' vai crear um espaço
    # .join vai adicionar algo ao ' ' anterior
    # mao p vai mapear cada elemento da lista
    # str converte os numeros para string
    print(f"Factors: {' '.join(map(str, sorted(divisores_proprios, reverse=True)))}")
else:
    print(f"{num} is not a perfect number")