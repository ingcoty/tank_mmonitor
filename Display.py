from ssd1306 import SSD1306_I2C
from machine import SoftI2C
from machine import Pin

class Display:

    def __init__(self):
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        self.display = SSD1306_I2C(128, 32, i2c)

    def text(self, msj:str):
        self.display.fill(0)
        self.display.text(msj, 0, 0, 1)
        self.display.show()