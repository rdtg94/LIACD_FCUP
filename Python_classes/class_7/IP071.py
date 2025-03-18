def frequency(ingredients):
    ingredient_count = {}
    for i in ingredients:
        if i in ingredient_count:
            ingredient_count[i] += 1
        else:
            ingredient_count[i] = 1
    return ingredient_count

ingredients = ["burger", "burger", "tea", "water", "burger", "tea", "juice"]
fr = frequency(ingredients)
print(sorted(list(fr.items())))