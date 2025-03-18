def swap(menu):
    new_menu = {}
    for key in menu:
        value = menu[key]
        new_menu[value] = key
    return new_menu





menu1 = {"coffee":60, "croissant":120, "donut":100, "burger":400}
new_menu1 = swap(menu1)
print(sorted(list(new_menu1.items())))
menu2 = {"one":"um", "two":"dois", "three":"tres", "four":"quatro"}
new_menu2 = swap(menu2)
print(sorted(list(new_menu2.items())))