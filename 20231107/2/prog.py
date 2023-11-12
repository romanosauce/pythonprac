class InvalidInput(Exception):
    def __init__(self):
        super().__init__('Invalid input')


class BadTriangle(Exception):
    def __init__(self):
        super().__init__('Not a triangle')


def triangleSquare(coords):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(coords)
    except Exception:
        raise InvalidInput

    try:
        area = 1/2 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    except Exception:
        raise BadTriangle

    if area == 0:
        raise BadTriangle
    return area


while True:
    data = input()
    try:
        area = triangleSquare(data)
    except InvalidInput as inv:
        print(inv)
    except BadTriangle as bad:
        print(bad)
    else:
        print(f"{area:.2f}")
        break
