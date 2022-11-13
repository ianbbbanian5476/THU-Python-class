precent_crabon_14 = 1
decreases_rate = 1-0.00012
year = 0
while precent_crabon_14 > 0.5:
    precent_crabon_14 *= decreases_rate
    year += 1
print(f'Carbon-14 has a half-life of {year} years.')