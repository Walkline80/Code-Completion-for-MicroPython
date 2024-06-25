'''
NTP 客户端。

[查看文档](https://github.com/micropython/micropython-lib/blob/master/micropython/net/ntptime/ntptime.py)
'''
host: str = ...
'''
可以通过以下操作在运行时配置`host`::

ntptime.host = 'myhost.org'
'''

timeout: int = ...
'''
可以通过以下操作在运行时配置`timeout`::

ntptime.timeout = 2
'''

def time(): ...

def settime():
	'''目前 MicroPython 中没有时区支持，`RTC`设置为`UTC`时间。'''
