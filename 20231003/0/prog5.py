def adders(n):
    res = []
    for i in range(n):
        def adder(x):
            return x + i
        res.append(adder)
    return res


