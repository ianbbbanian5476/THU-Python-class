while True:
    n = input()
    if n == '':
        break
    n = int(n)
    count = n
    if n % 3 != 0:
        n = (n//3 + 1) * 3
    count += n//3
    n = n//3
    while n >= 3:
        if n % 3 != 0:
            n = (n//3 + 1) * 3
        count += n//3
        n = n//3
    print(count)
