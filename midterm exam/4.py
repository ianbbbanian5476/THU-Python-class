num = int(input())
if num == 0:
    pass
else:
    binary = ''
    while num != 1:
        binary = str(num % 2) + binary
        num //= 2
    binary = '1' + binary
    binary = [*binary]
    count = 0
    for i in binary:
        if i == '1':
            count += 1
    print(f'The parity of {num} is {count} (mod 2)')

