""" def occurrences(lst, x):
    new_list = []
    for i in lst:
        if x == i:
            new_list.append(lst.index(i))  #dá sempre a primeira ocorrencia de i
    return new_list """

def occurrences(lst, x):
    new_list = []
    for index, value in enumerate(lst):
        if x == value:
            new_list.append(index)
    return new_list


lst = ["cola","cereal","donut","cola","cola","donut","cola"]
print(occurrences(lst, "cola"))
print(occurrences(lst, "cereal"))
print(occurrences(lst, "donut"))
print(occurrences(lst, "water"))