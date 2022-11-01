consonants = ['p','b','th','t','d','k','ge','g','m','ng','n','f','v','sh','s','z','ch','j','w','r','l','y','h']
vowel = ['a','e','i','o','u']
str1 = input('Enter word to translate: ')
check = 0
for i in consonants:
    if str1.startswith(i):
        tran = str1[len(i):]
        translate = tran + i + 'ay'
        check = 1
if check == 0:
    for j in vowel:
        if str1.startswith(j):
            translate = str1 + 'way'
print(f'The word in Pig Latin is {translate}.')
