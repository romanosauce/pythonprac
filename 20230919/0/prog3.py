a, b, c = eval(input())
# print(a > 0 and b > 0 and c > 0 and a < c + b and b < a + c and c < a + b)
print(min(a, b, c) > 0 and 2 * max(a, b, c) < a + b + c)
