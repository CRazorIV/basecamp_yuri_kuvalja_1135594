# Ask the user input for the widgets and gizmos 
widgets = int(input("the number of widgets: "))
gizmos = int(input("the number of gizmos: "))
# Process the input to calculate the total weight of the order
order = widgets * 75 + gizmos * 112
# output the calculated weight to the console
print(f"The Total Weight of the Order: {order} grams")