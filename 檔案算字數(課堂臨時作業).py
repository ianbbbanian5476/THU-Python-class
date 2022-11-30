import string

file = open('gettysburg.txt', 'r')
Line = file.readlines()
word = {}
count = 0
for line in Line:
    for i in line:
        if i in string.punctuation:
            i = ' '
    word1 = line.split(' ')
    for k in word1:
        if k not in word.keys():
            word[k] = 1
        else:
            word[k] += 1

print(word)
print(f'全部的單字數：{sum(word.values())}\n全部的不重複字數：{len(word.keys())}\n最頻繁出現的單字{max(word, key=word.get)}')
