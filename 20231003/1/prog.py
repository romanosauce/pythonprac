def Pareto(*par):
    res = []
    for i in par:
        for j in par:
            if i[0] <= j[0] and i[1] <= j[1] and (i[0] < j[0] or i[1] < j[1]):
                break
        else:
            res.append(i)
    return tuple(res)

print(Pareto(*eval(input())))
