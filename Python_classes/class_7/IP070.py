def possible_sums(coins):
    result = set()
    coins = list(coins)

    for coin1 in coins:
        result.add(coin1)
    

    for coin1 in coins:
        for coin2 in coins:
            soma = coin1 + coin2
            result.add(soma)
    

    for coin1 in coins:
        for coin2 in coins:
            for coin3 in coins:
                soma = coin1 + coin2 + coin3
                result.add(soma)
    
    return result

sums = possible_sums({1,2,10})
print(type(sums))
print(sorted(list(sums)))