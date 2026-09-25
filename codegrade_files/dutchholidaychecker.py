dutch_holidays: dict = {
    (1, 1): "Nieuwjaarsdag",
    (4, 27): "Koningsdag",
    (5, 5): "Bevrijdingsdag",
    (12, 5): "Sinterklaas",
    (12, 25): "Kerstdag",
    (12, 26): "2de kerstdag",
}

user_input: str = input("Enter the day and month: ")

# split the input on the comma to separate month and day
month_part, day_part = user_input.split(",")

# extract the numbers after the colon and convert to integer
month: int = int(month_part.split(":")[1])
day: int = int(day_part.split(":")[1])

# look up the holiday using the (month, day) tuple as key
holiday: str = dutch_holidays.get((month, day))

# if there is a valid holiday then we print it to console  
# otherwhise we print that there is no holiday
if holiday:
    print(holiday)
else:
    print("No holiday found on given input.")