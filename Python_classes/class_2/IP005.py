PI = 3.14159
D = float(input())
# area do circulo é r², quando dão o diametro, temos de dividir por 2
# para dar o raio, e aí elevar a 2

raio = (D/2)

circular_burguer_area = (PI*(raio**2))

square_area = circular_burguer_area

A = round((square_area**0.5), ndigits=3)

print(A)

# para calculo com raizes, raiz²(a) = a^(1/2); raiz³(a) = a^(1/3);...
