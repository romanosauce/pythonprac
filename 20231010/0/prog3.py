from math import *
def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A


scr = [[' '] * 60 for i in range(20)]
for j in range(0, 20000):
    s = j * 0.01
    for i in range(0, 60):
        x = scale(59, 0, -5, 5, i)
        scr[int(scale(-1, 1, 0, 19, sin(x+s)))][i] = '*'
    print('\n'.join([''.join(s) for s in scr]))
    scr = [[' '] * 60 for i in range(20)]
