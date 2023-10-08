def subtr(obj1, obj2):
    if isinstance(obj1, tuple | list):
        res = [i for i in obj1 if i not in obj2]
        return type(obj1)(res)
    else:
        return obj1 - obj2

print(subtr(*eval(input())))
