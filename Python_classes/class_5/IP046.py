def evolve(initial, n):
    current = initial
    for i in range(n + 1):
        print(''.join(current))
        prox_bloco = ''
        for i in current:
            if i == 'A':
                prox_bloco += 'AB'
            else:
                prox_bloco += 'A'
        current = prox_bloco

evolve("A", 4)
print("---------------")
evolve("ABBA", 3)
print("---------------")