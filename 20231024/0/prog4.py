from itertools import repeat


def travel(n):
    yield from repeat("Po Kochkam", n)
    return "I v yamu"

def travelwrap(n):
    res = yield from travel(n)
    yield res
