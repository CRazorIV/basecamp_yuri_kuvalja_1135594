# ask the user for the number of laps. 

number_of_laps_input = input("Input the amount of laps as 'Laps: <number>' ")

laps = int(number_of_laps_input.split(":")[1].strip())

# calculate the total distance in meters and convert it to kilometers as a float. 
total_distance_in_meters = laps * 400
total_distance_in_kilometers = float(total_distance_in_meters / 1000)

print(f"Kilometers: {total_distance_in_kilometers}, Meters: {total_distance_in_meters}")