D = float(input()) # KM
H = int(input()) # hours
M = int(input()) # minutes

# Para calcular o numero máximo de horas:
# converter o numero de horas (do input) para minutos (multiplicando horas por 60)
# somar estes minutos com os minutos do input
# dividir por 60 para converter minutos para hora
total_hours = ((H*60) + M) / 60

V = (D/total_hours)

print(round(V, ndigits=None))
