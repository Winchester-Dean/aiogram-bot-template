import asyncio
import os

from dispatcher import dp, bot

import handlers

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    asyncio.run(main())
