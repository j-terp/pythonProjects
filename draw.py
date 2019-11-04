print("Vad vill du rita?\n\nFigurer: Cirkel, Kvadrat, Stjärna\nMönster: Primtalscirkel\n")
choice = str.lower(input("> "))

import turtle
my_pencil = turtle.Turtle()
my_pencil.shape("turtle")
my_pencil.speed(0)
colours = [ "red","yellow","green","cyan","blue","magenta" ]

if choice == "cirkel":
    a = int(input("Ange stolek: "))
    my_pencil.penup()
    my_pencil.right(90)
    my_pencil.forward(a)
    my_pencil.left(90)
    my_pencil.pendown()
    my_pencil.circle(a)
elif choice == "kvadrat":
    a = int(input("Ange stolek: "))
    my_pencil.penup()
    for i in range(2):
        my_pencil.forward(a / 2)
        my_pencil.left(90)
    my_pencil.pendown()
    for i in range(4):
        my_pencil.forward(a)
        my_pencil.left(90)
elif choice == "stjärna":
    a = int(input("Ange stolek: "))
    x = int(input("Ange hur många uddar: "))
    y = 0.5 * x
    my_pencil.penup()
    my_pencil.left(90)
    my_pencil.forward(a / 2)
    my_pencil.pendown()
    if x <= 2:
        print("För få uddar i stjärnan")
    elif x % 2 == 1:
        my_pencil.right(180 - 90 / x)
        for i in range(x):
            my_pencil.forward(a)
            my_pencil.right(180 - 180 / x)
    elif y % 2 == 1:
        for i in range(2):
            my_pencil.right(180 - 90 / y)
            for i in range(int(y)):
                my_pencil.forward(a)
                my_pencil.right(180 - 180 / y)
            my_pencil.penup()
            my_pencil.right(90 / y)
            my_pencil.forward(a)
            my_pencil.pendown()
    else:
        my_pencil.right(180 - 90 / y)
        for i in range(x):
            my_pencil.forward(a)
            my_pencil.right(180 - 180 / y)
    
elif choice == "primtalscirkel":
    a = float(input("Ange stolek: "))
    x = float(input("Ange hur många grader: "))
    for i in range(360):
        my_pencil.color(colours[i % 6])
        my_pencil.circle(a)
        my_pencil.left(float(x))
elif choice == "fylldcirkel":
    a = float(input("Ange stolek: "))
    b = float(input("Ange minskning: "))
    c = float(input("Ange acceleration: "))
    x = float(input("Ange hur många grader: "))
    i = 0
    while a > 0:
        my_pencil.begin_fill()
        my_pencil.color(colours[i % 6])
        my_pencil.circle(a)
        my_pencil.left(int(x))
        my_pencil.end_fill()
        b += c
        a -= b
        i += 1
elif choice == "streckadcirkel":
    a = float(input("Ange stolek: "))
    b = float(input("Ange minskning: "))
    c = float(input("Ange acceleration: "))
    x = float(input("Ange hur många grader: "))
    i = 0
    while a > 0:
        my_pencil.color(colours[i % 6])
        my_pencil.circle(a)
        my_pencil.left(int(x))
        b += c
        a -= b
        i += 1
input("Done?")