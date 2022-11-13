vowel = ['a','e','i','o','u']
word = input('Input the word:')
word = [*word]
check = 0
for i in word:
    if i in vowel:
        print('true')
        check = 1
        break
if check == 0:
    print('false')
