from OTA_Wrapper import OTA_Wrapper
from wifi_config import SSID, PASSWORD
from time import sleep
from umqttsimple import MQTTClient
import network
import machine

BROKER="broker.hivemq.com"


def connect_wifi():
    """ Connect to Wi-Fi."""

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(SSID, PASSWORD)
    while not sta_if.isconnected():
        print('.', end="")
        sleep(0.25)
    print(f'Connected to WiFi, IP is: {sta_if.ifconfig()[0]}')


def process_message(topic, msg):
    print(msg)


connect_wifi()

client_id = "ESP32_TankMonitor"
mqtt_client = MQTTClient(client_id, BROKER)
mqtt_client.set_callback(process_message)
mqtt_client.connect()
mqtt_client.subscribe("mqtt-github-action/tank_monitor")

while True:
    print("waiting for a github push...")
    sleep(5)


#ota = OTA_Wrapper(github_url="https://github.com/ingcoty/tank_mmonitor.git")


