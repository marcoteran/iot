import os

print(os.popen("ifconfig wlan0").read())