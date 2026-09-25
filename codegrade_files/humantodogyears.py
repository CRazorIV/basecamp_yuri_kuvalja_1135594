# Ask the user for the amount of years and convert to interger
human_years: int = int(input("Human Years: "))

# positive numbers check
if human_years > 0:

    dog_years_list: list = [] 

    for years in range(human_years):
        # the first 2 values we count as 10.5 dog years.
        if years < 2:
            dog_years_list.append(10.5)
        # The rest of the values we count as 4 dog years.
        else:
            dog_years_list.append(4)

    # sum up all the values
    dog_years = sum(dog_years_list)

    print(f"Dog years: {dog_years}")

else:
    print("Provide only a positive number!")
