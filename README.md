# Tuxpad!
*A 6-key macropad with an OLED display, neopixel light bar, and circuitpython firmware, designed to simplify repetitive tasks.*

![rendering](https://i.imgur.com/r17VPHF.jpeg)
[PCB demo on KiCanvas](https://kicanvas.org/?repo=https%3A%2F%2Fgithub.com%2FJacobG-774%2Fhackpad%2Fblob%2Fmain%2FPCB%2Fhackpad.kicad_pcb)

**Features**

* Customizable macros to simplify productivity, gaming, or other workflows/applications
* RGB Neopixel bar for awesome customizable lighting
* OLED display for time, system information, or motivational messages

**Materials Used**

![schematic](https://i.imgur.com/mkDUquJ.png)

* Seeed XIAO RP2040 microcontroller - 1
* MX-style mechanical switches - 6
* 0.91” 128×32 OLED display - 1
* Blank DSA keycaps - 6
* SK6812 MINI-E RGB LEDs - 16
* M3×16mm screws - 4
In addition to the PCB and 3d printed case of course.


**How it Works**

![PCB](https://i.imgur.com/zED7hTH.png)

I decided on direct wiring for the switches as matrix wiring would add complication and more possible failure points to the design while only saving one pin (which I wouldn't need anyways). The Neopixel LEDs can be individually controlled through the firmware and allow for full and relatively simple customizability. 
My choice of CircuitPython without KMK for the firmware might seem counterintuitive, but this enables me to more easily base lighting patterns or displays on the LCD off key presses (for example, the neopixels change color every key press, or the LCD displays my total key press count for the day to keep me motivated). I also couldn't find any documentation for direct wiring, OLED, or LED support in KMK, so it wasn't a very viable option.

**Credits/Acknowledgements**

![case](https://i.imgur.com/iEhUcLl.png)

I'm happy to say I mostly designed my case and PCB with just the help of the Hackpad tutorial, Google, and my few brain cells. The rendering was made with the help of [ohagel](https://www.thingiverse.com/thing:738769) and [gcb](https://www.thingiverse.com/thing:421524)'s files on Thingiverse, and I used a small amount of AI and reverse engineering from [LyricSantana](https://github.com/LyricSantana/lyrics_macropad/tree/main)'s code for the firmware.



