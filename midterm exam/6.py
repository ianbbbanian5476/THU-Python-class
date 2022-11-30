teach_times = int(input())
dict_say = []
dict_res = []
for i in range(teach_times):
    say = dict_say.append(input())
    res = dict_res.append(input())

test_times = int(input())
for j in range(test_times):
    ask = input()
    print(dict_res[dict_say.index(ask)])
