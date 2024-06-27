'''
控制 WS2812 / NeoPixel LED

该模块提供用于 WS2818 / NeoPixel LED 的驱动器。

注意：

	默认情况下，此模块仅包含在 ESP8266、ESP32 和 RP2 端口上。

	在 STM32 / Pyboard 等平台上，您可以使用`mip`安装`neopixel`包，也可以直接从`micropython-lib`下载该模块并将其复制到文件系统中。

[查看文档](https://docs.micropython.org/en/latest/library/neopixel.html)
[查看 neopixel 源码](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/led/neopixel/neopixel.py)
'''
class NeoPixel(object):
	'''
	此类存储连接到引脚的 WS2812 LED 灯带的像素数据。

	应用程序应设置像素数据，然后在准备好更新灯带时调用`NeoPixel.write()`。
	'''
	def __init__(self, pin, n: int, *, bpp: int = 3, timing: int = 1):
		'''
		构造一个 NeoPixel 对象。

		参数包括：

		- `pin`是`machine.Pin`实例。
		- `n`是灯带中的 LED 数量。
		- `bpp`对于 RGB LED 是 3，对于 RGBW LED 是 4。
		- `timing`对于 400KHz LED 是 0，对于 800kHz LED（大多数都是800kHz）是 1。
		'''

	# Pixel access methods
	def fill(self, pixel: tuple):
		'''
		将所有像素的值设置为指定的`pixel`值（例如 RGB/RGBW 元组）。
		'''

	def __len__(self) -> int:
		'''返回灯带中的 LED 数量。'''

	def __setitem__(self, index: int, val: tuple):
		'''将`index`处的像素设置为该值，例如 RGB/RGBW 元组。'''

	def __getitem__(index: int) -> tuple:
		'''以 RGB/RGBW 元组的形式返回位于`index`处的像素。'''

	# Output methods
	def write():
		'''将当前像素数据写入灯带。'''
