# the amount of sides into a dictionary keyed to the shape.
shapes = {
    3: "Triangle",
    4: "Square",
    5: "Pentagon",
    6: "Hexagon",
    7: "Heptagon",
    8: "Octagon",
    9: "Nonagon",
    10: "Decagon",
}

#ask the user for the amout of sides
amount_of_sides = int(input("Please input the amount of sides: "))

#try to access the key value and print to the console
try:
    print(shapes[amount_of_sides])
except KeyError:
    print("Amount of sides is out of range.")
