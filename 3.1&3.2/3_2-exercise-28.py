nums = int(input('Enter number of copies: '))
if nums > 100:
    other = nums - 100
    nums = 100
else:
    other = 0
print(f'Cost is ${((nums * 5 + other * 3)/100):.2f}')