'''
1-Wire driver for MicroPython

The OneWire driver is implemented in software and works on all pins.

[View Doc](https://docs.micropython.org/en/latest/esp32/quickref.html#onewire-driver)
'''
class OneWireError(Exception):
	pass


class OneWire(object):
	SEARCH_ROM = ...
	MATCH_ROM = ...
	SKIP_ROM = ...

	def __init__(self, pin):
		pass

	def reset(self, required: bool = False):
		'''Reset the bus.'''

	def readbit(self):
		'''Read a bit.'''

	def readbyte(self) -> bytes:
		'''Read a byte.'''

	def readinto(self, buf):
		pass

	def writebit(self, value):
		'''Write a bit on the bus.'''

	def writebyte(self, value):
		'''Write a byte on the bus.'''

	def write(self, buf):
		'''Write bytes on the bus.'''

	def select_rom(self, rom):
		'''Select a specific device by its ROM code.'''

	def scan(self) -> list:
		'''Return a list of devices on the bus.'''

	def crc8(self, data):
		pass
