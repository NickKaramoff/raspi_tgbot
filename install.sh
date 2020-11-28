#!/bin/sh

poetry env use $(which python3)

echo "Installing dependencies..."
poetry install --no-dev

echo "Installing the systemd service..."

echo "[Unit]
Description=Start nick-raspi-01-bot

[Service]
Type=simple
WorkingDirectory=$(pwd)
User=$(whoami)
ExecStart=$(which poetry) run raspi-bot
Restart=on-failure

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/nick-raspi-01-bot.service

echo "Enabling the systemd service..."
systemctl enable nick-raspi-01-bot

echo "Starting the systemd service..."
systemctl start nick-raspi-01-bot

echo "Installation complete!"
echo "Type 'sudo journalctl -u nick-raspi-01-bot' to see the logs"
