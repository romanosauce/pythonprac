top = input()
w = len(top)
h = 1
gas = 0
liq = 0
while (cur_line := input()) and cur_line[1] != '#':
    if cur_line[1] == '.':
        gas += w - 2
    else:
        liq += w - 2
    h += 1

h += 1                  # last line
w, h = h, w
liq_num = liq // (w - 2)
if liq % (w - 2):
    liq_num += 1
gas_num = h - 2 - liq_num

print('#' * w)
for i in range(gas_num):
    print(f"#{'.'*(w-2)}#")
for i in range(liq_num):
    print(f"#{'~'*(w-2)}#")
print('#' * w)

frac_len = len(str(max(liq, gas))) + len(str(liq+gas)) + 1
if liq > gas:
    print(f"{'.' * round(20/liq*gas):<20} {str(gas)+'/'+str(liq+gas):>{frac_len}}")
    print(f"{'~' * 20} {str(liq)+'/'+str(liq+gas):>{frac_len}}")
else:
    print(f"{'.' * 20} {str(gas)+'/'+str(liq+gas):>{frac_len}}")
    print(f"{'~' * round(20/gas*liq):<20} {str(liq)+'/'+str(liq+gas):>{frac_len}}")
