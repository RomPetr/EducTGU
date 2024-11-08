import asyncio

"""
# Веб приложение доступа к ChatGPT
from g4f.gui import run_gui
run_gui()
"""

"""
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print('Начало')
    await say_after(1, 'Привет')
    await say_after(2, 'Мир')
    print('Конец')
asyncio.run(main())
"""

async def first_function(delay, name):
    print(f"{name} начала выполнение")
    await asyncio.sleep(delay)
    print(f"{name} завершила выполнение")

async def main():
    await  asyncio.gather(
        first_function(5, 'Первая функция'),
        first_function(2, 'Вторая функция')
    )
asyncio.run(main())