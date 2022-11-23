#已通過測資系統
while True:
    try:
        num = input().split(' ')
    except:
        break
    print(f'{abs(int(num[0])-int(num[1]))}')