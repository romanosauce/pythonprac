sum = 0
while sum <= 21:
    a = int(input())
    if a > 0:
        sum += a
    else:
        print(a)
        break
else:
    print(sum)
