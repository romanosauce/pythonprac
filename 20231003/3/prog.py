from math import *

def Calc(s, t, u):
    def f1(x):
        return eval(s)
    def f2(x):
        return eval(t)
    def f(z):
        x = f1(z)
        y = f2(z)
        return eval(u)
    return f

F = Calc(*eval(input()))
print(F(eval(input())))
