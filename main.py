from OTA_Wrapper import OTA_Wrapper
from wifi_config import SSID, PASSWORD
from time import sleep
import network

def connect_wifi():
    """ Connect to Wi-Fi."""

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(SSID, PASSWORD)
    while not sta_if.isconnected():
        print('.', end="")
        sleep(0.25)
    print(f'Connected to WiFi, IP is: {sta_if.ifconfig()[0]}')


connect_wifi()
ota = OTA_Wrapper(github_url="https://github.com/ingcoty/tank_mmonitor.git")
