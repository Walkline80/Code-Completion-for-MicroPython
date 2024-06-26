'''
DS18x20温度传感器驱动程序。

[查看 OneWire Driver 文档](https://docs.micropython.org/en/latest/esp8266/tutorial/onewire.html)
[查看 ds18x20 源码](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/sensor/ds18x20/ds18x20.py)
'''
import onewire


class DS18X20:
	def __init__(self, onewire: onewire.OneWire):
		'''创建一个与指定的`OneWire`总线关联的`DS18X20`对象。'''

	def scan(self) -> list | None:
		'''扫描总线并返回`rom`值列表。'''

	def convert_temp(self):
		'''启动温度转换。'''

	def read_scratch(self, rom) -> bytearray:
		'''读取指定设备的暂存器。'''

	def write_scratch(self, rom, buf):
		'''写入指定设备的暂存器。'''

	def read_temp(self, rom) -> float:
		'''读取指定设备的温度。'''
