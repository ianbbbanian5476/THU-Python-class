balance = float(input('Enter current balence: '))
amount = float(input('Enter amount of withdrawal: '))
if balance - amount >= 0:
    print(f'The new balance is ${balance - amount:.2f}.')
    if balance - amount < 150:
        print("Balance below $150.")
else:
    print("Withdrawal denied.")