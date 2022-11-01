nums = int(input("Enter number of bagels: "))
if nums >= 6:
    cost = 60
else:
    cost = 75
print(f'Cost is ${cost * nums / 100:.2f}')