'''
为 MicroPython 提供 SmartConfig 相关功能。

[View Doc](https://github.com/micropython/micropython/pull/13658)
'''
import typing


# Constants
# 配网协议类型
TYPE_ESPTOUCH: int = ...
TYPE_AIRKISS: int = ...
TYPE_ESPTOUCH_AIRKISS: int = ...
TYPE_ESPTOUCH_V2: int = ...

def start():
	'''开启配网功能'''

def stop():
	'''停止配网功能'''

def done() -> bool:
	'''
	获取配网完成状态

	返回`True`表示已获取配网信息，返回`False`表示未获取到配网信息。
	'''

def info() -> tuple:
	'''
	获取配网信息，返回值包含如下信息::

	    ('ssid', 'password', b'bssid', type[, b'rvd_data'])

	- rvd_data: EspTouch V2 custom data
	'''

def ssid() -> str:
	'''获取 ssid'''

def password() -> str:
	'''获取 password'''

def bssid() -> bytes:
	'''获取 bssid'''

@typing.overload
def type() -> int:
	'''获取配网协议类型'''

@typing.overload
def type(value: int):
	'''设置配网协议类型'''

def rvd_data() -> bytes:
	'''获取 EspTouch V2 自定义数据'''
