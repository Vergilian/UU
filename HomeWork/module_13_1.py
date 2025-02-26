import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for _ in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {_+ 1} шар')
    print(f'Силач {name} закончил соревнование')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())