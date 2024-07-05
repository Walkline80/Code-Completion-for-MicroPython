'''
Lightweight MQTT client for MicroPython.

[View Doc](https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/README.rst)
'''
class MQTTException(Exception): ...


class MQTTClient:
	'''a simple MQTT client for MicroPython.'''
	def __init__(self, client_id: str, server: str, port: int = 0, user: str | None = None,
		password: str | None = None, keepalive: int = 0, ssl=None):
		'''Create an instance of the MQTT client.'''

	def set_callback(self, f: function):
		'''Set callback for received subscription messages.'''

	def set_last_will(self, topic: bytes, msg: bytes, retain: bool = False, qos: int = 0):
		'''
		Set MQTT "last will" message.

		Should be called before `connect()`.
		'''

	def connect(self, clean_session: bool = True) -> bool:
		'''
		Connect to a server.

		Returns `True` if this connection uses persisten session stored on a server.

		This will be always `False` if `clean_session=True` argument is used
		(default).
		'''

	def disconnect(self):
		'''Disconnect from a server, release resources.'''

	def ping(self):
		'''Ping server (response is processed automatically by `wait_msg()`).'''

	def publish(self, topic: bytes, msg: bytes, retain: bool = False, qos: int = 0):
		'''Publish a message.'''

	def subscribe(self, topic: bytes, qos: int = 0):
		'''Subscribe to a topic.'''

	def wait_msg(self):
		'''
		Wait for a server message.

		A subscription message will be delivered to a callback set with
		`set_callback()`, any other messages will be processed internally.
		'''

	def check_msg(self):
		'''
		Check if there’s pending message from server.

		If yes, process the same way as `wait_msg()`, if not, return immediately.
		'''
