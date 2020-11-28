import logging

from telegram.ext import CommandHandler, Updater

from .commands import start

updater = Updater(
    token="1423516108:AAEFeFpyd9Q3Ki_zM0AW-hSm1ADPV8BlWBo", use_context=True
)
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
