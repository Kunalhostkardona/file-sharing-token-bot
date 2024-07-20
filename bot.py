from pyrogram import Client, errors
import logging

# Your existing imports and code
# ...

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Bot(Client):
    async def start(self):
        await super().start()
        logger.info("Bot started.")
    
    async def stop(self, *args):
        await super().stop()
        logger.info("Bot stopped.")

    # Custom error handler
    async def on_error(self, event, err):
        if isinstance(err, errors.FloodWait):
            logger.warning(f"Sleeping for {err.x} seconds due to FloodWait")
            await asyncio.sleep(err.x)
        elif isinstance(err, errors.RPCError):
            logger.error(f"RPCError: {err.MESSAGE}")
        else:
            logger.exception(f"Unexpected error: {err}")

if __name__ == "__main__":
    bot = Bot("my_account")
    bot.run()
