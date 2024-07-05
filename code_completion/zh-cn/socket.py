'''
套接字模块

此模块实现了相应`CPython`模块的子集，如下所述。

有关详细信息，请参阅原始`CPython`文档：[socket](https://docs.python.org/3.5/library/socket.html#module-socket)。

该模块提供对 BSD 套接字接口的访问。

[查看文档](https://docs.micropython.org/en/latest/library/socket.html)
'''
import typing


# Constants
# Address family types. Availability depends on a particular MicroPython port.
AF_INET: int = ...
AF_INET6: int = ...

# Socket types.
SOCK_STREAM: int = ...
SOCK_DGRAM: int = ...

# IP protocol numbers. Availability depends on a particular MicroPython port.
# Note that you don’t need to specify these in a call to `socket.socket()`,
# because `SOCK_STREAM`` socket type automatically selects `IPPROTO_TCP`, and
# `SOCK_DGRAM - IPPROTO_UDP`.
# Thus, the only real use of these constants is as an argument to `setsockopt()`.
IPPROTO_UDP: int = ... 
IPPROTO_TCP: int = ...
IPPROTO_IP: int = ...

# Socket option levels (an argument to `setsockopt()`).
# The exact inventory depends on a MicroPython port.
SOL_SOCKET: int = ...

# Socket options (an argument to `setsockopt()`).
# The exact inventory depends on a MicroPython port.
SO_REUSEADDR: int = ...
SO_BROADCAST: int = ...
SO_BINDTODEVICE: int = ...

IP_ADD_MEMBERSHIP: int = ...
TCP_NODELAY: int = ...

IPPROTO_SEC: int = ...
'''用于创建 SSL 兼容套接字的特殊协议值，WiPy 特有常量'''

# Functions
def getaddrinfo(host: str, port: int, af: int = 0, type: int = 0, proto: int = 0,
	flags: int = 0, /) -> tuple:
	'''
	将`host/port`参数转换为五元组的序列，其中包含创建连接到该服务的套接字所需的所有参数。

	参数`af`、`type`和`proto`（与`socket()`函数的含义相同）可用于筛选返回的地址类型。

	如果未指定参数或参数为 0，则会返回所有地址组合（需要用户进行过滤）。

	返回的五元组列表结构为：`(family, type, proto, canonname, sockaddr)`
	'''

def inet_ntop(af: int, bin_addr: bytes):
	'''
	将给定地址族`af`的二进制网络地址`bin_addr`转换为文本表示::

	    >>> socket.inet_ntop(socket.AF_INET, b"\\x7f\\x00\\x00\\x01")
	    >>> '127.0.0.1'
	'''

def inet_pton(af: int, txt_addr: str):
	'''
	将给定地址族`af`的文本网络地址`txt_addr`转换为二进制表示::

	    >>> socket.inet_pton(socket.AF_INET, "1.2.3.4")
	    >>> b'\\x01\\x02\\x03\\x04'
	'''


