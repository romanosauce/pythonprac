template = input().split()
while True:
    match input():
        case f if 'yes' in f:
            print("case 1")
        case f if f == template[1]:
            print('case 2')
        case f if f[0:len(template[2])] == template[2] and f[-len(template[1]):-1] == template[1]:
            print('case 3')
