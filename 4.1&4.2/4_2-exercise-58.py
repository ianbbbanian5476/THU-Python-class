numbers = [865,1169,1208,1243,329]
sum_numbers = []
result = []
for i in numbers:
    i = [*str(i)]
    count = 0
    for j in i:
        count += int(j)
    sum_numbers.append(count)
sorted_sum_numbers = sorted(sum_numbers)
for k in sorted_sum_numbers:
    result.append(numbers[sum_numbers.index(k)])
print(result)
