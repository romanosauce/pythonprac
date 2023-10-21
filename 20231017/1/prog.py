line = input().lower()
line = [c if c.isalpha() else ' ' for c in line]
line = ''.join(line).split()
freq = set()
for word in line:
    for i in range(len(word)-1):
        freq |= {word[i:i+2]}

print(len(freq))
