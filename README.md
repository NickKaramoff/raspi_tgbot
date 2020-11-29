# raspi_tgbot

[![Latest release](https://badgen.net/github/release/NickKaramoff/raspi_tgbot/stable)][latest-release]
![Python 3.6-3.9 required](https://badgen.net/badge/python/3.6%20|%203.7%20|%203.8%20|%203.9/3776AB)

Utilitary Telegram Bot for Raspberry Pi

This bot can

- display it's global IP address (`/ip`)

## Prerequisities

- Python 3.6 or newer
  - make sure your `python3` executable points to the correct version  
    Tip: use [pyenv][pyenv] to simplify Python version management
- [Poetry][poetry] (strongly recommended, but not required)

## Install

1. Clone the repository and enter the downloaded folder

   ```sh
   # you can also download the archive from github manually
   git clone https://github.com/NickKaramoff/raspi_tgbot.git
   cd raspi_tgbot
   ```

2. Create poetry env and install the dependencies

   ```sh
   poetry env use python3
   poetry install --no-dev
   ```

   - if you're not using Poetry:

     ```sh
     pip install -r requirements.txt
     ```
     
3. Create the `.env` file with the following settings

   ```dotenv
   BOT_TOKEN=??? # replace with your bot token
   ALLOWED_IDS=1234567,87654321 # comma-separated list of user ids
   ```

   - you get the bot token when you create a bot with [BotFather][botfather]
   - you can get user IDs of user by forwarding their messages to [GetIDs Bot][getidsbot]

3. _(optional)_ Create a systemd service file in
   `/etc/systemd/system/raspi_tgbot.service` with the following content:

   ```ini
   [Unit]
   Description=Start nick-raspi-01-bot

   [Service]
   Type=simple
   WorkingDirectory=$(pwd)
   User=nick
   ExecStart=/home/nick/.poetry/bin/poetry run raspi-bot
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

   Then enable and run the service:

   ```sh
   sudo systemctl enable nick-raspi-01-bot
   sudo systemctl start nick-raspi-01-bot
   ```

[botfather]: https://t.me/BotFather
[getidsbot]: https://t.me/getidsbot
[latest-release]: https://github.com/NickKaramoff/raspi_tgbot/releases/latest
[poetry]: https://python-poetry.org/
[pyenv]: https://github.com/pyenv/pyenv
