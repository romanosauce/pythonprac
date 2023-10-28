import itertools as it

print(*sorted(list(map(lambda x: ''.join(x), filter(lambda x: ''.join(x).count('TOR') == 2, it.product('TOR', repeat=int(input())))))), sep=', ')
