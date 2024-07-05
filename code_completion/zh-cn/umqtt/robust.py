'''
用于 MicroPython 的轻量级 MQTT 客户端（“可靠”版）

umqtt.robust 是在 umqtt.simple 的基础上构建的，并增加了自动重连功能，以解决某些网络错误。

[查看文档](https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.robust/README.rst)
'''
from . import simple


class MQTTClient(simple.MQTTClient):
	'''一个适用于 MicroPython 的简单 MQTT 客户端。'''
	# Constants
	DELAY: int = ...
	DEBUG: bool = ...

	def __init__(self, client_id: str, server: str, port: int = 0, user: str | None = None,
		password: str | None = None, keepalive: int = 0, ssl=None):
		'''创建一个 MQTT 客户端实例。'''

	def delay(self, i): ...

	def log(self, in_reconnect: bool, e):
		'''记录异常信息'''

	def set_callback(self, f: function):
		'''为收到的订阅信息设置回调。'''

	def set_last_will(self, topic: bytes, msg: bytes, retain: bool = False, qos: int = 0):
		'''
		设置 MQTT "last will" 消息。

		应在`connect()`之前调用。
		'''

	def connect(self, clean_session: bool = True) -> bool:
		'''
		连接到服务器。

		如果此连接使用存储在服务器上的持久会话，则返回`True`。

		如果使用了`clean_session=True`参数（默认使用），则返回`False`。
		'''

	def reconnect(self):
		'''重新连接服务器。'''

	def disconnect(self):
		'''断开服务器连接，释放资源。'''

	def ping(self):
		'''Ping 服务器（响应由`wait_msg()`自动处理）。'''

	def publish(self, topic: bytes, msg: bytes, retain: bool = False, qos: int = 0):
		'''发布消息'''

	def subscribe(self, topic: bytes, qos: int = 0):
		'''订阅主题。'''

	def wait_msg(self):
		'''
		等待服务器消息。

		订阅信息将发送到使用`set_callback()`设置的回调，其他信息将在内部处理。
		'''

	def check_msg(self):
		'''
		检查是否有来自服务器的待处理信息。

		如果有待处理消息，则按照与`wait_msg()`相同的方式处理，如果没有，则立即返回。
		'''
