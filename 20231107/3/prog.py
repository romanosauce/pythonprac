class Undead(Exception):
    def __init__(self, arg='Generic Undead'):
        super().__init__(arg)


class Skeleton(Undead):
    def __init__(self):
        super().__init__('Skeleton')


class Zombie(Undead):
    def __init__(self):
        super().__init__('Zombie')


class Ghoul(Undead):
    def __init__(self):
        super().__init__('Ghoul')


def necro(a):
    ex = [Skeleton, Zombie, Ghoul]
    raise ex[a % 3]


x, y = eval(input())
for i in range(x, y):
    try:
        necro(i)
    except Skeleton:
        print('Skeleton')
    except Zombie:
        print('Zombie')
    except Undead:
        print('Generic Undead')
