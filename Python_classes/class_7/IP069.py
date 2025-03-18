def remove(x, menu):
    items_to_remove = set()
    for i in menu:
        if i[0] == x:
            items_to_remove.add(i)
            
    for item in items_to_remove:
        menu.remove(item)


menu = {"banana", "juice", "burger", "coffee", "tea"}
remove("b", menu)
print(type(menu))
print(sorted(list(menu)))