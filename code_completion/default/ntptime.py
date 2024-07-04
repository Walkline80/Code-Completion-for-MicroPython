'''
a NTP client.

[View ntptime.py](https://github.com/micropython/micropython-lib/blob/master/micropython/net/ntptime/ntptime.py)
'''
host: str = ...
'''
host can be configured at runtime by doing::

ntptime.host = 'myhost.org'
'''

timeout: int = ...
'''
timeout can be configured at runtime by doing::

ntptime.timeout = 2
'''

def time(): ...

def settime():
	'''
	There’s currently no timezone support in MicroPython, and the RTC is set in
	UTC time.
	'''
