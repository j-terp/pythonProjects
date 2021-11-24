def has_equal_ends(list_a, list_b):
    if list_a[-1] == list_b[-1]:
        return True
    else:
        return False
list_a = ["A", "would", "be", "True"]
list_b = ["B", "is", "False"]
print(has_equal_ends(list_a, list_b))