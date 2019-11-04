import math

# defining all the basic calculations
def calculate_base():
    """Calculates base from area and height"""
    area = float(input("Area: "))
    height = float(input("Height: "))
    base = area / height
    return base
def calculate_height():
    """Calculates height from area and base"""
    area = float(input("Area: "))
    base = float(input("Base: "))
    height = area / base
    return height
def calculate_area():
    """Calculates area from base and height"""
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = base * height
    return area
def calculate_radius():
    """Calculates radius from circle area"""
    area = float(input("Area: "))
    radius = pow(float(area / math.pi), 0.5)
    return radius
def calculate_circleArea():
    """Calculates circle area from radius"""
    radius = float(input("Radius: "))
    area = pow(radius, 2) * math.pi
    return area

# Instruction for the different calculations 
def instruction():
    print("\n2-dimensional\n",
    "Triangle -base, -height, -area\n",
    "Rectangle -base, -height, -area\n",
    "Cirkle - radius, -circum(ference), -area\n",
    "Commands: Instruction, Stop")
    print("\nWrite your prefered calculation\nEx: 'Triangle-base' or 'Circkle-circum'")
instruction()
command = str.lower(input("> "))
while command != "stop":
    # 2-dimensional
    if command == "instruction":
        instruction()
    elif command == "triangle-base":
        answer = calculate_base() * 2
        print("The base is", answer)
    elif command == "triangle-height":
        answer = calculate_height() * 2
        print("The height is", answer)
    elif command == "triangle-area":
        answer = calculate_area() / 2
        print("The area is", answer)
    elif command == "rectangle-base":
        answer = calculate_base()
        print("The base is", answer)
    elif command == "rectangle-height":
        answer = calculate_height()
        print("The height is", answer)
    elif command == "rectangle-area":
        answer = calculate_area()
        print("The area is", answer)
    elif command == "circle-radius":
        answer = calculate_radius()
        print("The radius is", answer)
    elif command == "circle-circum" or command == "circle-circumference":
        answer = calculate_radius() * 2
        print("The circumference is", answer)
    elif command == "circle-area":
        answer = calculate_circleArea()
        print("The area is", answer)
    command = str.lower(input("> "))
print("Ending the program")