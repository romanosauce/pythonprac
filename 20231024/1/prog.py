def fib(m, n):
    el_1 = 1
    el_2 = 1
    for i in range(m):
        new_el = el_1 + el_2
        el_1, el_2 = el_2, new_el
    for i in range(n):
        yield el_1
        new_el = el_1 + el_2
        el_1, el_2 = el_2, new_el


import sys
exec(sys.stdin.read())
