import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import displayio
import adafruit_displayio_ssd1306
import time
import neopixel

key_pins = [board.D10, board.D9, board.D8, board.D7, board.D6, board.D3]

keys = []
for pin in key_pins:
    key = digitalio.DigitalInOut(pin)
    key.direction = digitalio.Direction.INPUT
    key.pull = digitalio.Pull.UP
    keys.append(key)

board = Keyboard(usb_hid.devices)

#will change to useful macros later
key_mapping = {
    0: Keycode.A,
    1: Keycode.B,
    2: Keycode.C,
    3: Keycode.D,
    4: Keycode.E,
    5: Keycode.F,
}

i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
#may add a fancy bitmap here in the future
display.fill(0)
display.text("hackpad!", 0, 0, 1)
display.show()
  
pixels = neopixel.NeoPixel(board.D0, 16)
pixels.brightness = .5

while True:
    for i in range(len(keys)):
        if keys[i].value: 
            board.send(key_mapping[i])
    pixels.fill((255, 255, 255))
    #will change to a cooler rgb pattern but I want to get it working first
    time.sleep(0.1)