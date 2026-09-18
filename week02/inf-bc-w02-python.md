# Python 02: Branching Programs

**Introduction**: This document presents learning steps for Python 02. In Python 02, you will learn basics of Python structures to add decision points to your programs. A branching program is a flow of sequential instructions with branching statements. By the end this week, you will be able to implement a program where a user can enter simple input, the program can make choices based on some conditions and after calculation, results can be printed.

**Note:** Exercises of this learning path can be done using:

1. Online Python Editor **OPyEditor**: The final program should be stored on your local machine.
2. Local Python Package (see Step-01): Using **BRef-01: Appendix B** Python can be installed on your local machine.

## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- **BRef-02**: Book, Mark Lutz; **"Learning Python: Powerful Object-Oriented Programming"**; [Available here](https://www.oreilly.com/library/view/learning-python-6th/9781098171292/)
- **ORef-01**: Online Tutorial; Charles Severance; "Python for Everybody"; [Available here](https://books.trinket.io/pfe/index.html)
- **OPyEditor**: Online Editor for Programming; "Online Python (with shell and file storing functionalities)"; [Available here](https://www.online-python.com/)

## Path:

Follow these steps:

### Step-01: Set Up

#### Goals:

```
After taking this step, you will be able to:
	1. implement and run your Python programs on your local machine.
```

#### What to Learn?

1. Using **BRef-01: Appendix B** perform the following tasks:
   1. Install Python on your machine.
   2. Open a terminal (command window) and check the version of your Python. Which command did you use?
   3. Using **OPyEditor** implement a program that prints a statement of a defined variable, like `Hello Python!`. Save the file on your local machine within a folder created by you. Using your terminal (command line) execute your first Python program. Which command do you need to execute a Python program?

I checked my Python version with `python3 --version` in the terminal. To run a program I use `python3 filename.py`, so for my first program that was `python3 hello.py`. The variable version of the program looks like this:

```python
hello_message = "Hello Python!"
print(hello_message)
```

#### Exercises:

1. Create a file named `print_input.py`. Open it using an editor of your own choice. Enter your code in it to ask the user to input a text. Print that text. Run the file using the command line.

see resource: print_input.py

2. Read **BRef-01: Chapter 01, Section Running Python** and runPython shell. Excute `quit()`. What do you observe?

I quit the python shell using this function.

3. StartPython shell and execute `num = input('Enter a number:')`. Enter a number and print the value of `num`. There are two different ways to print the value of `num`. Try both at shell. Which one works in **OPyEditor**? Do you recognise differences between programming using _python shell_ and an _editor_? Read **BRef-01: Chapter 01, Section Running Python** including subsections.

I use visual studio code as my main text editor and not the python shell or the OPyEditor.
When I run this I simply get back the value of a number in a string format since this is not converted to a int.

**Note**: After this step, you can try both _python shell_ and _editor_ to practice. It is recommended to use _python shell_ for small experiments and use programming within *editor*s (local or online) for writing a full program.

For ease of use I mainly use the editor since I can use the python interperter from there as well.

<hr>

### Step-02: Programs need to decide.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement boolean expressions.
	2. implement Python programs with conditional statements.
```

#### What to Learn?

1. Using **BRef-01: Chapter 04** and **BRef-02: Chapter 12** discuss and experiment the following questions:
   1. What is a comment? How can you specify a comment in Python?
   2. What are: boolean values, boolean expressions, comparison operators?
   3. What is a conditional statement in Python? What is correct syntax for a correct _if-else_ statament? What is a _body_ of a _if-else_ statement?

**1. Comments** \
A comment is a piece of text in the code that Python does not execute. It is there to explain to a human reader what the code does. In Python a comment starts with a `#`, everything after it on that line is ignored by the interpreter.

```python
# this whole line is a comment
print("Hello")  # a comment can also come after code
```

**2. Boolean values, boolean expressions and comparison operators** \
A boolean value is one of the two values `True` or `False`. A boolean expression is an expression that evaluates to a boolean value, for example `5 > 3` evaluates to `True`. Comparison operators are the operators used to build those expressions: `==` (equal to), `!=` (not equal to), `<` (smaller than), `>` (bigger than), `<=` (smaller than or equal to) and `>=` (bigger than or equal to).

**3. Conditional statements** \
A conditional statement lets the program choose between different blocks of code depending on whether a boolean expression is `True` or `False`. The syntax is the keyword `if`, then the condition, then a colon `:`. The `else` branch runs when the condition is `False`. The _body_ is the indented block of code underneath the `if` or the `else`, the indentation is what tells Python which lines belong to which branch.

```python
if temperature > 30:
    print("It is hot")   # this indented line is the body of the if
else:
    print("It is not hot")   # this indented line is the body of the else
```

#### Exercises:

1. Create a variable with the value `True`. Print it. Change the value to `False`. Print it.

```python
truthy = True
print(truthy)

truthy = False
print(truthy)
```

2. Create a variable
   - named `a` with the value `True`, another
   - named `b` with the value `False`. Use print to check the output of `print(a == b)`.
   - Do the same for the other comparison operators, `!=`, `<`, `>`, `<=`, `>=`.

```python
a = True
b = False

print(a == b)  # False
print(a != b)  # True
print(a < b)   # False
print(a > b)   # True
print(a <= b)  # False
print(a >= b)  # True
```

What I noticed here is that `<` and `>` also work on booleans, because Python treats `True` as `1` and `False` as `0`. That is why `a > b` gives `True`.

3. Repeat the second exercise using an _if-statement_. Print `yes` or `no`, for true false.
   - Write a comment above the _if-statement_ explaining with it does.

```python
a = True
b = False

# check whether a and b hold the same value, print yes if they do and no if they don't
if a == b:
    print("yes")
else:
    print("no")

# check whether a and b hold different values
if a != b:
    print("yes")
else:
    print("no")
```

4. Implement a program in which the user is asked for input. Save the input of the user in a variable. Print `yes` if the input contains the character `e`, `no` if not.

```python
user_text = input("Enter some text: ")

# the in operator checks whether the character e appears anywhere in the text
if "e" in user_text:
    print("yes")
else:
    print("no")
```

5. Think of an useful situation where you need to check something with a if-statement within another if-statement (nested if-statements). Code it and write a comment to explain why it needs a nested if.

A useful situation is entry to a concert: you have to be 18 or older **and** you need a ticket. The second question only makes sense once the first one is answered, and the message I want to show is different for each case.

```python
age = int(input("How old are you? "))
has_ticket = input("Do you have a ticket? (yes/no) ")

# the ticket only needs to be checked if the visitor is old enough, so that
# check is nested inside the age check. This way I can give three different
# messages instead of one general "no".
if age >= 18:
    if has_ticket == "yes":
        print("Welcome to the concert!")
    else:
        print("You are old enough, but you still need a ticket.")
else:
    print("Sorry, you must be 18 or older.")
```

6. Finish all the exercises listed in **BRef-01-Chapter 04: Things to Do**.

<!-- TODO Yuri: the Chapter 04 "Things to Do" exercises still need to be made and pasted in here. -->

<hr>

### Step-03: What is a function?

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python functions: function definition, calling functions, return of a function, functions with arguments.
```

#### What to Learn?

1. Using **BRef-01: Chapter 09** and **BRef-02: Chapter 16** answer and experiment the following questions:
   1. What is a function in Python?
   2. What are the main elements of a Python function? Define a simple function that does nothing.
   3. How can a function be used (called)?
   4. How can one return the result of a function?
   5. What are the arguments and/or parameters?

**1. What is a function?** \
A function is a named, reusable block of code that performs one task. You write it once and you can call it as many times as you want, which keeps the program shorter and easier to read.

**2. Main elements of a function** \
A function consists of the keyword `def`, a name, a pair of parentheses that can hold parameters, a colon `:`, and an indented body. A function that does nothing still needs a body, so you use the keyword `pass`:

```python
def do_nothing():
    pass
```

**3. Calling a function** \
You call a function by writing its name followed by parentheses, with the arguments inside them: `do_nothing()` or `sum_numbers(5, 10)`. A function only runs when it is called, defining it is not enough.

**4. Returning a result** \
With the `return` keyword. `return` sends a value back to the place where the function was called, so you can store it in a variable or use it in another expression. A function without a `return` gives back `None`. This is different from `print()`, which only shows something on the screen and does not give a value back.

**5. Arguments and parameters** \
Parameters are the names in the function definition, arguments are the actual values you pass in when you call the function.

```python
def greet(name):     # name is the parameter
    print(f"Hello {name}")

greet("Yuri")        # "Yuri" is the argument
```

#### Exercises:

_Note_: In the following exercises you can decide yourself what should be the name of function in your solution. Check [PEP8 Function and Variable Names](https://peps.python.org/pep-0008/#function-and-variable-names) for guidelines.

1. Explain in your own words the difference between `arguments` and `parameters`.

An argument is used with the data passed to the function when the function is called, inside the function the arguments are assigned to variables called parameters.

2. Create a function that just prints the word `hello`. Call the function and run your program. Where the function is _defined_? Where is it _called_?

```python
def hello_world():
    print("Hello")

hello_world()
```

3. Create a function that takes a text as an argument. The function prints the text it receives. Call the function and run your program.

```python
def hello_input(name: str) -> None:
    print(f"Hello {name}!")

name = input("What is your name? \n")
hello_input(name)
```

4. Create a function that takes two numbers as argument. The function adds the numbers together and returns the results. Call the function and run your program.

```python
def sum_numbers(number1: int, number2: int) -> int:
    return number1 + number2

result = sum_numbers(5, 10)
print(result)
```

5. Create two functions, each takes a number as argument. The first one returns the number multiplied by 2 and returns it. The second multiplies it by 10 and returns it. Calling both functions add the two returned numbers together and print it. Run your program and check the results.

```python
def doubled(number: int) -> int:
    return number * 2

def multiplied_by_10(number: int) -> int:
    return number * 10

number = 5

doubled_value = doubled(number)
multiplied_by_10_value = multiplied_by_10(number)

# 10 + 50 = 60
print(doubled_value + multiplied_by_10_value)
```

6. Create two functions. One that prints `hello`, the other prints `bye`. Ask the user to input a number, if the number is higher than 10, call the first function. If the number if lower or equal to 10, call the second function. Test your program.

```python
def hello() -> str:
    return "Hello"

def bye() -> str:
    return "Bye"

user_input: int = int(input("Input a number: "))

if user_input > 10:
    print(hello())
else:
    print(bye())
```

7. Create two functions. One that prints `hello`, the other prints `bye`. The first functions calls the second one after printing. Call the first function.

```python
def hello() -> None:
    print("Hello")
    bye()

def bye() -> None:
    print("Bye")

hello()
```

Both functions only print, they do not return anything, so the return type is `None` and not `str`. Calling `bye()` from inside `hello()` works because by the time `hello()` is actually called, `bye` is already defined.

8. Provide your solutions to the exercises of **ORef-01: Functions**. The description of functions in **ORef-01: Functions** can be used as extra learning reference.

<p>Helaas kan deze opdracht niet worden uitgevoerd omdat deze bron niet meer beschikbaar is.</p>

9. Design two exercises of your own. They should improve understanding topics of this step.

**Exercise 9a: `return` is not the same as `print()`**

> Write two functions that both double a number. The first one, `double_and_return`, gives the result back with `return`. The second one, `double_and_print`, shows the result with `print()` and returns nothing.
> Call both functions with the number `5` and store each result in a variable. Print both variables and explain the difference. Then try to use the result of each function in a new calculation.

```python
def double_and_return(number: int) -> int:
    return number * 2

def double_and_print(number: int) -> None:
    print(number * 2)

returned_value = double_and_return(5)
printed_value = double_and_print(5)

print(f"returned_value = {returned_value}")
print(f"printed_value  = {printed_value}")

# only the returned value can be used again in a new calculation
print(double_and_return(returned_value))
```

Output:

```
10
returned_value = 10
printed_value  = None
20
```

_Why this exercise helps:_ both functions look like they "do the same thing", because the number `10` appears on the screen either way. But `printed_value` is `None`, because `double_and_print` shows the value instead of giving it back. Only `returned_value` can be fed into another calculation. This makes visible that `print()` is output to the screen and `return` is output to the rest of the program.

**Exercise 9b: parameters, default values and keyword arguments**

> Write a function `apply_discount` that takes a price and a discount percentage and returns the new price. Give the percentage a default value of 10, so the function can also be called with only a price. Write a second function `format_price` that takes an amount and returns it as a readable string.
> Call `apply_discount` three ways: with only a price, with both values as positional arguments, and with both values as keyword arguments in reversed order. Print each result through `format_price`.

```python
def apply_discount(price: float, percentage: float = 10.0) -> float:
    """Return the price after subtracting the given discount percentage."""
    return price - (price * percentage / 100)

def format_price(amount: float) -> str:
    """Return the amount as a readable euro string."""
    return f"EUR {amount:.2f}"

# 1. only a price, so the default percentage of 10 is used
print(format_price(apply_discount(50.0)))

# 2. two positional arguments, the order decides which parameter gets which value
print(format_price(apply_discount(50.0, 25.0)))

# 3. two keyword arguments, now the order does not matter
print(format_price(apply_discount(percentage=50.0, price=50.0)))
```

Output:

```
EUR 45.00
EUR 37.50
EUR 25.00
```

_Why this exercise helps:_ it shows that a parameter can have a default value, so an argument becomes optional. It also shows the difference between positional arguments, where the order decides everything, and keyword arguments, where the name decides. And because `format_price(apply_discount(...))` passes the returned value of one function straight into another, it shows that a `return` value is just a value you can keep using.

10. Install _Visual Studio Code_ on your working machine. Implement and run a simple Python program of your choice.
    - It is important to learn how to create a new Python program, how to configure interpreter and how to run the program. Where do you see the results?

The results are returned in the terminal.

## Code Analysis

1. Given the following problem statement, one of the students has submitted two solutions. The submitted solutions may not work correctly.
   - Without executing the submitted code, check the implementation, analyze and find the issue(s).
   - Use the following link to run the code step by step and visualize the execution. [Python Execution Visualizer](https://cscircles.cemc.uwaterloo.ca/visualize) Note: Before pressing "Visualize Execution" you need to enter your input at "Enter optional text input for ...".
   - This step-by-step execution should confirm the issues you have found in the code.
   - After listing the issues, propose how the code must be fixed. Fix the code and again use step-by-step execution to see that the possible issues are fixed.
   - Remember: the main goal is to learn how the program is executed step-by-step. Focus on the **goal**.

   **Problem Statement**

   > Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number.
   >
   > ###### Input example:
   >
   > `3141`
   >
   > ###### Output example:
   >
   > `3+1+4+1=9`

   **Incorrect Solutions** \
   Solution 1:

   ```python
   fourdigit_num = int(input("Input a four digit number: "))
   x  = fourdigit_num // 1000
   x1 = (fourdigit_num - x * 1000) // 100
   x2 = (fourdigit_num - x * 1000 - x1 * 100) // 10
   x3 = fourdigit_num - x * 1000 - x1 * 100 - x2 * 10
   print("Sum:",x+x1+x2+x3)
   ```

   Solution 2:

   ```python
   numstr = input("enter a 4 digit number")
   sum = 0
   text = ""
   for i in range(len(numstr)):
      sum += int(numstr[i])
      text = text + numstr[i]
   print(text)
   ```

   **Analysis**

   _Solution 1_

   The arithmetic in this solution is actually correct. With the input `3141` the variables become `x = 3`, `x1 = 1`, `x2 = 4`, `x3 = 1` and the sum is `9`. The issues are:
   1. **The output does not match the problem statement.** The program prints `Sum: 9`, but the required output is `3+1+4+1=9`. The individual digits have to be shown in the output, with `+` between them and `=` before the total.
   2. **There is no check that the input really has four digits.** If the user enters `31`, then `x` and `x1` become `0` and the program silently gives a wrong looking answer instead of warning the user.
   3. **The variable names say nothing.** `x`, `x1`, `x2` and `x3` do not explain that they are the thousands, hundreds, tens and units digit. This makes the code hard to follow.

   _Solution 2_

   This solution has a bigger problem, it never produces the required result at all:
   1. The sum is calculated but never printed. The variable `sum` is filled in correctly inside the loop, but the last line only prints `text`. The `=9` part of the output is simply missing.
   2. **`text` is built without the `+` signs.** The line `text = text + numstr[i]` just glues the digits back together, so for the input `3141` it prints `3141` instead of `3+1+4+1`. The loop rebuilds the input instead of formatting it.
   3. **`sum` overwrites a built-in function.** Python already has a function called `sum()`. Using it as a variable name shadows it, so it can no longer be used later in the program. A name like `total` is better.
   4. The program works for any number of digits, not only four.

   Step-by-step execution \

   Running solution 2 in the visualizer with the input `3141` confirms this: after the four rounds of the loop `sum` holds `9` and `text` holds `"3141"`, and then only `text` is printed. So the value `9` is calculated and then thrown away, which is exactly issue 1.

   Fixed code

   Solution 1 fixed, the digits are now printed in the required format:

   ```python
   fourdigit_num = int(input("Input a four digit number: "))

   thousands = fourdigit_num // 1000
   hundreds = (fourdigit_num - thousands * 1000) // 100
   tens = (fourdigit_num - thousands * 1000 - hundreds * 100) // 10
   units = fourdigit_num - thousands * 1000 - hundreds * 100 - tens * 10

   total = thousands + hundreds + tens + units
   print(f"{thousands}+{hundreds}+{tens}+{units}={total}")
   ```

   Solution 2 fixed, the `+` signs are added and the total is printed:

   ```python
   numstr = input("Enter a 4 digit number: ")

   total = 0
   text = ""

   for i in range(len(numstr)):
       total += int(numstr[i])
       if i == 0:
           text = numstr[i]
       else:
           text = text + "+" + numstr[i]

   print(f"{text}={total}")
   ```

   Both fixed versions give `3+1+4+1=9` for the input `3141`, which matches the output example of the problem statement.
