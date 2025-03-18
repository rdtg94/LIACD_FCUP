def super_swap(menu):
    reversed_menu = {}
    for item, price in menu.items():
        if price in reversed_menu:
            reversed_menu[price].add(item)
        else:
            reversed_menu[price] = {item}
    return reversed_menu
