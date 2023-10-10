from decimal import Decimal

def esum(N, one):
    res = type(one)(1)
    fact = one
    for i in range(1, N+1):
        fact = fact * i
        res += 1/fact
    print(1)
    return res
