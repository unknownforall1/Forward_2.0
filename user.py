from config import BOT_TOKEN, API_HASH, API_ID, BOT_USERNAME, TO_CHANNEL
from config import LOGGER
from pyrogram import Client, __version__
import asyncio
BOT_USERNAME=Config.BOT_USERNAME

class Bot(Client):
    def __init__(self):
        super().__init__(
            bot_token=BOT_TOKEN,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            workers=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        if BOT_USERNAME:
            await User.send_message(self, chat_id=BOT_USERNAME, text="/forward")
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
