change = int(input())
count = 0
for i in range(change//50+1):
    for j in range((change-i*50)//25+1):
        for k in range((change-i*50-j*25)//10+1):
            for l in range((change-i*50-j*25-k*10)//5+1):
                count += 1
print(count)