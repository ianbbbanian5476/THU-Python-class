case = int(input())
for t in range(case):
    input_times = int(input())
    scoreList = []
    check = 0
    for i in range(input_times):
        scoreList.append(int(input()))
    for j in range(1,len(scoreList)):
        if check == 0:
            maxi = scoreList[0] - scoreList[j]
            check = 1
        elif scoreList[0] - scoreList[j] > maxi:
            maxi = scoreList[0] - scoreList[j]
    print(maxi)



