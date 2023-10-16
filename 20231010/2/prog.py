from math import *

def make_func(src):
    def func(x):
        return eval(src)
    return func

def print_screen(screen):
    print('\n'.join([''.join(s) for s in screen]))

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

data = input().split()
w = int(data[0])
h = int(data[1])
a, b = int(data[2]), int(data[3])

func = make_func(data[4])

screen = [[' '] * w for i in range(h)]

func_range = []
for i in range(w):
    x = scale(0, w-1, a, b, i)
    func_range += [func(x)]
y_scale_min, y_scale_max = min(func_range), max(func_range)

if isclose(y_scale_min, y_scale_max):
    y_scale_min -= 10
    y_scale_max += 10
x_prev, y_prev = 0, int(scale(y_scale_min, y_scale_max, h-1, 0, func_range[0]))

for i in range(1, w):
    x, y = i, int(scale(y_scale_min, y_scale_max, h-1, 0, func_range[i]))
    # mirror y axis, be careful with drawing direction and comparison (not intuitial, to prevent overdrawing, y+1 was added)
    if y_prev > y:
        _y, _y_prev = y_prev, y + 1
    else:
        _y, _y_prev = y, y_prev
    for j in range(_y_prev, _y):
        screen[j][x_prev] = '*'
    screen[y][x] = '*'
    x_prev, y_prev = x, y

print_screen(screen)
