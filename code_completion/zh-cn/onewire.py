'''
用于 MicroPython 的 OneWire 驱动程序。

OneWire 驱动程序在软件中实现，适用于所有引脚。

[查看 OneWire Driver 文档](https://docs.micropython.org/en/latest/esp32/quickref.html#onewire-driver)
[查看 onewire 源码](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/bus/onewire/onewire.py)
'''
class OneWireError(Exception): ...


class OneWire(object):
	SEARCH_ROM: int = ...
	MATCH_ROM: int = ...
	SKIP_ROM: int = ...

	def __init__(self, pin): ...

	def reset(self, required: bool = False):
		'''重置总线。'''

	def readbit(self):
		'''读取一位数据。'''

	def readbyte(self) -> bytes:
		'''读取一字节数据'''

	def readinto(self, buf): ...

	def writebit(self, value):
		'''在总线上写入一位数据。'''

	def writebyte(self, value):
		'''在总线上写入一字节数据。'''

	def write(self, buf):
		'''在总线上写入一组字节数据。'''

	def select_rom(self, rom):
		'''通过其 ROM 代码选择特定设备。'''

	def scan(self) -> list:
		'''返回总线上的设备列表。'''

	def crc8(self, data): ...
