def addf(f, g):
    return lambda x: f(x) + g(x)

f = addf(bin, str)
print(f(1234))
