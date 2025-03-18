def compose(f,g):
    h = {}
    for value in f:   #itera as keys em f
        #print(value)
        #print(f[value])
        if f[value] in g: # se o value for uma key em g
            h[value] = g[f[value]]
    
    return h




f = {"coffee":"cafe", "milk":"leite", "tea":"cha", "juice":"sumo"}
g = {"leite":"leche", "sumo":"zumo"}
h = compose(f,g)
print(sorted(list(h.items())))