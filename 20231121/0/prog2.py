with open("in", "rt") as f:
    data = f.read()
    print(data[len(data)//3:])
    i = len(data) // 3
    while data[i] != '\n':
        print(data[i], end='')
        i += 1
    print(data[i], end='')
