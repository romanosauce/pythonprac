a = eval(input())
for i in a:
    if i % 2:
        print(i)
        break
else:
    print(a[-1])
