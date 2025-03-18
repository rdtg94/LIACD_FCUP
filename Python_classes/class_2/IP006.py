D = int(input())  # int converte para inteiro

H = D*24
M = H*60
S = M*60

print(f"{D} days: {H} hours")
print(f"{D} days: {M} minutes") 
print(f"{D} days: {S} seconds")
# função f permite, durante o print, adicionar dentro de chavetas a variável que queremos chamar
