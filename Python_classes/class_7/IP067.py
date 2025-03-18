def highest_items(menu):
    max_price = max(menu.values()) #estabelecer o valor maximo para poder comparar
    highest = [] #lista dos produtos mais caros
    for item, price in menu.items(): #i.items cria lista de tuplos (item,price)
        if price == max_price:
            highest.append(item)
    return highest


menu = {"donut":100, "burger":400, "water":50, "pizza":400, "juice":150}
print(sorted(highest_items(menu)))

