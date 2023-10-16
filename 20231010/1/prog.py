from fractions import Fraction

def check(*args):
    data = [Fraction(str(elem)) for elem in args]
    s = data[0]
    w = data[1]
    deg_a = int(data[2])
    coef_a = data[3:4+deg_a]
    deg_b = int(data[4+deg_a])
    coef_b = data[5+deg_a:6+deg_a+deg_b]

    numerator = 0
    for i in range(deg_a, -1, -1):
        numerator += s ** i * coef_a[deg_a-i]
    denum = 0
    for i in range(deg_b, -1, -1):
        denum += s ** i * coef_b[deg_b-i]

    return numerator / denum == w if denum else False


data = input().split(',')
print(check(*data))
