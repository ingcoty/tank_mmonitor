import time
from sr04t import Srt04t


sensor = Srt04t(triger_pin=13, echo_pin=12)

while True:
    pulse = sensor.read_distance()
    print(pulse)
    time.sleep(5)
