import argparse
import os
import sys

from colorama import init

from .bot import _run_bot
from .config import _list_config, _read_from_config, _write_to_config

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
    subparsers = parser.add_subparsers(title="subcommands", dest="command")

    config_parser = subparsers.add_parser(
        "config",
        description="Configuration management for raspi_tgbot",
        help="configuration management",
    )
    group = config_parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-l", action="store_true", help="list configuration", dest="list"
    )
    group.add_argument(
        "--set", nargs=2, help="set configuration value", metavar=("KEY", "VALUE")
    )
    group.add_argument("--get", help="read configuration value", metavar="KEY")

    args = parser.parse_args()

    if args.command is None:
        _run_bot()
    elif args.command == "config":
        if args.list:
            _list_config()
            return
        elif args.get:
            print(_read_from_config(args.get))
        elif args.set:
            _write_to_config(*args.set)

    print(args)

    # _run_bot()


if __name__ == "__main__":
    __main()
