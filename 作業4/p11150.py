#while True:
#    n = input()
#    if n == '':
#        break
#    n = int(n)
#    count = n
#    if n % 3 != 0:
#        n = (n//3 + 1) * 3
#    count += n//3
#    n = n//3
#    while n >= 3:
#        if n % 3 != 0:
#            n = (n//3 + 1) * 3
#        count += n//3
#        n = n//3
#    print(count)


def iszhengwei(s:str):
    s = s.split(' ')
    #if s == 'zhengwei':
    #    return True
    return s

print(iszhengwei(5))



