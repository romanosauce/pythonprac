l = []
while a := input():
    a = eval(a)
    l.append(a)

w = len(l)
if all([len(el) == w for el in l]):
    l = [[a[i] for a in l] for i in range(len(l[0]))]
    for a in l:
        print(*a)
else:
    print("Wrong size")
