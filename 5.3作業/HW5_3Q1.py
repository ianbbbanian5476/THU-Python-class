import string

word = {}
count = 0
txt = input().lower().translate(str.maketrans('', '', string.punctuation))
for k in txt:
    if k == ' ':
        pass
    elif k not in word.keys():
        word[k] = 1
    else:
        word[k] += 1

maxvalue = word[max(word,key=word.get)]
maxkey = ''
while maxvalue in word.values():
    maxkey += max(word,key=word.get)
    word[max(word,key=word.get)] = 0
print(maxkey)