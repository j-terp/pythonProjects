from random_numberlist import randomlist
import time
try_list = []
try_sum = 0
user_loops = int(input("Loops: "))
for _ in range(user_loops):
    win = False
    tries = 1
    while win == False:
        lotto_list = randomlist(7)
        win_number = randomlist(1)[0]
        for number in lotto_list:
            if number == win_number:
                win = True
                break
        if win == True:
            print("VINST:   " + str(tries))
            try_list.append(str(tries))
            try_sum += tries
        else:
            print("Förlust: " + str(tries))
            tries += 1
        time.sleep(1/900)

average = try_sum * 100 // len(try_list) / 100
print("\nLista över försök:\n" + ", ".join(try_list))
print("\nAverage: " + str(average))