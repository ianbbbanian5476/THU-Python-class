#已通過測資系統
for i in range(int(input())):
    a, b = input().split(' ',1)
    b = b.split(' ')
    b = list(map(int,b))
    b = sorted(b)
    z = b[int(a)//2]
    d = 0
    for k in b:
        d += abs(k-z)
    print(d)