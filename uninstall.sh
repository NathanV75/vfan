#!/bin/bash
set -e

if [ "$EUID" -ne 0 ]; then
    echo "This requires root. Exiting without doing anything..."
    exit
fi

# stop and disable service
systemctl stop vfan
systemctl disable vfan


# remove systemd service file
rm /etc/systemd/system/vfan.service
systemctl daemon-reload

# remove python script
rm /usr/local/bin/vfan.py

# warn about python dependencies
echo "This script does not automatically uninstall python depenancies as they may be used by other programs."

echo "Sucessfully uninstalled."
