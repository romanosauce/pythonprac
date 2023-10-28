import itertools

def slide(seq, n):
    i = 0
    seq_copy = itertools.tee(seq)
    while True:
        seq_slice = itertools.islice(seq_copy[0], i, i+n)
        elem = next(seq_slice, None)
        if elem is not None:
            yield elem
            yield from seq_slice
        else:
            break
        seq_copy = itertools.tee(seq_copy[1])
        i += 1


import sys
exec(sys.stdin.read())
