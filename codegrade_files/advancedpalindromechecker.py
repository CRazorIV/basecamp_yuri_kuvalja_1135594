user_string: str = input("Enter a sentence: ")
cleaned = user_string.lower().replace(" ", "")

i = 0
j = len(cleaned) - 1
is_palindrome = True

while i < j:
    if cleaned[i] != cleaned[j]:
        is_palindrome = False
        break
    i += 1 
    j -= 1

if is_palindrome:
    print(f"{user_string} is a palindrome.")
else:
    print(f"{user_string} is not a palindrome.")
