def walk2d():
    x, y = 0, 0
    dx, dy = yield x, y
    while True:
        x += dx
        y += dy
        dx, dy = yield x, y
