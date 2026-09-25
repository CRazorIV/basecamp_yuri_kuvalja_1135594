conversion_table: dict[int, int] = {}

for celsius in range(0, 101, 10):
    fahrenheit = round(celsius * 9 / 5 + 32)
    conversion_table[celsius] = fahrenheit

print("°C", "°F")

for celsius, fahrenheit in conversion_table.items():
    print(celsius, fahrenheit)
