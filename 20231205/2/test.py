size = 7
cur_ind = 0
step = 1
event_ind = 0
while cur_ind < size:
    start = cur_ind
    finish = min(cur_ind + step * 2, size)
    middle = start + step
    print(start, finish, middle, event_ind)
    event_ind += 2
    cur_ind += step * 2
