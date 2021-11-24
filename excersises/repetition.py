def start(name,description,level):
    print("\n" + str(name), str(level), "\n" + str(description), "\n")
# ----- Start of Exercises -----
def exercise_1():
    start("Character Input", "input strings types int", "(I)")
    name = input("What's your name? ")
    age = int(input("How many years will you turn this year? "))
    wishes = int(input("How many wishes do you want? "))
    year100 = 2019 - age + 100
    for i in range(wishes):
        print("Congratulations", name + "! You will be 100 years old in the year", year100)

def exercise_2():
    start("Odd Or Even", "input if types int equality comparison numbers mod", "(I)")
    number = int(input("Give a number: "))
    if number % 4 == 0:
        print("It's a multiple of 4")
    elif number % 2 == 0:
        print("It's even")
    else:
        print("It's odd")
    num = int(input("Now, a number to divide: "))
    check = int(input("And the number to divide with: "))
    if num % check == 0:
        print("Divides evenly")
    else:
        print("Doesn't divide evenly")

def exercise_3():
    start("List Less Than Ten", "list numbers elements if conditional", "(II)")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for number in a:
        if number < 10:
            print(number)
            b.append(number)
    print(b)
    
def exercise_4():
    start("Divisors","","II")
    number = int(input("Input number: "))
    divisor = 0
    for i in range(number):
        divisor += 1
        remainder = number % divisor
        if remainder == 0:
            print(divisor)

def exercise_5():
    start("List Overlap","","II")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for number_a in a:
        for number_b in b:
            if number_a == number_b:
                print("Match: " + str(number_a))
                if number_a in c == False: #Not working
                    print("Not found: " + str(number_a))
                    c.append(number_a)
    print(c)

def exercise_6():
    start("6")

def exercise_7():
    start("7")

def exercise_8():
    start("8")

def exercise_9():
    start("9")

def exercise_10():
    start("10")

def exercise_11():
    start("11")

def exercise_12():
    start("12")

def exercise_13():
    start("13")

def exercise_14():
    start("14")

def exercise_15():
    start("15")

def exercise_16():
    start("16")

def exercise_17():
    start("17")

def exercise_18():
    start("18")

def exercise_19():
    start("19")

def exercise_20():
    start("20")

def exercise_21():
    start("21")

def exercise_22():
    start("22")

def exercise_23():
    start("23")

def exercise_24():
    start("24")

def exercise_25():
    start("25")

def exercise_26():
    start("26")

def exercise_27():
    start("27")

def exercise_28():
    start("28")

def exercise_29():
    start("29")

def exercise_30():
    start("30")

def exercise_31():
    start("31")

def exercise_32():
    start("32")

def exercise_33():
    start("33")

def exercise_34():
    start("34")

def exercise_35():
    start("35")

def exercise_36():
    start("36")

# ----- Executing Exercise -----
myExercises = {
    "1": exercise_1,
    "2": exercise_2,
    "3": exercise_3,
    "4": exercise_4,
    "5": exercise_5,
    "6": exercise_6,
    "7": exercise_7,
    "8": exercise_8,
    "9": exercise_9,
    "10": exercise_10,
    "11": exercise_11,
    "12": exercise_12,
    "13": exercise_13,
    "14": exercise_14,
    "15": exercise_15,
    "16": exercise_16,
    "17": exercise_17,
    "18": exercise_18,
    "19": exercise_19,
    "20": exercise_20,
    "21": exercise_21,
    "22": exercise_22,
    "23": exercise_23,
    "24": exercise_24,
    "25": exercise_25,
    "26": exercise_26,
    "27": exercise_27,
    "28": exercise_28,
    "29": exercise_29,
    "30": exercise_30,
    "31": exercise_31,
    "32": exercise_32,
    "33": exercise_33,
    "34": exercise_34,
    "35": exercise_35,
    "36": exercise_36,
}
def selection():
    number = input("What exercise shall be executed? ")
    executing_exercises(number)
    retry = str(input("Retry? ")).lower()
    if retry == "yes" or retry == "y":
        selection()
    else:
        print("Done")
def executing_exercises(name):
    myExercises.get(name, lambda: 'Invalid')()
selection()