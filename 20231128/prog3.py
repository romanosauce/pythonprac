while True:
    match input().split():
        case ['mov', s1, s2]:
            print(f'moving {s2} to {s1}')
        case ['push' | 'pop' as cmd, *reglist]:
            print(f'{cmd}ing', *reglist)
        case [s1, s2]:
            print(f'making {s1} with {s2}')
        case _:
            print('Parse Error')
            break
