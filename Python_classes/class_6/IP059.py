def sort_strings(lst):
    def sort_key(x):
        return -len(x), x
    lst.sort(key=sort_key)


lst1 = ["forty","two","is","the","meaning","of","life"]
sort_strings(lst1)
print(lst1)
lst2 = ["to","be","or","not","to","be","that","is","the","question"]
sort_strings(lst2)
print(lst2)