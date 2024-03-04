import asyncio
import time

# import aiohttp

g = 0


async def some_func(i: int):
    global g

    await asyncio.sleep(0.1)
    g += 1
    print(g)
    print(f"some_func-{i} started...")
    await asyncio.sleep(3)
    print(f"some_func-{i} still processing...")
    await asyncio.sleep(3)
    print(f"some_func-{i} finished...")
    # await aiohttp.get("http://url")

    return f"async - {i}"


async def target(a: int):
    print(a)
    await asyncio.sleep(1)
    print(a)
    res = await some_func(-1)
    print(res)


def gener1():
    ...  # sleep(1)
    yield 10
    ...  # sleep(1)
    yield 11
    ...  # sleep(1)
    yield 12


# def gener2():
#     ...  # sleep(1)
#     yield 20
#     ...  # sleep(1)
#     yield 21
#     ...  # sleep(1)
#     yield 22
#
#
# g1 = gener1()
# g2 = gener2()
#
# next(g1)
# next(g2)
# sleep(1)
# next(g1)
# next(g2)
# sleep(1)
# next(g1)
# next(g2)
# sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(target(1))
    gather = asyncio.gather(
        some_func(2),
        some_func(3),
        some_func(4),
        some_func(5),
    )
    # input("")
    cur = time.time()
    loop.run_until_complete(gather)
    end = time.time() - cur
    input("[MAIN] >>>")
    print(end)
    print(g)
