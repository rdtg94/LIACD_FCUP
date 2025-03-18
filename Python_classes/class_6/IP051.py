def rotate(lst, dir):
    # faz check de se a lista está vazia. Sem isto dá erro no pop()
    if not lst:
        return

    if dir == "right":
        last_element = lst.pop() # last elemento é retirado de lst e guardado em last_element 
        # pop() retira o ultimo por defeito, pop(x) - retira o elemento de index x
        lst.insert(0, last_element) # insert na posição 0 o last_element retirado da lst
    
    elif dir == "left":
        first_element = lst.pop(0) # retira o elemento de index 0 e guarda em first_element
        lst.append(first_element) # adiciona no fim de lst o first element retirado em cima


lst = ["pacifier", "teddy", "train", "block", "rabbit"]
rotate(lst, "right")
print(lst)
rotate(lst, "right")
print(lst)
rotate(lst, "left")
print(lst)
empty = []
rotate(empty, "left")
print(empty)