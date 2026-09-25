# Ask the user for a year 
user_input_in_years = input("Please input a year: ")

# Check if the input is a valid year 
if user_input_in_years.isdigit() and len(user_input_in_years) == 4:
    year = int(user_input_in_years)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Provide a valid year in the format YYYY.")