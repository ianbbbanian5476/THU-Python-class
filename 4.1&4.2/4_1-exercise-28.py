num = int(input('Enter a positive integer: '))
result = 1
for i in range(1,num+1):
    result *= i
print(f'{num}! is {result}')
