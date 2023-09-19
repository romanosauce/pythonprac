while a := input():
    a = eval(a)
    if a % 2 == 0:
        print(a)
    if a == 13:
        break
else:
    print('CONGRATS')
