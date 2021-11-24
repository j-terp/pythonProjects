def is_palindrom(user_string):
    if user_string == user_string[::-1]:
        return True
    else:
        False
print(is_palindrom("boom"))