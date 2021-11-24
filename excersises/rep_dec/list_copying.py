list_a = ["Hejsan", 23, True]
def copy_list(original):
    list_b = ["B"]
    for term in original:
        list_b.append(term)
    return list_b
print(copy_list(list_a))