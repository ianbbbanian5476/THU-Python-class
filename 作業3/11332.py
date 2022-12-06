while True:
    num = int(input())
    if num == 0:
        break
    while len([*str(num)]) != 1:
        num = sum(list(map(int,[*str(num)])))
    print(num)