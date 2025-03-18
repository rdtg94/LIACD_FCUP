def transform(lst, k):
    for i in range(len(lst)):
        lst[i] = lst[i] * k

lst = [1,2,3,4,5]
transform(lst, 2)
print(lst)
transform(lst, 5)
print(lst)