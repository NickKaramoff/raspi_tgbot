#!/bin/sh

echo "Installing a systemd service..."

echo "[Unit]
Description=Start nick-raspi-01-bot

[Service]
Type=simple
ExecStart=/home/nick/.poetry/bin/poetry run raspi-01-bot
Restart=on-failure
WorkingDirectory=$(pwd)

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/nick-raspi-01-bot.service

systemctl start nick-raspi-01-bot
