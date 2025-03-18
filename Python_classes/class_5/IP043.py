def search(tup, value):
    first_index = -1
    last_index = -1
    for i in range(len(tup)):
        if tup[i] == value:
            if first_index == -1:
                first_index = i
            last_index = i
    return (first_index, last_index)


print(search( (1,2,1,2,1), 1 ))
print(search( ("a","b","b","c"), "b" ))
print(search( ("a","b","b","c"), "c" ))
print(search( (True, True, True), False ))