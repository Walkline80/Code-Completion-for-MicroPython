'''
DS18x20 temperature sensor driver.

[View OneWire Driver Doc](https://docs.micropython.org/en/latest/esp8266/tutorial/onewire.html)
[View ds18x20.py](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/sensor/ds18x20/ds18x20.py)
'''
import onewire


class DS18X20:
	def __init__(self, onewire: onewire.OneWire):
		'''Create a DS18X20 object associated with the given OneWire bus.'''

	def scan(self) -> list | None:
		'''Scan the bus and return a list of rom values.'''

	def convert_temp(self):
		'''Start a temperature conversion.'''

	def read_scratch(self, rom) -> bytearray:
		'''Read the scratchpad of the given device.'''

	def write_scratch(self, rom, buf):
		'''Write the scratchpad of the given device.'''

	def read_temp(self, rom) -> float:
		'''Read the temperature of the given device.'''
