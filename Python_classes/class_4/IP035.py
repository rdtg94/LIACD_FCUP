import math
def digits_average(n):
    # Se o número tiver apenas um dígito, devolve-o
    if n < 10:
        return n
    
    # Converte o número numa lista de dígitos
    # Exemplo: 158 -> [1,5,8]
    digits = [int(d) for d in str(n)]
    
    # Calcula as médias entre dígitos adjacentes
    averages = []
    for i in range(len(digits)-1):
        # Calcula a média entre cada par de dígitos
        # Por exemplo: para 158
        # Primeiro par (1,5): (1+5)/2 = 3
        # Segundo par (5,8): (5+8)/2 = 6.5
        avg = (digits[i] + digits[i+1]) / 2
        
        # Arredonda para o inteiro mais próximo
        # Usa int(avg + 0.5) para arredondar corretamente
        # Por exemplo: 6.5 + 0.5 = 7, então int(7) = 7
        averages.append(int(avg + 0.5))
    
    # Converte a lista de médias num único número
    # Por exemplo: [3,7] -> 37
    next_n = int(''.join(map(str, averages)))
    
    return digits_average(next_n)

print(digits_average(158))  
print(digits_average(9534))
print(digits_average(9062))