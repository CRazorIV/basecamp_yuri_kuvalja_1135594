# Python 01: Linear Programs.

**Introduction**: This document presents learning steps for Python 01. In Python 01, you will learn the elements of Python to build your first interactive linear program. We define a linear program as a flow of sequential instructions without branching and loops. At the end of Python 01, you will be able to implement a program where a user can enter simple inputs and the program calculates and prints the results as its output.

**Note:** In Python 01, exercises and examples can be executed using:

1. Online Python Editor **OPyEditor**: The final program should be stored on your local machine.

## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- **BRef-02**: Book, Mark Lutz; **"Learning Python: Powerful Object-Oriented Programming"**; [Available here](https://www.oreilly.com/library/view/learning-python-6th/9781098171292/)
- **ORef-01**: Online Tutorial; Charles Severance; "Python for Everybody"; [Available here](https://books.trinket.io/pfe/index.html)
- **OPyEditor**: Online Editor for Programming; "Online Python (with shell and file storing functionalities)"; [Available here](https://www.online-python.com/)

## Path:

Follow the following steps:

### Step-01: What is a Program?

#### Goals:

```
After taking this step, you will be able to:
	1. understand the concept of (computer and non-computer) programs.
	2. experience your first taste of Python without knowing all the details.
```

#### What to Learn?

1. Use **BRef-01: Chapter 01** and **BRef-02: Chapter 02** as a reference and discuss the following questions:
   1. What is a general definition of a program? Provide some (non-computer) examples.
   2. What are the main elements of a (Python) program?
   3. How Python runs programs?
   4. **First Taste of Python**: Read section *Little Programs* and analyze the provided examples.
   5. Consider the following Python programs and guess what each program does. Analyze and discuss inputs, behaviour and expected outputs.
   		- *Note*: Certainly there are lines that you won't understand. The goal is to evaluate your first taste of Python programs and check how intuitive they are. You will be learning all details in later stages.

```python
#Code 01:
words = []
num_str = input("How many words would you like to enter?")
num = int(num_str)
for _ in range(0, num):
	word = input("Next word: ")
  	words.append(word)
print("This is your list of words:", words)
```

#### Exercises:

1. Make a small research to understand the meaning of *syntax in programming*. Give three examples of the programs you have read in **BRef-01: Chapter 01**.

Syntax is the set of rules that determines how code needs to be written so python can understand and run it correctly. It's a bit like grammar in a language: a sentence needs the right structure to make sense, and code needs the right structure to run. If the syntax is wrong it will refuse to run the code. Just like in math where a wrong formula equals a error. Examples from the book introducing python modern computing in simple packages.  

2. Take each of the given following Python programs and carry out these steps:
	- Write down syntactical elements that are understandable for you.
	- Specify statements that you know (or you can guess) the results of the their execution.
	- Share your lists within your learning group.
	- Discuss what will be the result / output of the program (without execution).

*Note*: It is not expected that students understand all the elements of these programs. The main goal is to get a taste of Python programs and discuss about them. *Trust your intuition*.

```python
#Code 02f
a = 16
b = 12
b = a
a = 22
print(a)
print(b)
# what will be printed here?
```
we start of with this:
a = 16
b = 12

from there b gets the value of a (16)
b is now 16
a gets changed to 22 

we print both the values

Output:
```python
22
16
```

I see variables, prints to the console and numbers being used here. 
I understand how this syntax works in python. 

```python
#Code 03
num = int(input("Enter a number: "))
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while num > 0:
       sum += num
       num -= 1
   print("Result is", sum)
```

In this program we have 2 outcomes:

Happy flow: We enter a positive number => while the num is bigger than 0 we add the sum on top of the number in this case the sum is 0 as
defined on line 101. on every iteration the current value of the num gets added up to the sum => the num gets incremented down by steps of 1 until the while loop breaks itself and the sum is printed as the result.

Sad flow: We enter a negative number we enter the if statement and get the output "enter a positive number"

For the syntax I see the use of if else statements, while loop, prints, arithmetic operations using the += -= assignment operators, type conversion in the userinput making it a interger value. 

I understand these syntactic rules in python. 
	
```python
#Code 04
import random
print(random.randint(0, 9))
```
In this program a random number from 0 to 9 can be printed to the console. 

The import is being used here at the top of the file to specify the random module being used in this file. 
Without this import we cannot use the random module. 

I understand how importing elements from other files and utilizing them in my current environment works in python.
	
```python
#Code 05
my_str = input("Enter a string: ")
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
	print(word)
```
I see the use of list comprehension a technique in python to quickly perform operations in a list itself.

The user inputs a string which will be splitted into a list with .split() and is then modified to be lowercased for every element in that list. 

The sort method sorts words ascending from the alphabet by default (A-Z)

Then we print every word to the console as seen in the for loop. 

3. Using **OPyEditor** try to execute the given programs. Does the output of the programs match your expectations?

Yes they did match my expectations as I have listed here above underneath the code snippets. 

<hr>

### Step-02: Everything starts with Data.

#### Goals:

```
After taking this step, you will be able to:
	1. understand values, variables, primitive data types (int, str, float, boolean).
	2. understand the concept of mutability (some data types are mutable and some are not).
	3. implement Python programs containing variables, assigning values, print.
	4. interpret and implement basic operations of strings: concatenation (combining), duplicating, scanning and slicing.
```

#### What to Learn?

1. Using **BRef-01: Chapter 02** and **BRef-02: Chapter 04, Chapter 05** explore the answers for the following questions: 
*Note: There are some concepts (like objects, classes, references) that students may not be able to grasp completely. The main idea is to try as much as possible. They will be more clear later when they learn Object Oriented programming in Python.*
   1. What is a value? What is a variable?
   2. What is a *type*? Provide five examples.
   3. How can you define a variable in Python? 
   4. Define some variables in Python that are not permitted in Python. Experiment with breaking various rules in defining variables. Analyse the error message.
   5. How can you assign a value to a variable? How can we express that two items are equal?
   6. How can you identify the type of a value / variable?
   
4. Using **BRef-01: Chapter 05** and **BRef-02: Chapter 07** discuss and experiment the following questions:
   1. What are the character and text string types in Python? Make examples. 
   2. How can you combine several strings? Implement an example.
   3. Can you multiply a number with a string? What is the result? Implement an example.
   4. How can you get the 5th character of a given string? How can you get the first character?
   5. How can you get a substring from a given string? For example, the zipcodes (postcodes) in The Netherlands consist of 4 digits followed by 2 letters. How can you extract the letters from a given zipcode?
   6. You have learned how to print something as an output of your program. How can you read something as input? What is the *function*? What is the type?


#### Exercises:

1. Check the following program and write down what will be the result of the prints:

```python
x = 12
y = 15
z = 1
y = z
z = 12
y = 13
x = y 
y = x
z = 7
print(x)
print(y)
print(z)
```

To understand this we focus on the first 3 lines of the program so we know what value we start with:
```python
x = 12
y = 15
z = 1
```
from there we can continue line by line like the interperter does. 
y gets assigned the current value of z which is 1 so y is now actually z which is 1 so to yot this down i do 
y = 1 (keep this mentally noted)
z = 12
y = 13

x = 1
y = 1 
z = 7 

Output:
```python
x = 1
y = 1
z = 7
```

2. A phone number is a number. Yet we would want to save it as a text. Can you think of a reason why?

The reason why a phone number is stored as a string object is because of the special characters that are appended with a phone number
take (+31) country codes for example + cannot be stored as a interger theirfore it must be saved as a string. 

3. The number in the address of your house, for example Kerkweg **8**, is a number. Yet we would want to save it as a text. Can you think of a reason why?

4. What is an example from a number we use in the real world that we want to save as a number in Python, not as a text.

Age is a good value to store in a interger format not only specificly in python for that matter. It is always a round number without decimals. 

5. User input in Python is always considered a text, even if we just enter numbers, why would it act like this?

There is no way for Python to know in advance whether what you type is meant to be a number or anything else from the interpreter sees everything the user types as a raw sequence of characters until it's told otherwise. So input() always hands back a string no matter what was typed.

6. Define a variable called zipcode (postcode) and give it the value of your own zipcode. Print it using print().

```python
zipcode = "2991EH" 
print(zipcode)
```

7. Define a variable called favorite_food, give it the value "Pizza". Print it. Change the value to "Roti". Print it. 

```python
favorite_food = "Pizza" 
print(favorite_food)
favorite_food = "Roti"
print(favorite_food)
```

8. Define a variable that stores your school email address. Extract your student number from this email address.

```python
school_email = "1135594@hr.nl"
at_index = school_email.find("@")
student_number = school_email[:at_index]
print(student_number)
```

9. Write down the complete alphabet in a variable. Split it halfway over two different variables. Join them back together in the wrong order and print it. 

```python

alphabet = "abcdefghijklmnopqrstuvwxyz"

half = len(alphabet) // 2     
first_half = alphabet[:half]   
second_half = alphabet[half:]  

wrong_order = second_half + first_half
print(wrong_order)

```

10. Explain in your own words with an ```f``` string is?

fstring allows you to embed variables and expressions in a string. 

```python
age_output = f"your age is: {age}" 
print(age_output)
```

11. Finish all the exercises listed in **BRef-01-Chapter 02: Things to Do** and Practice the exercises listed in **BRef-01-Chapter 05: Things to Do**.

<hr>

### Step-03: How to Calculate?
#### Goals:
```
After taking this step, you will be able to:
	1. understand the main arithmetic operations in Python.
	2. implement arithmetic expressions in Python.
	3. convert one primitive data type to another using functions: int(), float(), str(), bool().
	4. implement Python programs containing: input from the user, type conversion, calculation, printing.
```
#### What to Learn?

1. Using **BRef-01: Chapter 03** and **BRef-02: Chapter 05**answer the following questions:
   1. Name basic built-in data types in Python. Use examples.
   2. What are the basic arithmetic operations? Make a list with the meaning (semantics) of each operation.
   3. Why is *precedence* an important concept? Make examples.
   4. How can you convert one data type to another? Name basic built-in functions.

#### Exercises:

1. Create two variables with a number in it, you can decide which numbers, add them together and print the result.
2. Do the same for subtraction, division and multiplication.
3. Get input from the user. Save it as a number. Print it.
4. Try to divide something by zero. Describe the error you get.
5. Create two variables with text in them. Print them togeter at once, using only 1 print statement.
6. Python uses PEMDAS. What is that and is it different from the way you learned it?
7. Create one calculation using at least four parentheses, three multiplications and four subtractions. Print the result.
8. Finish all the exercises listed in **BRef-01-Chapter 03: Things to Do**.


## Code Analysis


1. Analyze the programming solutions given below and write down in one sentence: what do they do? What problems do they try to solve?

```python
# Code Analysis 1
# Inputs
a = int(input("enter value A: "))
b = int(input("enter value B: "))

# Processing
t = a
a = b
b = t

# Outputs
print("A =", a)
print("B =", b)
```

```python
# Code Analysis 2

# Inputs
num = int(input("Enter a number: "))

# Processing
dig = num % 10

# Outputs
print(dig)
```

2. Implementing a solution for a given problem is challenging for a starting programmer. It is helpful to have a guideline with some steps. Check [this guideline](./checklist_metacog.pdf) and apply it the Problem 5 of this week. *Hint: A template with some examples provided [here](./template.py)*

3.  One of the students has tried to apply the guideline for a given problem. But, the code does not produce the expected results. Check the code and without executing the code try to find the mistake.

```python
# Ask the user for the name of item X.
# Then ask the user for the price of item X.
# Finally, ask the user for desired quantity of item X.
# Based on input, calculate how much you have to pay.
# Write the message in the form:
#   "To purchase N units of X you must pay M euros."


# Inputs
name = input("Input the name of item X: ")

price = input("What is the price of", name, "? ")

quantity = input("How many units of", name, "do you want to buy? ")

# Processing
total = price * quantity

# Outputs
print("To purchase", quantity, "units of", name, "you must pay", total, "euros.")
```
