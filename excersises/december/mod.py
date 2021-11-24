def divisable(a,b):
    return a % b
def is_divisable(a,b):
    return divisable(a,b) == 0
"""number = int(input(""))
divisor = int(input(""))
print(is_divisable(number,divisor))"""

def evens(numbers):
    result = []
    for n in numbers:
        if is_divisable(n,2):
            result.append(n)
    return result
a = [17,5,2,4,6,7]
print(evens(a))