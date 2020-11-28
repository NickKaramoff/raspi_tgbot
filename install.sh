#!/bin/sh

/home/nick/.poetry/bin/poetry env use /home/nick/.pyenv/shims/python3

echo "Installing dependencies..."
/home/nick/.poetry/bin/poetry install --no-dev

echo "Installing the systemd service..."

sudo echo "[Unit]
Description=Start nick-raspi-01-bot

[Service]
Type=simple
WorkingDirectory=$(pwd)
User=nick
ExecStart=/home/nick/.poetry/bin/poetry run raspi-bot
Restart=on-failure

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/nick-raspi-01-bot.service

echo "Enabling the systemd service..."
sudo systemctl enable nick-raspi-01-bot

echo "Starting the systemd service..."
sudo systemctl start nick-raspi-01-bot

echo "Installation complete!"
echo "Type 'sudo journalctl -u nick-raspi-01-bot' to see the logs"
