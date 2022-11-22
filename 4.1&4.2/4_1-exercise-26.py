def count0(key : str, test : str):
    try:
        ram = test.split(key)
        count = len(ram) - 1
    except:
        count = 0
    return count

print(count0('aa','aaabb'))
k = split('hi guys',' ')
print(k)