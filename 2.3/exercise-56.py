be_salary = int(input('Enter begining salary:'))
cal = be_salary * 1.05 * 1.05 * 1.05
print(f'New salary: ${cal:,.2f}\nChange: {(cal/be_salary - 1):.2%}')
