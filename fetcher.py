from telethon import TelegramClient
import asyncio

# API عمومی تست تلگرام
api_id = 2040
api_hash = "b18441a1ff607e10a989891a5462e627"
session_name = "anon"

def fetch_messages(channel_username, limit=10):
    async def main():
        client = TelegramClient(session_name, api_id, api_hash)
        await client.start()
        messages = []
        async for message in client.iter_messages(channel_username, limit=limit):
            messages.append({
                "date": message.date.strftime("%Y-%m-%d %H:%M:%S"),
                "text": message.text or "[Media]"
            })
        await client.disconnect()
        return messages

    return asyncio.run(main())
