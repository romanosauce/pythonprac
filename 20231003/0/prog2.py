def rec(n):
    if n:
        print(n)
        rec(n - 1)
    return

rec(int(input()))
