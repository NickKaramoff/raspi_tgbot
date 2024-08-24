import logging
from json import JSONDecodeError
from pathlib import PosixPath
from typing import Dict

import ujson

CONFIG_PATH = PosixPath.home() / ".config" / "raspi_tgbot.json"

logger = logging.getLogger("raspi_tgbot")


def __get_config_json() -> Dict:
    try:
        with CONFIG_PATH.open("r") as fp:
            return ujson.load(fp)
    except FileNotFoundError:
        CONFIG_PATH.touch()
    except PermissionError:
        logger.warning(f"Can't access the config file at {str(CONFIG_PATH)}")
    except JSONDecodeError:
        logger.error(f"Can't decode JSON in {str(CONFIG_PATH)}")
    finally:
        return {}


def __write_config_json(json: dict) -> None:
    try:
        fp = CONFIG_PATH.open('w')
    except FileNotFoundError:
        fp = CONFIG_PATH.open('x')
    except PermissionError:
        exit(f"Can't access the config file at {str(CONFIG_PATH)}")

    if fp is not None

    try:
        ujson.dump(json, fp)

    try:
        with CONFIG_PATH.open("w") as fp:
            return ujson.dump(json, fp)
    except FileNotFoundError:
        CONFIG_PATH.touch()
    except PermissionError:
        logger.warning(f"Can't access the config file at {str(CONFIG_PATH)}")
    except JSONDecodeError:
        logger.error(f"Can't decode JSON in {str(CONFIG_PATH)}")
    finally:
        return {}


def _read_from_config(key: str) -> str:
    return __get_config_json().get(key)

def _write_to_config(key: str, value: str) -> None:
    if not CONFIG_PATH.exists():
        CONFIG_PATH.touch()

    with CONFIG_PATH.open('r') as fp:
        current_config =


def _list_config() -> None:
    for key, val in __get_config_json().items():
        print(f"{key}={val}")
