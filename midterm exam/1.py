#通過預設測試資料
for i in range(int(input())):
    a, b, c, d = input().split(' ')
    a, b, c, d = int(a), int(b), int(c), int(d)
    count = 0
    while a != c or b != d:
        if a == 0 and a + b == 0:
            b += 1
            count += 1
        elif b != 0:
            a += 1
            b -= 1
            count += 1
        else: 
            a += 1
            b = a
            a = 0
            count += 1
    print(f'Case {i+1}: {count}')

    

