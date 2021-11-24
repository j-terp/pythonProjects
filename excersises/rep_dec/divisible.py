def divisible_by_five(number):
    return int(number) % 5 == 0
user_input = input("Number: ")
print(divisible_by_five(user_input))

def divisible_by(number,divisor):
    return int(number) % int(divisor) == 0
user_number = input("Number: ")
user_divisor = input("Divisor: ")
print(divisible_by(user_number,user_divisor))