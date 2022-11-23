def count0(key : str, test : str):
    try:
        ram = test.split(key)
        count = len(ram) - 1
    except:
        count = 0
    return count

print(count0('a','aaabb'))
    #if key in test:
    #    ram = test.split(key)
    #    count = len(ram) - 1
    #else:
    #    count = 0
