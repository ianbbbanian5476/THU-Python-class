i,j = input().split(' ')
maxi = 0
for num in range(int(i),int(j)+1):
    count = 1
    while num != 1:
        if num % 2 == 1:
            num = 3 * num + 1
            count += 1
        else:
            num /= 2
            count += 1
    if count > maxi:
        maxi = count
print(i,j,maxi)