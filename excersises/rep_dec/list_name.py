def name_list(n):
    n_list = []
    for _ in range(50):
        n_list.append(n)
    return n_list
user_name = str(input("Name: "))
print(name_list(user_name))