class Triangle:
    def __init__(self, *coords):
        self.coords = coords
        self.area = round(abs(0.5 * ((self.coords[1][0] - self.coords[0][0]) *
                              (self.coords[2][1] - self.coords[0][1]) -
                              (self.coords[2][0] - self.coords[0][0]) *
                              (self.coords[1][1] - self.coords[0][1]))), 3)
        self.empty = False if self.area else True

    def __abs__(self):
        return self.area if self.area else 0

    def __bool__(self):
        return not self.empty

    def __lt__(self, obj):
        return self.area < obj.area

    def __contains__(self, obj):
        def vec_mult(ox, oy, x0, y0, x1, y1):
            return (x0 - ox) * (y1 - oy) - (x1 - ox) * (y0 - oy)

        def in_point(ox, oy, coords):
            return (vec_mult(ox, oy, *coords[0], *coords[1]) >= 0 and
                    vec_mult(ox, oy, *coords[1], *coords[2]) >= 0 and
                    vec_mult(ox, oy, *coords[2], *coords[0]) >= 0) or (
                    vec_mult(ox, oy, *coords[0], *coords[1]) <= 0 and
                    vec_mult(ox, oy, *coords[1], *coords[2]) <= 0 and
                    vec_mult(ox, oy, *coords[2], *coords[0]) <= 0)
        if not obj:
            return True
        return all([in_point(*obj.coords[0], self.coords),
                    in_point(*obj.coords[1], self.coords),
                    in_point(*obj.coords[2], self.coords)])

    def __and__(self, obj):
        if not self or not obj:
            return False
        if self in obj:
            return True
        for A, B in ((self.coords[0], self.coords[1]),
                     (self.coords[1], self.coords[2]),
                     (self.coords[2], self.coords[0])):
            for C, D in ((obj.coords[0], obj.coords[1]),
                         (obj.coords[1], obj.coords[2]),
                         (obj.coords[2], obj.coords[0])):
                x1, x2, a1, a2 = A[0], B[0], C[0], D[0]
                y1, y2, b1, b2 = A[1], B[1], C[1], D[1]
                A1 = y2 - y1
                B1 = x1 - x2
                C1 = y1*x2 - y2*x1
                A2 = b2 - b1
                B2 = a1 - a2
                C2 = b1*a2 - b2*a1
                sign1 = A1 * a1 + B1 * b1 + C1
                sign2 = A1 * a2 + B1 * b2 + C1
                sign3 = A2 * x1 + B2 * y1 + C2
                sign4 = A2 * x2 + B2 * y2 + C2
                if (sign1 == 0):
                    if min(x1, x2) <= a1 <= max(x1, x2) and \
                            min(y1, y2) <= b1 <= max(y1, y2):
                        return True
                if (sign2 == 0):
                    if min(x1, x2) <= a2 <= max(x1, x2) and \
                            min(y1, y2) <= b2 <= max(y1, y2):
                        return True
                if (sign3 == 0):
                    if min(a1, a2) <= x1 <= max(a1, a2) and \
                            min(b1, b2) <= y1 <= max(b1, b2):
                        return True
                if (sign4 == 0):
                    if min(a1, a2) <= x2 <= max(a1, a2) and \
                            min(b1, b2) <= y2 <= max(b1, b2):
                        return True
                if (sign1 > 0) != (sign2 > 0) and (sign3 > 0) != (sign4 > 0):
                    return True
        return False

import sys
exec(sys.stdin.read())
