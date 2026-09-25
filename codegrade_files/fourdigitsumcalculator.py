# Ask the input

user_input = input("Input a four digit number: ")

# Check the type of the input, check if there is a value and check if the input is really 4 digits.
if user_input == "" or not user_input.isdigit() or len(user_input) != 4:
    print("Provide a valid 4 digit number!")
else:
    # Convert the input to a number in the process to not throw a error at a wrong input. 
    number = int(user_input)
    sum = 0 

    # Loop through the user_input and for every iteration add the number up to the sum. 
    for number in user_input:
        sum += int(number)

    # Return the output in a nice format to the console. 
    print(f"{user_input[0]}+{user_input[1]}+{user_input[2]}+{user_input[3]}={sum}")