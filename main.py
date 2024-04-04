from OTA_Wrapper import OTA_Wrapper
from wifi_config import SSID, PASSWORD
from time import sleep
from Display import Display
from umqtt.simple import MQTTClient
import network
import machine
import time
from sr04t import Srt04t

BROKER="18.185.170.141"
REPOSITORY = "https://github.com/ingcoty/tank_mmonitor.git"

level_sensor = Srt04t(triger_pin=25, echo_pin=4)
display = Display()

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
    print("actualizando firmware")
    ota = OTA_Wrapper(github_url=REPOSITORY)

connect_wifi()

#process_message("","")

#add this comment to update github.

client_id = "ESP32_TankMonitor"
mqtt_client = MQTTClient(client_id, BROKER)
mqtt_client.set_callback(process_message)
mqtt_client.connect()
mqtt_client.subscribe("mqtt-github-action/tank_monitor")

while True:
    mqtt_client.check_msg()
    level = level_sensor.read_distance()
    print(level)
    display.text(f"Tank: {level} %")
    sleep(5)



