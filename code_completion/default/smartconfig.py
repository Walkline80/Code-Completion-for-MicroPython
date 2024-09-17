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


def version():
	'''获取 SmartConfig 内部版本号'''

def start():
	'''开启配网功能'''

def stop():
	'''停止配网功能'''

def done() -> bool:
	'''
	获取配网完成状态

	返回`True`表示已获取配网信息，返回`False`表示未获取到配网信息。
	'''

def timeout():
	'''设置/获取配网超时时间，单位为秒，有效值范围：15~255'''

def fast_mode():
	'''设置/获取配网模式，默认为正常模式'''

def v2_key():
	'''设置/获取 EspTouch V2 协议使用的密钥，长度为16字节，传递`None`或空字符串清空秘钥'''

def info() -> tuple:
	'''
	获取配网信息，返回值包含如下信息::

	```python
		# v2_data - EspTouch V2 custom data
	    ('ssid', 'password', b'bssid', type[, b'v2_data'])
	```
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

def v2_data() -> bytes:
	'''获取 EspTouch V2 自定义数据'''
