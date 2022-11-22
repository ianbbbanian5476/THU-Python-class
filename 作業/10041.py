for i in range(int(input())):
    a, b = input().split(' ',1)

    b = b.split(' ')
    b = list(map(int,b))
    b = sorted(b)
    print(b)
    print(b[round(int(a)/2)-1])