'''
DHT11 & DHT22 temperature/humidity sensor driver

[View Doc dht-driver](https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver)
[View Doc Temperature and Humidity](https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html)
'''
class DHTBase:
	def __init__(self, pin): ...

	def measure(self):
		'''Measure temperature and humidity.'''


class DHT11(DHTBase):
	'''DHT11 driver for MicroPython.'''
	def humidity(self) -> float:
		'''Humidity in percent.'''

	def temperature(self) -> float:
		'''Temperature in Celsius.'''


class DHT22(DHTBase):
	'''DHT22 driver for MicroPython.'''
	def humidity(self) -> float:
		'''Humidity in percent.'''

	def temperature(self) -> float:
		'''Temperature in Celsius.'''
