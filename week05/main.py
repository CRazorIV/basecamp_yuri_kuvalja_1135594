# # def sum_numbers(*numbers):
# #     """
# #     Function to sum up all the numbers of values in a tuple.
# #     """
# #     total = 0

# #     for i in range(len(numbers)):
# #         total += numbers[i]

# #     return total


# # print(sum_numbers(40,20,10,10))

# def count_passes(**kwargs):
#     count = 0
#     #Complete this function to count the number of passes

#     for value in kwargs.values():
#         if value == "Pass":
#             count += 1
#     return count

# result = count_passes(math="Fail", science="Fail", history="Pass", english="Pass")
# print(result)

# numbers_tuple: tuple[int] = (1,2,3) 
# (one, two, three) = numbers_tuple
# print(three)

tuple_1: tuple = ("a", "b", "c")
tuple_2: tuple = (1,2,3)
combined_tuples: tuple = tuple_1 + tuple_2
print(combined_tuples)