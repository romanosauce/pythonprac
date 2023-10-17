text = input()

d = {}

for word in text.split():
    if d.get(word):
        d[word] += 1
    else:
        d[word] = 1

print(d)
