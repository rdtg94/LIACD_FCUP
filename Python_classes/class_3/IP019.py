r1 = float(input())
x1 = float(input())
y1 = float(input())
r2 = float(input())
x2 = float(input())
y2 = float(input())

# é necessario calcular distancia entre centros
# usar o teorema de pitagoras
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

if distancia == r1 + r2 or distancia == r1 - r2 or distancia == r2 - r1:
    print("The circles are tangent.")
else:
    print("The circles are not tangent.")