import math

a = float(input())
b = float(input())
c = float(input())

# Calcular discriminante
D = b**2 - 4*a*c

if D > 0:
    # 2 raízes reais distintas
    R1 = (-b + math.sqrt(D)) / (2*a)
    R2 = (-b - math.sqrt(D)) / (2*a)
    print(f"R1 = {round(R1, ndigits=2)}")
    print(f"R2 = {round(R2, ndigits=2)}")
elif D == 0:
    # 1 raiz real
    R = -b / (2*a)
    print(f"R = {round(R, ndigits=2)}")
else:
    # 2 raízes complexas
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print(f"R1 = {round(real_part, ndigits=2)} + {round(imaginary_part, ndigits=2)}i")
    print(f"R2 = {round(real_part, ndigits=2)} - {round(imaginary_part, ndigits=2)}i")