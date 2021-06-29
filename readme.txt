Install and run pigpiod:
http://abyz.me.uk/rpi/pigpio/download.html

Add to crontab -e:
* * * * * ~/workspace/vfan/vfan.sh >/dev/null 2>&1
