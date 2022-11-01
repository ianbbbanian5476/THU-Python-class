wage = eval(input('Enter hourly wage: '))
worked = eval(input('Enter number of hours worded: '))
if worked >= 40:
    other = worked - 40
    worked = 40
else:
    other = 0
print(f'Gross pay for week is ${(worked * wage) + (1.5 * wage * (other)) :.2f}')