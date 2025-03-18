def update_price(menu, k):
    for i in menu:
        menu[i] += k
    return menu

menu = {"coffee":60, "croissant":120, "donut":100, "burger":400}
update_price(menu, 10)
print(sorted(list(menu.items())))
update_price(menu, 20)
print(sorted(list(menu.items())))