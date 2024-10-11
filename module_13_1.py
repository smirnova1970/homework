import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}-й шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    strong1 = asyncio.create_task(start_strongman('Pasha', 3))
    strong2 = asyncio.create_task(start_strongman('Denis', 4))
    strong3 = asyncio.create_task(start_strongman('Apollon', 5))
    await strong1, strong2, strong3


asyncio.run(start_tournament())
