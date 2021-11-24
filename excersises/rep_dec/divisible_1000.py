from divisible import divisible_by
a = 0
for _ in range(1000):
    a += 1
    if divisible_by(a,7) == True and divisible_by(a,2) == False:
        print(a)