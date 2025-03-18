def calculator(a, b, c):
    minimo = min(a, b, c)
    maximo = max(a, b, c)
    soma = a + b + c
    # tem de ser formatada com f"" senão retorna tuplos com parentesis
    return f"{maximo} {minimo} {soma}"

# print(calculator(45, 12, 36))
# print(calculator(-900, 245, 1034))
# print(calculator(2, 2, 1))
# print(calculator(-3, -3, -3))