first = eval(input("Enter cost of first suit: "))
second = eval(input("Enter cost of second suit: "))
print(f'Cost of the two suit is ${min([first,second]) * 0.5 + max([first,second]):.2f}')