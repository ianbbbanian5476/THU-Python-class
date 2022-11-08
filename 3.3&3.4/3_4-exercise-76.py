al = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
origin = ['Connecticut','Delaware','Georgia','Maryland','Massachusetts','New Hampshire','New Jersey','New York','North Carolina','Pennsylvania','Rhode Island','South Carolina','Virginia']
ans = []
finnal = []
file = open('States.txt','r')
for line in file:
    if line in origin:
        ans.append(line)

for a in al:
    for an in ans:
        if an.startswith(a):
            finnal.append(an)
print(finnal)