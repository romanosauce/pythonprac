arr = eval(input())
arr = list(arr)
i = 1
while i < len(arr):
    j = i
    while j > 0 and arr[j-1] ** 2 % 100 > arr[j] ** 2 % 100:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1
    i += 1
print(arr)
