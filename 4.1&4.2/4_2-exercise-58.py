numbers = [865,1169,1208,1243,290]
sum_numbers = []
result = []
for i in numbers:
    b = [*str(i)]
    i = list(map(int,b))
    sum_numbers.append(i)
sorted_sum_numbers = sorted(sum_numbers,key=sum)
for k in sorted_sum_numbers:
    j = list(map(str,k))
    result.append(''.join(j))
print(result)
