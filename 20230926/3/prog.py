row = list(eval(input()))
w = len(row)
m1 = [row]
for i in range(1, w):
    row = list(eval(input()))
    m1.append(row)
m2 = []
for i in range(w):
    row = list(eval(input()))
    m2.append(row)
m3 = []
for i in range(w):
    m3.append([])
    for j in range(w):
        el = 0
        for k in range(w):
            el += m1[i][k] * m2[k][j]
        m3[i].append(el)
for row in m3:
    for i in range(len(row)):
        print(row[i], ',' if i != len(row) - 1 else '', sep='', end='')
    print()
