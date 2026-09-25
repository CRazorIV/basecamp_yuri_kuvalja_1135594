# Ask the user for year input and convert it to a whole number

user_input_in_years = int(input("Years: "))

# Process the user input and convert it to days by multiplying by 365 and for months multiply by 12 (Not accounting for leap years)
amount_of_days = user_input_in_years * 365 
amount_of_months = user_input_in_years * 12

# Print the output to the console.
print(f"Months: {amount_of_months}, Days: {amount_of_days}")

# 1135594 | Yuri Kuvalja