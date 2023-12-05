import asyncio


async def squarer(x):
    return x**2

async def doubler(x):
    return 2 * x


async def main(param):
    res = await asyncio.gather(squarer(param[0]), squarer(param[1]))
    res = await asyncio.gather(doubler(res[0]), doubler(res[1]))
    print(*res)
