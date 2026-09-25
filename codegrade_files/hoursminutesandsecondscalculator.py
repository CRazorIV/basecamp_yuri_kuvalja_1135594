# ask the user for the input in days 
days_input = input("Days: ")

#check if the input is valid and convert it to a whole number 
if days_input.isdigit():
    days = int(days_input)
    # Process the days by multiplying by 24 hours, 60 minutes and 60 seconds to get the 3 values. 
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    # return the 3 values nicely to the console in a f sting 
    print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
else:
    print("Invalid input. Enter a whole number of days.")
