def gfun():
    sum = 0
    i = 1
    while True:
        sum += 1 / (i * i)
        i += 1
        yield sum

