# Step-01: Strings

# 1. Ask the user to input a text. Print the length of the entered text.
text = input("Enter a text: ")
print(len(text))

# 2. Ask the user to input a text. Replace the first character with a `k` and print the result.
text = input("Enter a text: ")
print("k" + text[1:])

# 3. Make a variable with the text "this is a text". Remove all spaces from it. Print the result.
text = "this is a text"
print(text.replace(" ", ""))

# 4. Ask the user to input a text. Capitalize the complete input. Print the result.
text = input("Enter a text: ")
print(text.upper())

# 5. Ask the user to input a text. Remove all `e` characters from it. Print the result.
#    Without an `e` in the input, replace() simply finds nothing and returns the text unchanged.
text = input("Enter a text: ")
print(text.replace("e", ""))

# 6. Ask the user to input a text. Count how many times the input contains the character `i`.
text = input("Enter a text: ")
print(text.count("i"))

# 7. Ask the user to input two texts (two inputs). Print them together in one line using an f-string.
first = input("Enter a text: ")
second = input("Enter another text: ")
print(f"{first} {second}")


# Step-02: Looping with while

# 1. Print the numbers 1 to 42 using a `while` loop.
number = 1
while number <= 42:
    print(number)
    number = number + 1

# 2. Print all odd numbers between 1 to 100 by using a `while` loop.
number = 1
while number <= 100:
    if number % 2 != 0:
        print(number)
    number = number + 1

# 3. Print the numbers from 10 to -10 using a `while` loop.
number = 10
while number >= -10:
    print(number)
    number = number - 1

# 4. Ask the user to input a text. Print each character of the input on a new line using a `while` loop.
text = input("Enter a text: ")
index = 0
while index < len(text):
    print(text[index])
    index = index + 1

# 5. Ask the user to input a text. Print each character of the input that is the character `e` or `a`
#    on a separate line.
text = input("Enter a text: ")
index = 0
while index < len(text):
    if text[index] == "e" or text[index] == "a":
        print(text[index])
    index = index + 1
