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
    
    # end faz com que print em vez de separar com linha nova
    # separe com espaço, nesta caso a sehuir aos :
    print(f"Factors:", end=" ")

    # este for vai iterar a lista de divisores proprios
    # sorted vai ordenar a lista por ordem crescente
    # como queremos ordem decrescente usamos reverse = True                            
    for divisor in sorted(divisores_proprios, reverse = True):
        print(divisor, end=" ") #entre cada numero queremos espaço
else:
    print(f"{num} is not a perfect number")