# Python 05: Functions, Lists and Tuples.

**Introduction**: This document presents learning steps for Python 05. In Python 05, you will learn how to build a sequence structure using basic data types. Moreover, you will learn more features of functions.

**Note:** Exercises of this learning path can be done using:

1. IDE: Using online resources [Visual Studio Code](https://code.visualstudio.com/docs) can be installed on your local machine.

## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- **ORef-01**: Online Tutorial; Charles Severance; "Python for Everybody"; [Available here](https://books.trinket.io/pfe/index.html)

## Path:

### Step-01: Tuples.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs using tuples: creating, unpacking, modifying, combining two tuples, iterating over a tuple.
```

#### What to Learn?

1. Using BaseCamp Tutorial [Available here](./bc-w05-python-tutorial.md) and **BRef-01: Chapter 07** answer and experiment the following questions:
   1. What is a tuple in Python and how is it defined?
   2. How can one combine and compare two (or more) tuples?
   3. How can one iterate over the elements of a tuple?
   4. How is a tuple modified?

#### Exercises:
1. You can create a tuple with mixed types in it, for example texts and numbers. Can you think of a advantage and a disadvantage of doing this? Implement your example.

Using a tuple with mixed values is useful because that means we don't have to define tuples based on types when we can just use the same tuple. Also I can think of another reason which would be that otherwise we could not include nested collections within tuples without mixed types. 

Say my algorithm defines a process which outputs a list that still needs to mutate but I eventually need to lock in which collections are part of the result. I can nest that list into a tuple so the reference cannot be reassigned to a different object. However, the list itself remains mutable its contents can still be changed. A disadvantage of mixed types is that it makes code harder to read, since you have to remember which index holds what type.

2. Create a tuple with three numbers in it. Unpack the tuple into three different variables. Print the last one.

```python
numbers_tuple: tuple[int] = (1,2,3) 
(one, two, three) = numbers_tuple
print(three)
```
3. Create a tuple with two numbers in it, create a second tuple with two texts in it. Add them together into a new tuple. Print the new tuple.

```python
tuple_1: tuple = ("a", "b", "c")
tuple_2: tuple = (1,2,3)
combined_tuples: tuple = tuple_1 + tuple_2
print(combined_tuples)
```

4. Create a tuple with three numbers in it. Use a for loop to iterate over each value. Multiply each value by 2 and print each result.

```python
numbers: tuple = (3, 7, 5)
for num in numbers:
    print(num * 2)
```

5. Create a function that returns a tuple containing three texts. Call the function. Unpack the tuple into variables. Print the variables.

```python
def three_words() -> tuple:
    return ("hello", "world", "python")

(a, b, c) = three_words()
print(a, b, c)
```
6. Design two exercises of your own. They should improve understanding topics of this step.

**Exercise 1:** Create a tuple of five city names. Use a for loop to print only the cities that have more than 5 letters.

```python
cities: tuple = ("Amsterdam", "Rome", "Berlin", "Tokyo", "Rotterdam")
for city in cities:
    if len(city) > 5:
        print(city)
```

**Exercise 2:** Create two tuples with three numbers each. Use a loop to print the sum of matching pairs (first + first, second + second, etc.).

```python
tuple_a: tuple = (10, 20, 30)
tuple_b: tuple = (5, 15, 25)
for i in range(len(tuple_a)):
    print(tuple_a[i] + tuple_b[i])
```

<hr>

### Step-02: Lists.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs using lists: defining, offset, slicing, adding new element, modifying an element.
```

#### What to Learn?

1. Using BaseCamp Tutorial [Available here](./bc-w05-python-tutorial.md) and **BRef-01: Chapter 07** answer and experiment the following questions:
   1. What is a list in Python and how is it defined?
   2. What is the result of *split()* on a string?
   3. There are two ways to get items from a list: offset and slice. What are the pros / cons of each? Experiment with some examples.
   4. How can you add new elements to a list?
   5. How can you modify elements of a list?
   6. How can one iterate over the elements of a list?
   7. *Mutability* is one of the main differences between a tuple and a list. Elaborate this with some example.

#### Exercises:

1. Define a list of integers representing scores of a game. Write a program that prints out maximum and minimum of the ```scores```.
2. Extend your program from the previous exercise such that it prints two largest and two smallest elements of the ```scores```.
3. Write a program that asks the user to enter a list of integers. Do the following:
	- Print the total number of items in the list.
	- Print the last item in the list.
	- Print the list in reverse order.
	- Print Yes if the list contains a 5 and No otherwise.
	- Print the number of fives in the list.
	- Remove the first and last items from the list, sort the remaining items, and print the result.
	- Print how many integers in the list are less than 5.
4. Write a program that generates a list of 20 random numbers between 1 and 100.
 	- Print the list.
	- Print the average of the elements in the list.
	- Print the largest and smallest values in the list.
	- Print the second largest and second smallest entries in the list
	- Print how many even numbers are in the list.
5. Start with the list ```[8,9,10]```. Do the following:
	- Set the second entry (index 1) to 17
	- Add 4,5, and 6 to the end of the list
	- Remove the first entry from the list
	- Sort the list
	- Double the list
	- Insert 25 at index 3
	- The final list should equal ```[4,5,6,25,10,17,4,5,6,10,17]```
6. Create the following lists using a loop.
	- A list consisting of the integers 0 through 49
	- A list containing the squares of the integers 1 through 50.
	- The list ```['a','bb','ccc','dddd', . . . ]``` that ends with 26 copies of the letter z.
7. Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M. For instance, if ```L=[3,1,4]``` and ```M=[1,5,9]```, then N should equal ```[4,6,13]```.
8. Design two exercises of your own. They should improve understanding topics of this step.

```python
import random

# Exercise 1: max and min of scores
scores = [42, 17, 88, 3, 56, 99, 21]
print("Maximum:", max(scores))
print("Minimum:", min(scores))

# Exercise 2: two largest and two smallest elements
ordered = sorted(scores)
print("Two smallest:", ordered[0], ordered[1])
print("Two largest:", ordered[-1], ordered[-2])

# Exercise 3: operations on a user-entered list of integers
raw = input("Enter integers separated by spaces: ")
numbers = [int(x) for x in raw.split()]

print("Total number of items:", len(numbers))
print("Last item:", numbers[-1])
print("Reversed:", numbers[::-1])
print("Contains a 5?", "Yes" if 5 in numbers else "No")
print("Number of fives:", numbers.count(5))

trimmed = sorted(numbers[1:-1])
print("First and last removed, rest sorted:", trimmed)
print("Count of integers less than 5:", len([n for n in numbers if n < 5]))

# Exercise 4: 20 random numbers between 1 and 100
rand_list = [random.randint(1, 100) for _ in range(20)]
print("List:", rand_list)
print("Average:", sum(rand_list) / len(rand_list))
print("Largest:", max(rand_list), "Smallest:", min(rand_list))
unique_sorted = sorted(set(rand_list))
print("Second largest:", unique_sorted[-2], "Second smallest:", unique_sorted[1])
print("Even numbers count:", len([n for n in rand_list if n % 2 == 0]))

# Exercise 5: step-by-step list manipulation
lst = [8, 9, 10]
lst[1] = 17                       # set index 1 to 17
lst.extend([4, 5, 6])             # add 4, 5, 6 to the end
lst.pop(0)                        # remove the first entry
lst.sort()                        # sort the list
lst = lst * 2                     # double the list
lst.insert(3, 25)                 # insert 25 at index 3
print(lst)
print("Matches expected:", lst == [4, 5, 6, 25, 10, 17, 4, 5, 6, 10, 17])

# Exercise 6: build lists using loops
zero_to_49 = [i for i in range(50)]
print(zero_to_49)

squares = [i ** 2 for i in range(1, 51)]
print(squares)

letters = [chr(ord('a') + i) * (i + 1) for i in range(26)]
print(letters)

# Exercise 7: element-wise sum of two equal-sized lists
print("\nExercise 7")
L = [3, 1, 4]
M = [1, 5, 9]
N = [L[i] + M[i] for i in range(len(L))]
print("N =", N)

# Exercise 8: two exercises of my own

# 8a) Remove all duplicates from a list while keeping the original order.
def remove_duplicates(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

print("Without duplicates:", remove_duplicates([1, 2, 2, 3, 1, 4, 3]))

# 8b) Rotate a list to the right by k positions.
def rotate_right(items, k):
    if not items:
        return items
    k = k % len(items)
    return items[-k:] + items[:-k]

print("Rotated by 2:", rotate_right([1, 2, 3, 4, 5], 2))
```

<hr>

### Step-03: Functions (more).

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python functions: positional arguments, keyword arguments, parameters default values, docstrings.
```

#### What to Learn?

1. Using BaseCamp Tutorial [Available here](./bc-w05-python-tutorial.md) and **BRef-01: Chapter 09** answer and experiment the following questions:
   1. What are the positional arguments in Python? What about keyword arguments?
   2. How can one define default values for function parameters?
   3. What are Docstrings? How can they be helpful?

#### Exercises:

1. Describe in your own words what `*args` and `**kwargs` do.

*args allows a unspecified number of positional arguments given to a function. And **kwargs allows a unspecified number of keyword arguments given to a function. 

2. Create a function that takes an `*args` of numbers as argument, which calculates the sum of all numbers and returns the result. Call the function and print the returned value.

```python
def sum_numbers(*numbers):
    """
    Function to sum up all the numbers of values in a tuple.
    """
    total = 0

    for i in range(len(numbers)):
        total += numbers[i]

    return total


print(sum_numbers(40,20,10,10))
```

3. Complete the given code below.

 ```python
def count_passes(**kwargs):
    count = 0
    
    for value in kwargs.values():
        if value == "Pass":
            count += 1
    return count

result = count_passes(math="Fail", science="Fail", history="Pass", english="Pass")
print(result)
```

4. Design two exercises of your own. They should improve understanding topics of this step.

**Exercise A:** Create a function `build_profile` that takes a first name and last name as positional arguments, and any number of keyword arguments (`**kwargs`) to represent additional profile fields. The function should return a dictionary containing all the information. Give default values to first and last name so the function can be called without them.

```python
def build_profile(first_name="Unknown", last_name="Unknown", **kwargs):
    """Build a dictionary containing a user profile."""
    profile = {"first_name": first_name, "last_name": last_name}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

print(build_profile("Yuri", "K", age=25, city="Rotterdam"))
print(build_profile(hobby="coding"))
```

**Exercise B:** Create a function `describe_items` that takes `*args` for item names and `**kwargs` for item descriptions, then prints each item with its description if available, or "No description" otherwise. Include a docstring explaining the function.

```python
def describe_items(*args, **kwargs):
    """Print each item with its description from kwargs, or 'No description' if not provided."""
    for item in args:
        description = kwargs.get(item, "No description")
        print(f"{item}: {description}")

describe_items("apple", "banana", "cherry", apple="A red fruit", cherry="Small and sweet")
```

5. **Extra:** Provide your solutions to the exercises of **ORef-01: Functions**

<!-- Niet repliceerbaar -->

<hr>



## Code Analysis

1. Analyze the given codes below without executing them. What will be the result of the programs?

```python
a_tuple = ('Never', 'gonna', 'give', 'you', 'up')
counter = 0
for x in a_tuple:
    if x[0] ==  'g':
        counter = counter + 1
    else:
        counter = counter + 2
print(counter)
```

```python
def do_something(x):
    rtuple = x,
    for i in range(2,11):
        rtuple = rtuple + ((x*i),)
    return rtuple
print(do_something(6))
```

```python
def do_something(*args, **kwargs):
    for i in args:
        for key, value in kwargs.items():
            if i == key:
                print(value)
#
#
do_something("a", "z", "d", "b", a=1, b=2, c=3, d=4)
```

```python
def process_strings(strings):
    processed_strings = []
    for string in strings:
        processed_string = ""
        for char in reversed(string):
            processed_string += char
        processed_strings.append(processed_string)
    return processed_strings

def main():
    names = ["Alice", "Bob", "Charlie", "Dave"]
    processed_names = process_strings(names)
    for name in processed_names:
        print(name)

main()
```