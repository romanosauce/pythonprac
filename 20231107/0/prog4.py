from math import inf
def div_ab(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return inf

for i in ((10, 2), (1, 0), (9, 3)):
    print(div_ab(*i))
