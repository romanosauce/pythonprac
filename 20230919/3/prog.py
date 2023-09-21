n = int(input())
i = n
while i < n + 3:
    j = n
    while j < n + 3:
        if sum(map(int, list(str(i * j)))) != 6:
            res = i * j
        else:
            res = ':=)'
        print(f"{i} * {j} = {res}", end=' ')
        j += 1
    print('')
    i += 1
