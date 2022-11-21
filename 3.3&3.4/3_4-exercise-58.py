vowel = ['a','e','i','o','u']
word = input('Input the word:')
word = [*word]
check = 0
for i in word:
    if i in vowel:
        check += 1
if check == 5:
    print('true')
else:
    print('false')
