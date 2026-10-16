# Python 06: Functions, Dictionaries and Sets.

**Introduction**: This document presents learning steps for Python 06. In Python 06, you will learn dictionaries to collect keys and coresponding values. Moreover, you will learn how anonymous functions can be helpful. 


**Note:** Exercises of this learning path should be done using:

1. IDE: Using online resources [Visual Studio Code](https://code.visualstudio.com/docs) can be installed on your local machine.


## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- **ORef-01**: Online Tutorial; Charles Severance; "Python for Everybody"; [Available here](https://books.trinket.io/pfe/index.html)
- **ORef-02**: Book, Brian Heinold; "A Practical Introduction to Python Programming" [Available Online, Check here](https://www.brianheinold.net/python/python_book.html)


## Path:

### Step-01: Dictionaries.

#### Goals:

```
After taking this step, you will be able to interpret and implement Python programs with Python Dictionaries: creating, adding and modifying items,  extracting value(s), extracting key(s), deleting, pop and clear, iteration over dictionaries.
```

#### What to Learn?

1. Using **BRef-01: Chapter 08** answer and experiment the following questions:
   1. What is a dictionary in Python and how can you create a dictionary?
   2. How can items be added/changed to/in a dictionary?
   3. How can you get the value of a given key?
   4. What are the behaviour of these functions: *keys()*, *values()*, *items()*?
   5. When can we use *del*, *pop()* and *clear()*? Experiment with some examples.
   6. How can one iterate over a dictionary?

#### Exercises:

1. Describe in your own words the difference between a `dictionary` and a `tuple`.

A dictionary is a collection of key-value pairs where each key is unique and maps to a value. You can look up, add, change, and remove items by their key. A tuple is an ordered, immutable sequence of values accessed by index. The main differences: dictionaries are mutable and use keys for access, while tuples are immutable and use numeric indices.

2. Create a new dictionary containing a key named `FirstName` with the value `Larry`, a key named `LastName` with the value `Page`. Print the last value from the dictionary.

```python
person = {"FirstName": "Larry", "LastName": "Page"}
last_value = list(person.values())[-1]
print(last_value)
```

3. Create a dictionary with the following pairs `"brand": "Ford", "model": "Mustang", "year": 1964`.
	- Print all the values from the dictionary.
	- Print all the keys from the dictionary.
	- Print the length of the dictionary.
	- Add `"color": "Red"` and remove the pair with key = `"year"`. Print keys and values separately.

```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

print("Values:", list(car.values()))
print("Keys:", list(car.keys()))
print("Length:", len(car))

car["color"] = "Red"
del car["year"]

print("Keys:", list(car.keys()))
print("Values:", list(car.values()))
```

4. Modify the code from the previous exercise so each value becomes a `tuple` containing two random numbers.

```python
import random

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

for key in car:
    car[key] = (random.randint(1, 100), random.randint(1, 100))

print(car)
```

5. Provide your solutions to the exercises of **ORef-01: Dictionary**.

6. Design two exercises of your own. They should improve understanding topics of this step.

**Exercise A:** Create a dictionary that maps student names to their grades (as a list). Write code that iterates over the dictionary and prints only students who have an average grade above 7.

```python
students = {
    "Alice": [8, 7, 9],
    "Bob": [5, 6, 4],
    "Charlie": [7, 8, 8],
    "Diana": [6, 5, 7]
}

for name, grades in students.items():
    average = sum(grades) / len(grades)
    if average > 7:
        print(f"{name}: average = {average:.1f}")
```

**Exercise B:** Create two dictionaries representing inventories of two shops. Merge them into one dictionary where, if both shops have the same item, the quantities are added together.

```python
shop1 = {"apples": 10, "bananas": 5, "oranges": 8}
shop2 = {"bananas": 3, "grapes": 12, "apples": 7}

merged = dict(shop1)
for item, quantity in shop2.items():
    if item in merged:
        merged[item] += quantity
    else:
        merged[item] = quantity

print(merged)
```

7. If you don't have an IDE yet, install an IDE on your working machine. Implement and run a simple Python program of your choice.
	- It is important to learn how to create a new Python program, how to configure interpreter and how to run the program. Where do you see the results?
	- *Note*: Visual Studio Code is recommended as an IDE within this study program. The book **BRef-01** provides and explanation about *PyCharm*.

8. **Extra:** Provide your solutions to the exercises of **ORef-01: Dictionaries**


<hr>


### Step-02: Sets.

#### Goals:

```
After taking this step, you will be able to interpret and implement Python programs with Python Sets: creating sets, difference between sets and lists and tuples, adding and removing elelemnts, membership operator, iteration over a set, basic operations between sets: intersection, union, difference and subset.
```

#### What to Learn?

1. Using **BRef-01: Chapter 08** answer and experiment the following questions:
   1. What is a set in Python and how is it defined?
   2. How can one add/remove elements to/from a set?
   3. How can one iterate over a set?
   4. Assume two sets S1 and S2. How can one specify the following operations on S1 and S2 in Python:
	   - Intersection of S1 and S2.
	   - Union of S1 and S2.
	   - Difference S1 and S2.
	   - Is S1 a subset of S2 (or vice-versa)?

#### Exercises:

1. Describe in your own words the difference between a `set` and a `tuple`.

A set is a unordered collection of items meant as a sort of storage and cannot contain duplicate elements and a tuple is a inmmutable collection meant for storing data that should not mutate. (constants). 

2. Describe in your own words the difference between a `set` and a `list`.

A set is a unordered collection and a list is a ordered collection.

3. Create a set with and fill it with some values you can think of yourself. Print the length and the last value from the set.

```python
# Sets do not support indexing so we first convert it to a list. 
set1 = {"Yuri", "Kuvalja", 19, "Software Developer", True, ("Motivated")}
print(len(set1))
print(list(set1).pop())
```

3. Create a function which takes a `dictionary` as argument and returns a `set` created from the values of the given `dictionary`. Call the function and print all values from the returned set.

```python   
def values_to_set(dictionary: dict) -> set:
    return set(dictionary.values())

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
result = values_to_set(my_dict)

for value in result:
    print(value)
```

4. Create a `set` containing 5 letters `x,y,q,z,u`. Ask the user the input a letter. Check with `if` statement if the given letter is inside the `set`, print `yes` or `no`.

```python
set1: set = {"x","y","q","z","u"} 
user_input: str = input("Enter a letter: ")
print("Yes" if user_input in set1 else "No")
```

5. Design two exercises of your own. They should improve understanding topics of this step.

**Exercise A:** Given two sets of student names, find which students are in both classes (intersection), which are in either class (union), and which are only in class 1 (difference).

```python
class1 = {"Alice", "Bob", "Charlie", "Diana"}
class2 = {"Charlie", "Diana", "Eve", "Frank"}

print("In both:", class1 & class2)
print("In either:", class1 | class2)
print("Only in class 1:", class1 - class2)
```

**Exercise B:** Write a function that takes a list and returns a set of only the elements that appear more than once (the duplicates).

```python
def find_duplicates(items: list) -> set:
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

print(find_duplicates([1, 2, 3, 2, 4, 5, 1, 6]))
```


### Step-03: Functions (more).

#### Goals:

```
After taking this step, you will be able to interpret and implement Python programs with anonymous functions.
```

#### What to Learn?

1. Using **BRef-01: Chapter 09** answer and experiment the following questions:
   1. "Functions are first-class citizens": What does this sentence mean?
   2. What is an anonymous function and how can you define it in Python? Experiment with some examples.

#### Exercises:


1. Complete the given code by creating a lambda that checks if a given number is even.

```python
even = lambda x : x % 2 == 0 
print(even(4))
print(even(13))
```

2. Create a code snippet that splits up a list into two new lists. Depending on if the number in the list is even or odd. Accomplish this with using a lambda and knowledge from the earlier weeks. 
- For example: Original list of integers:
`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
New list with only the even numbers:    
`[2, 4, 6, 8, 10]`.
New list with the odd numbers:
`[1, 3, 5, 7, 9]`

```python
unordered_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function composition
check_even_logic: any = lambda a : a % 2 == 0 
check_odd_logic: any = lambda a : a % 2 != 0
even_list: list = list(filter(check_even_logic, unordered_list))
odd_list: list = list(filter(check_odd_logic, unordered_list))

print(even_list)
print(odd_list)
```

3. Complete the function that checks if a given list is sorted or not, use at least one lambda within the function.

```python
def am_i_sorted(numberlist):
    compare = lambda a, b: a <= b
    return all(compare(numberlist[i], numberlist[i + 1]) for i in range(len(numberlist) - 1))

result = am_i_sorted([1,2,5,6,8,17])
print(result) # True
result = am_i_sorted([1,2,99,6,8,17])
print(result) # False
```

4. Create a lambda that takes two arguments and returns a Tuple containing those two values. 

```python
to_tuple = lambda a, b: (a, b)
print(to_tuple(3, 7))       # (3, 7)
print(to_tuple("hi", True)) # ('hi', True)
```

5. Design two exercises of your own. They should improve understanding topics of this step.

**Exercise A:** Create a list of names and use a lambda with `sorted()` to sort them by the length of each name.

```python
names = ["Alice", "Bob", "Charlotte", "Ed", "Francisco"]
sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names)  # ['Ed', 'Bob', 'Alice', 'Charlotte', 'Francisco']
```

**Exercise B:** Create a lambda that takes a number and returns a string saying whether it is positive, negative, or zero. Use it on a list of numbers with `map()`.

```python
classify = lambda n: "positive" if n > 0 else ("negative" if n < 0 else "zero")
numbers = [-5, 0, 3, -1, 7]
results = list(map(classify, numbers))
print(results)  # ['negative', 'zero', 'positive', 'negative', 'positive']
```


<hr>


## Code Analysis
1. Analyze the given code below without executing it. What will be the result of the program?

 ```python
sfind = set('orihme')
schar = set('ichgo')
print("Step 1:")
for i in sfind:
    if i in schar:
        print(i)
#
print("Step 2:")
schar.update(sfind)
for i in schar:
    print(i)
```

2. Given the following code below. Explain in your own words what happens in this code. What are the keys in the dictionary?

 ```python
import random
rdic = {}
for i in range(0,10):
	rdic[i] = random.randint(0,100)
for item in rdic.values():
	print(item)
```

3. Analyse the given code below without executing it. What will be the result of the program?

```python
r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))
```
