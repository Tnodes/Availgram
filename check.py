import asyncio
import aiohttp
from telegram import Bot
from telegram.ext import Application

# Telegram bot token and chat ID
BOT_TOKEN = 'xxxx:xxxx'
CHAT_ID = 'xxxx'

async def send_telegram_message(message):
    app = Application.builder().token(BOT_TOKEN).build()
    await app.bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"Message sent to Telegram: {message}")

async def check_local_health():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.head("http://localhost:7000/health") as response:
                if response.status == 200:
                    await send_telegram_message(f"AVAIL NODE\nYour nodes status is NORMAL! 🙂")
                else:
                    await send_telegram_message(f"AVAIL NODE\nYour nodes status is not good! 😵‍💫, Status code: {response.status}")
    except Exception as e:
        await send_telegram_message(f"An error occurred while checking local health: {str(e)}")
        print(f"Error occurred: {str(e)}")

async def main():
    while True:
        await check_local_health()
        await asyncio.sleep(18000)  # Sleep for 5 hours

if __name__ == "__main__":
    asyncio.run(main())
