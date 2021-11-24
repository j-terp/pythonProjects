import random
def randomlist(length):
    numberlist = []
    for _ in range(int(length)):
        numberlist.append(random.randrange(0,100))
    return numberlist
print(randomlist(7))