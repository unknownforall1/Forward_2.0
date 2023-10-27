from pyrogram import Client, __version__

from config import Config
from config import LOGGER

from user import Bot
import pyromod.listen


class Bot(Client):
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            Config.BOT_SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={
                "root": "plugins"
            },
            workers=10,
            bot_token=Config.BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        me = await self.get_me()
        await self.send_message(chat_id=TO_CHANNEL, text=STARTED)

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")
