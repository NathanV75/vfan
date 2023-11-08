#!/bin/bash
set -e

if [ "$EUID" -ne 0 ]; then
    echo "This requires root. Exiting without doing anything..."
    exit
fi
#copy python script
cp vfan.py /usr/local/bin/vfan.py
chmod +x /usr/local/bin/vfan.py

#install dependencies
pip install -r requirements.txt

#copy systemd service file
cp vfan.service /etc/systemd/system/vfan.service

#start and enable service
systemctl daemon-reload
systemctl start vfan
systemctl enable vfan