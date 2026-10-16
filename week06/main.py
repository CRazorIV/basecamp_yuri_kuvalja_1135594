# set1: set = {"x","y","q","z","u"} 
# user_input: str = input("Enter a letter: ")

# def compare_letter_to_value(given_letter: str, given_set: set) -> None:
#     isContained: bool = False
#     for value in given_set:
#         if value == given_letter:
#             isContained = True
#             break

#     if isContained:
#         print("Yes")
#     else: 
#         print("No")

# compare_letter_to_value(user_input[0], set1)

# set1: set = {"x","y","q","z","u"} 
# user_input: str = input("Enter a letter: ")
# print("Yes" if user_input in set1 else "No")

# even = lambda x : x % 2 == 0 
# print(even(4))
# print(even(13))


# unordered_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Function composition
# check_even_logic: any = lambda a : a % 2 == 0 
# check_odd_logic: any = lambda a : a % 2 != 0
# even_list: list = list(filter(check_even_logic, unordered_list))
# odd_list: list = list(filter(check_odd_logic, unordered_list))

# print(even_list)
# print(odd_list)


# 3. Complete the function that checks if a given list is sorted or not, use at least one lambda within the function.

# def am_i_sorted(numberlist) -> list:
#     # write the code


# result = am_i_sorted([1,2,5,6,8,17])
# print(result) # True
# result = am_i_sorted([1,2,99,6,8,17])
# print(result) # False

# 4. Create a lambda that takes two arguments and returns a Tuple containing those two values. 
