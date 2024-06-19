'''
a NTP client.

[View Doc](https://github.com/micropython/micropython-lib/blob/master/micropython/net/ntptime/ntptime.py)
'''
host = ... # host can be configured at runtime by doing: ntptime.host = 'myhost.org'
timeout = ... # timeout can be configured at runtime by doing: ntptime.timeout = 2

def time():
	pass

def settime():
	'''
	There's currently no timezone support in MicroPython, and the RTC is set in UTC time.
	'''
