from collections import Counter

w = int(input())

freq_tab = Counter()
while (line := input().lower()):
    line = filter(lambda x: len(x) == w,
                  ''.join([c if c.isalpha() else ' ' for c in line]).split())
    freq_tab.update(Counter(line))

if len(freq_tab):
    max_val = freq_tab.most_common(1)[0][1]
    print(*sorted([key for key, value in freq_tab.items() if value == max_val]))
