'''
DS18x20 temperature sensor driver.

[View Doc](https://docs.micropython.org/en/latest/esp8266/tutorial/onewire.html)
'''
class DS18X20:
	def __init__(self, onewire):
		'''Create a DS18x20 object associated with the given OneWire bus.'''

	def scan(self):
		'''Scan the bus and return a list of rom values.'''

	def convert_temp(self):
		'''Start a temperature conversion.'''

	def read_scratch(self, rom):
		'''Read the scratchpad of the given device.'''

	def write_scratch(self, rom, buf):
		'''Write the scratchpad of the given device.'''

	def read_temp(self, rom):
		'''Read the temperature of the given device.'''
