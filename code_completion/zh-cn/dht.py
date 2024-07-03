'''
DHT11 和 DHT22 温度/湿度传感器驱动程序

[查看 DHT 驱动程序文档](https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver)
[查看温度和湿度文档](https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html)
'''
class DHTBase:
	def __init__(self, pin): ...

	def measure(self):
		'''测量温度和湿度。'''


class DHT11(DHTBase):
	'''用于 MicroPython 的 DHT11 驱动程序。'''
	def humidity(self) -> float:
		'''获取湿度（百分比）。'''

	def temperature(self) -> float:
		'''获取温度（摄氏度）。'''


class DHT22(DHTBase):
	'''用于 MicroPython 的 DHT22 驱动程序。'''
	def humidity(self) -> float:
		'''获取湿度（百分比）。'''

	def temperature(self) -> float:
		'''获取温度（摄氏度）。'''
