#!/bin/sh

echo "Installing dependencies..."
poetry install

echo "Installing the systemd service..."

echo "[Unit]
Description=Start nick-raspi-01-bot

[Service]
Type=simple
ExecStart=/home/nick/.poetry/bin/poetry run raspi-01-bot
Restart=on-failure
WorkingDirectory=$(pwd)

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/nick-raspi-01-bot.service

echo "Enabling the systemd service..."
systemctl enable nick-raspi-01-bot

echo "Starting the systemd service..."
systemctl start nick-raspi-01-bot

echo "Installation complete!"
echo "Type 'sudo journalctl -u nick-raspi-01-bot' to see the logs"
