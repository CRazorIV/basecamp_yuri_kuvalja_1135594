#region step-01 exersizes 1 - 3
hello_message = "Hello Python"
print(hello_message)
#endregion 

#region step-02 exersizes 1 - 6
truthy = True
print(truthy)
truthy = False
print(truthy)

a = True
b = False
print(a == b)

# check to see if a is equal to b 
if a == b:
    print("Yes")
else:
    print("No")

#endregion 

#region step-03 exersizes 1 - 10

def hello_world():
    print("Hello")

hello_world()

def hello_input(name: str) -> None:
    print(f"Hello {name}!")

name = input("What is your name? \n")

hello_input(name)

def sum_numbers(number1: int, number2: int) -> int:
    return number1 + number2

result = sum_numbers(5, 10)
print(result)

def hello() -> str:
    return "Hello"

def bye() -> str:
    return "Bye"

user_input: int = int(input("Input a number: "))

if user_input > 10:
    print(hello())
else:
    print(bye())

def hello() -> str:
    print("Hello")
    bye()

def bye() -> str:
    print("Bye") 

hello()

def doubled(number: int) -> int:
    return number * 2

def multiplied_by_10(number: int) -> int:
    return number * 10

doubled_value = doubled(5)
multiplied_by_10_value = multiplied_by_10(doubled_value)

print(doubled_value + multiplied_by_10_value)

#endregion 