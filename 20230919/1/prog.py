a = int(input())
cl = 0b0
if a % 25 == 0:
    if a % 2 == 0:
        cl |= 0b1
    else:
        cl |= 0b10
if a % 8 == 0:
    cl |= 0b100
print('A', '+' if cl & 0b1 else '-', 'B', '+' if cl & 0b10 else '-',
      'C', '+' if cl & 0b100 else '-')
