eq = input()
a, b = eval(input())
print(eval(eq, {'x':a,'y':b}))
print(eval(eq, {'y':a,'x':b}))
