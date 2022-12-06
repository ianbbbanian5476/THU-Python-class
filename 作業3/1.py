r = []
c = []
fig_num = 0
while True:
    fig = input()
    fig_num += 1
    if fig == '*':
        break
    else:
        figs, fig_point = fig.split(' ',1)
        fig_point = list(map(float,fig_point.split(' ')))
        if figs == 'r':
            r.append(fig_point+[fig_num])
        if figs == 'c':
            c.append(fig_point+[fig_num])
point_num = 0
while True:
    point_x , point_y = map(float,input().split(' '))
    point_num += 1
    check = 0
    if point_x == 9999.9 and point_y == 9999.9:
        break
    for i in r:
        if point_x > i[0] and point_x < i[2]:
            if point_y > i[3] and point_y < i[1]:
                check = 1
                print(f'Point {point_num} is contained in figure {i[4]}')
    for j in c:
        delta_x,delta_y = abs(j[0] - point_x),abs(j[1] - point_y)
        d = (delta_x ** 2 + delta_y ** 2) ** 0.5
        if d < j[2]:
            check = 1
            print(f'Point {point_num} is contained in figure {j[3]}')
    if check == 0 :
        print(f'Point {point_num} is not contained in any figure')