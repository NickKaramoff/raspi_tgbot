import logging
import os

from dotenv import load_dotenv
load_dotenv()

from telegram.ext import CommandHandler, Updater

from .commands import start

updater = Updater(token=os.getenv("BOT_TOKEN", ""), use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


dispatcher.add_handler(CommandHandler("start", start))


def main():
    updater.start_polling()


if __name__ == "__main__":
    main()
