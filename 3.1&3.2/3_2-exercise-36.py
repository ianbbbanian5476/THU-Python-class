year = int(input('Enter a year: '))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        ans = 'is not'
    else:
        ans = 'is'
else:
    ans = 'is not'
print(f'{year} {ans} a leap year.')