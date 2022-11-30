num = []
while True:
    try:
        a = int(input())
    except:
        break
    num.append(a)
    num = sorted(num)
    if len(num) % 2 == 0:
        print((num[len(num)//2]+num[len(num)//2-1])//2)
    else:
        print(num[len(num)//2])