import asyncio

event = asyncio.Event()


async def writer(queue, delay):
    await asyncio.sleep(delay)
    i = 0
    while not event.is_set():
        await queue.put(f"{i}_{delay}")
        i += 1
        await asyncio.sleep(delay)


async def stacker(queue, stack):
    while not event.is_set():
        await asyncio.sleep(0)
        item = await queue.get()
        await stack.put(item)


async def reader(stack, quantity, delay):
    await asyncio.sleep(delay)
    i = 0
    while i < quantity:
        item = await stack.get()
        print(item)
        i += 1
        await asyncio.sleep(delay)
    event.set()


async def main(delay1, delay2, delay3, quantity):
    queue = asyncio.Queue(0)
    stack = asyncio.LifoQueue(0)
    await asyncio.gather(
        writer(queue, delay1),
        writer(queue, delay2),
        stacker(queue, stack),
        reader(stack, quantity, delay3))

asyncio.run(main(*eval(input())))
