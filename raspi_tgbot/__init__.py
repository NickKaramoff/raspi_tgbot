import argparse
import os
import sys

from colorama import init

from .bot import _run_bot

__version__ = "1.1.0"

init()


def __main():
    if not os.name == "posix":
        sys.exit("Only POSIX systems are supported")

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
