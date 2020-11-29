import logging
import os

from dotenv import load_dotenv

load_dotenv()

from telegram.ext import CommandHandler, Updater

from .commands import start, get_ip

updater = Updater(token=os.getenv("BOT_TOKEN", ""), use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("ip", get_ip))


def main():
    updater.start_polling()
    updater.idle()
    exit(0)


if __name__ == "__main__":
    main()
