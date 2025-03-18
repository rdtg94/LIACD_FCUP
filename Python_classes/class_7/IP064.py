def rename(menu, old_name, new_name):
    if old_name in menu:
        menu[new_name] = menu.pop(old_name)
    return menu


menu = {"coffee":60, "croissant":120, "donut":100, "burger":400}
rename(menu, "croissant", "frenchy")
print(sorted(list(menu.items())))
rename(menu, "donut", "roundy")
print(sorted(list(menu.items())))
rename(menu, "icecream", "icy")
print(sorted(list(menu.items())))
