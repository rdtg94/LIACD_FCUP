def price_diversity(menu):
    prices = []
    for i in menu.values():
        prices.append(i)
    return set(prices)

menu = {"donut":100, "burger":400, "soda":150, "pizza":400, "juice":150}
prices = price_diversity(menu)
print(type(prices))
print(sorted(list(prices)))