class socket(object):
	def __init__(self, af: int = AF_INET, type: int = SOCK_STREAM, proto: int = IPPROTO_TCP, /):
		'''
		使用给定的地址族、套接字类型和协议号创建新的套接字。

		请注意，大多数情况下不需要指定`proto`（也不推荐，因为某些 MicroPython 端口可能会省略`IPPROTO_*`常量）。

		相反，`type`参数会自动选择所需的协议。
		'''

	# Methods
	def close(self):
		'''
		标记套接字已关闭，并释放所有资源。

		一旦关闭，今后对套接字对象的所有操作都将失败。

		如果协议支持，远端将收到 EOF 指示。

		套接字在被垃圾回收时会自动关闭，但建议在使用完毕后立即明确地`close()`它们。
		'''

	def bind(self, address):
		'''
		将套接字绑定到`address`。

		该套接字必须尚未绑定。
		'''

	@typing.overload
	def listen(self):
		'''启用服务器接受连接。'''

	@typing.overload
	def listen(self, backlog: int):
		'''
		启用服务器接受连接。

		`backlog`必须至少为 0（如果低于 0，则将设为 0），并指定系统在拒绝新连接之前允许的未接受连接数。
		'''

	def accept(self) -> tuple:
		'''
		接受连接。

		套接字必须绑定到一个地址并监听连接。

		返回值是一对`(conn, address)`，其中`conn`是一个新的套接字对象，用于在连接上发送和接收数据，
		`address`是绑定到连接另一端套接字的地址。
		'''

	def connect(self, address):
		'''连接到位于`address`的远程套接字。'''

	def send(self, bytes: bytes) -> int:
		'''
		向套接字发送数据。

		套接字必须连接到远程套接字。

		返回发送的字节数，可能小于数据长度（"short write"）。
		'''

	def sendall(self, bytes: bytes) -> int:
		'''
		向套接字发送所有数据。

		套接字必须连接到远程套接字。

		与`send()`不同的是，此方法会尝试发送所有数据，即连续地逐块发送数据。

		此方法在非阻塞套接字上的行为未定义。

		因此，在 MicroPython 上，建议使用`write()`方法，该方法对阻塞套接字采用相同的
		"no short writes" 策略，并将返回在非阻塞套接字上发送的字节数。
		'''

	def recv(self, bufsize: int) -> bytes:
		'''
		从套接字接收数据。

		返回值是一个字节对象，代表接收到的数据。

		一次接收的最大数据量由`bufsize`指定。
		'''

	def sendto(self, bytes: bytes, address):
		'''
		向套接字发送数据。

		套接字不应连接到远程套接字，因为目标套接字是由`address`指定的。
		'''

	def recvfrom(self, bufsize: int) -> tuple:
		'''
		从套接字接收数据。

		返回值是一对`(bytes, address)`，其中`bytes`是表示接收到的数据的字节对象，
		`address`是发送数据的套接字的地址。
		'''

	def setsockopt(self, level, optname, value):
		'''
		设置给定套接字选项的值。

		所需的符号常量在 socket 模块`SO_*`中定义。

		`value`可以是整数，也可以是代表缓冲区的字节类对象。
		'''

	def settimeout(self, value: float | None):
		'''
		设置阻塞套接字操作的超时时间。

		参数`value`可以是表示秒数的非负浮点数，也可以是`None`。

		如果给定的值不是零，那么在操作完成之前，如果超时时间已过，后续的套接字操作将引发
		`OSError`异常。

		如果值为 0，套接字将进入非阻塞模式。

		如果值为`None`，则套接字处于阻塞模式。

		并非每个 MicroPython 端口都支持此方法。
		'''

	def setblocking(self, flag: bool):
		'''
		设置套接字的阻塞或非阻塞模式。

		如果`flag`为`False`，则套接字设置为非阻塞模式，否则设置为阻塞模式。

		该方法是某些`settimeout()`调用的简写：

		- sock.setblocking(True)`等同于`sock.settimeout(None)`。

		- sock.setblocking(False)`等同于`sock.settimeout(0)`。
		'''

	def makefile(self, mode: str = 'rb', buffering: int = 0, /):
		'''
		返回与套接字相关联的文件对象。

		确切的返回类型取决于为`makefile()`提供的参数。

		仅支持二进制模式（`'rb'`、`'wwb'`和`'rwb'`）。

		CPython 的参数：`encoding`，`errors`和`newline`不支持。

		与 CPython 的区别：

			由于 MicroPython 不支持缓冲流，因此会忽略参数`buffering`的值，并将其视为 0（无缓冲）。

			关闭由`makefile()`返回的文件对象也将关闭原始套接字。
		'''

	def read(self, size: int = None) -> bytes:
		'''
		从套接字读取最多`size`个字节数据。

		返回字节对象。

		如果未给定`size`，则会读取套接字的所有可用数据，直至 EOF，因此该方法在套接字关闭前不会返回。

		该函数会尽量读取所请求的全部数据（no "short reads"）。

		但在非阻塞套接字的情况下，可能无法做到这一点，因此返回的数据会较少。
		'''

	def readinto(self, buf, nbytes: int) -> int:
		'''
		将字节读入`buf`。

		如果指定了`nbytes`，则最多读取这么多字节。

		否则，最多读取`len(buf)`字节。

		与`read()`一样，本方法遵循 "no short reads" 策略。

		返回值：读取并存储到`buf`中的字节数。
		'''

	def readline(self) -> bytes:
		'''
		读取一行，以换行符结束。

		返回值：读取的行。
		'''

	def write(self, buf) -> int:
		'''
		将字节缓冲区写入套接字。

		此函数将尝试向套接字写入所有数据（no "short writes"）。

		但在非阻塞套接字中可能无法做到这一点，因此返回值将小于`buf`的长度。

		返回值：写入的字节数。
		'''
