user_string: str = input("Enter a sentence: ")

i = 0
j = len(user_string) - 1
is_palindrome = True

while i < j:
    if user_string[i] != user_string[j]:
        is_palindrome = False
        break
    i += 1 
    j -= 1

if is_palindrome:
    print(f"{user_string} is a palindrome.")
else:
    print(f"{user_string} is not a palindrome.")
