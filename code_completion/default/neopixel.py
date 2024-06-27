'''
control of WS2812 / NeoPixel LEDs

This module provides a driver for WS2818 / NeoPixel LEDs.

Note:

	This module is only included by default on the ESP8266, ESP32 and RP2 ports.

	On STM32 / Pyboard and others, you can either install the neopixel package
	using mip, or you can download the module directly from micropython-lib and
	copy it to the filesystem.

[View Doc](https://docs.micropython.org/en/latest/library/neopixel.html)
[View neopixel.py](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/led/neopixel/neopixel.py)
'''
class NeoPixel(object):
	'''
	This class stores pixel data for a WS2812 LED strip connected to a pin.

	The application should set pixel data and then call `NeoPixel.write()` when
	it is ready to update the strip.
	'''
	def __init__(self, pin, n: int, *, bpp: int = 3, timing: int = 1):
		'''
		Construct an NeoPixel object. The parameters are:

		- `pin` is a machine.Pin instance.
		- `n` is the number of LEDs in the strip.
		- `bpp` is 3 for RGB LEDs, and 4 for RGBW LEDs.
		- `timing` is 0 for 400KHz, and 1 for 800kHz LEDs (most are 800kHz).
		'''

	# Pixel access methods
	def fill(self, pixel: tuple):
		'''
		Sets the value of all pixels to the specified `pixel` value (i.e. an
		RGB/RGBW tuple).
		'''

	def __len__(self) -> int:
		'''Returns the number of LEDs in the strip.'''

	def __setitem__(self, index: int, val: tuple):
		'''Set the pixel at `index` to the value, which is an RGB/RGBW tuple.'''

	def __getitem__(index: int) -> tuple:
		'''Returns the pixel at `index` as an RGB/RGBW tuple.'''

	# Output methods
	def write():
		'''Writes the current pixel data to the strip.'''
