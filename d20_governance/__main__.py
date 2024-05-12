import asyncio
import datetime

from d20_governance.bot import run_bot
from d20_governance.utils.constants import LOGGING_PATH
from d20_governance.utils.utils import clean_temp_files, check_dirs
from d20_governance.health_check import start_server  # Importar start_server desde health_check.py

async def main():
    try:
        check_dirs()
        fastapi_task = asyncio.create_task(start_server())
        discord_task = asyncio.create_task(run_bot())
        
        await asyncio.gather(fastapi_task, discord_task)
    finally:
        clean_temp_files()
        with open(f"{LOGGING_PATH}/bot.log", "a") as f:
            f.write(f"\n--- Bot stopped at {datetime.datetime.now()} ---\n\n")

if __name__ == "__main__":
    asyncio.run(main())