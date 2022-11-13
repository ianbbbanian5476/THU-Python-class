now = 7000000000
rate = 1.011
year = 2011
while now < 8000000000:
    now *= rate
    year += 1
print(f'World populations will be 8 billion in the year {year}')
