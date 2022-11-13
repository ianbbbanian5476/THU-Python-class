coffee_temp = 212
room_temp = 70
k = 0.079
mins = 0
while coffee_temp > 150:
    coffee_temp -= k * (coffee_temp - room_temp)
    mins += 1
print(f'The coffee will cool to below 150 degrees in {mins} minutes.')