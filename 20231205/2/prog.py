import asyncio


async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()
    i_b = start
    i_a1 = start
    i_a2 = middle
    while i_a1 < middle and i_a2 < finish:
        if A[i_a1] < A[i_a2]:
            B[i_b] = A[i_a1]
            i_a1 += 1
        else:
            B[i_b] = A[i_a2]
            i_a2 += 1
        i_b += 1
    while i_a1 < middle:
        B[i_b] = A[i_a1]
        i_a1 += 1
        i_b += 1

    while i_a2 < finish:
        B[i_b] = A[i_a2]
        i_a2 += 1
        i_b += 1

    event_out.set()


async def mtasks(A):
    new_A = A.copy()
    B = [_ for _ in range(len(A))]

    events = [asyncio.Event() for _ in range(len(A)+1)]
    tasks = []
    for event in events:
        event.set()

    step = 1
    flag = True

    while step < len(new_A):
        new_events = []
        event_ind = 0
        cur_ind = 0

        while cur_ind < len(A):
            start = cur_ind
            finish = min(cur_ind + step * 2, len(A))
            middle = min(start + step, len(A))
            new_events.append(asyncio.Event())
            tasks.append(asyncio.create_task(merge(new_A, B,
                                                   start,
                                                   middle,
                                                   finish,
                                                   events[event_ind],
                                                   events[event_ind+1],
                                                   new_events[-1])))
            event_ind += 2
            cur_ind += step * 2

        new_A, B = B, new_A
        step *= 2
        flag = not flag
        new_events.append(new_events[-1])
        events = new_events
    return tasks, new_A

import sys
exec(sys.stdin.read())
