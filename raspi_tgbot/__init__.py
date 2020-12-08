import argparse

from .bot import _run_bot

__version__ = "1.1.0"


def __main():
    parser = argparse.ArgumentParser(
        "raspi_tgbot",
        description="Utilitary Telegram Bot for Raspberry Pi",
        epilog="More docs at https://github.com/NickKaramoff/raspi_tgbot",
        add_help=True,
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.parse_args()

    _run_bot()


if __name__ == "__main__":
    __main()
