zhi_yin_shu = [2,3,5,7,11,13,17,19]
test = int(input())
check = 0
double_check = 0
if test in zhi_yin_shu:
    pass
else:
    for i in zhi_yin_shu:
        if test % i == 0:
            check = 1
if check == 0:
    backward = ''
    for j in [*str(test)]:
        backward = j + backward

    if backward in zhi_yin_shu:
        pass
    else:
        for k in zhi_yin_shu:
            if int(backward) % k == 0:
                double_check = 1

if check == 0 and double_check == 0:
    print(f'{test} is emirp.')
elif check == 0:
    print(f'{test} is prime.')
else:
    print(f'{test} is not prime.')