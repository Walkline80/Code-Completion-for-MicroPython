'''
Lightweight MQTT client for MicroPython ("robust" version).

umqtt.robust is built on top of umqtt.simple and adds auto-reconnect facilities
for some of networking errors.

[View Doc](https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.robust/README.rst)
'''
from . import simple


class MQTTClient(simple.MQTTClient):
	# Constants
	DELAY: int = ...
	DEBUG: bool = ...

	def delay(self, i): ...

	def log(self, in_reconnect, e):
		'''Logging exception message'''

	def reconnect(self):
		'''Reconnect to a server.'''

	def publish(self, topic, msg, retain: bool = False, qos: int = 0):
		'''Publish a message.'''

	def wait_msg(self):
		'''
		Wait for a server message.

		A subscription message will be delivered to a callback set with
		`set_callback()`, any other messages will be processed internally.
		'''

	def check_msg(self, attempts=2):
		'''
		Check if there’s pending message from server.

		If yes, process the same way as `wait_msg()`, if not, return immediately.
		'''
