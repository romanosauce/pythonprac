import sys

seg_num = sys.stdin.buffer.read(1)[0]
in_data = sys.stdin.buffer.read()[:-1]          # get rid of newline

i = 0
res = []
st_i = end_i = 0
while i < len(in_data) and i < seg_num:
    st_i = max(end_i, int(i * len(in_data) / seg_num))
    end_i = max(st_i + 1, int((i + 1) * len(in_data) / seg_num))
    res += [in_data[st_i:end_i]]
    i += 1

res = [seg_num.to_bytes(1, 'big')] + sorted(res) + [b'\n']
sys.stdout.buffer.write(b''.join(res))
