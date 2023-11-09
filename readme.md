# vfan
Variable fan speed using PWM for Raspberry Pi. Installs as a systemd service.

Note: this uses BCM pin 18 for Hardware PWM by default.

## Installation
To install vfan as a systemd service use the following steps.
1. Run `vfan.py` with `python3 ./vfan.py`.
1. Adjust parameters like FAN_GPIO and PWM_FREQ and restart the script as needed.
1. When you are happy with the settings `sudo ./install.sh`.
1. That's it, vfan should now be running as a service.

> Note: FAN_GPIO must be a GPIO that supports Hardware PWM

## Uninstallation
To remove vfan use the following steps.
1. Run `sudo ./uninstall.sh`.
1. Manually uninstall unwanted python depenancies. See requirements.txt for what was isntalled. Note some depenancies may be used by other software.
1. That's it. vfan should now be completely removed.