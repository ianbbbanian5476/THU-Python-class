import string

file = open('Q2_Input.txt', 'r')
Line = file.readlines()
count = 0
for line in Line:
    word_is_ = line.split('is')
    count += len(word_is_) - 1

print(count)
