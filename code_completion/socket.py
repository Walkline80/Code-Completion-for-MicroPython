'''
socket module

This module implements a subset of the corresponding CPython module, as described below.

For more information, refer to the original CPython documentation: socket.

This module provides access to the BSD socket interface.

[View Doc](https://docs.micropython.org/en/latest/library/socket.html)
'''
from typing import overload


# Constants
# Address family types. Availability depends on a particular MicroPython port.
AF_INET = ...
AF_INET6 = ...

# Socket types.
SOCK_STREAM = ...
SOCK_DGRAM = ...

# IP protocol numbers. Availability depends on a particular MicroPython port.
# Note that you don’t need to specify these in a call to `socket.socket()`,
# because `SOCK_STREAM`` socket type automatically selects `IPPROTO_TCP`, and
# `SOCK_DGRAM - IPPROTO_UDP`.
# Thus, the only real use of these constants is as an argument to `setsockopt()`.
IPPROTO_UDP = ... 
IPPROTO_TCP = ...

# Socket option levels (an argument to `setsockopt()`).
# The exact inventory depends on a MicroPython port.
SOL_SOCKET = ...

# Socket options (an argument to `setsockopt()`).
# The exact inventory depends on a MicroPython port.
SO_REUSEADDR = ...
SO_BROADCAST = ...
SO_BINDTODEVICE = ...

IPPROTO_SEC = ...
'''
Constants specific to WiPy

Special protocol value to create SSL-compatible socket.
'''

# Functions
def getaddrinfo(host: str, port: int, af: int = 0, type: int = 0, proto: int = 0,
	flags: int = 0, /) -> tuple:
	'''
	Translate the host/port argument into a sequence of 5-tuples that contain all
	the necessary arguments for creating a socket connected to that service.

	Arguments `af`, `type`, and `proto` (which have the same meaning as for the
	`socket()` function) can be used to filter which kind of addresses are
	returned.

	If a parameter is not specified or zero, all combinations of addresses can
	be returned (requiring filtering on the user side).

	The resulting list of 5-tuples has the following structure:

		`(family, type, proto, canonname, sockaddr)`
	'''

def inet_ntop(af: int, bin_addr: bytes):
	'''
	Convert a binary network address `bin_addr` of the given address family `af`
	to a textual representation::

	    >>> socket.inet_ntop(socket.AF_INET, b"\\x7f\\x00\\x00\\x01")
	    >>> '127.0.0.1'
	'''

def inet_pton(af: int, txt_addr: str):
	'''
	Convert a textual network address `txt_addr` of the given address family `af`
	to a binary representation::

	    >>> socket.inet_pton(socket.AF_INET, "1.2.3.4")
	    >>> b'\\x01\\x02\\x03\\x04'
	'''


class socket(object):
	def __init__(self, af: int = AF_INET, type: int = SOCK_STREAM, proto: int = IPPROTO_TCP, /):
		'''
		Create a new socket using the given address family, socket type and
		protocol number.

		Note that specifying `proto` in most cases is not required (and not
		recommended, as some MicroPython ports may omit `IPPROTO_*` constants).

		Instead, `type` argument will select needed protocol automatically.
		'''

	# Methods
	def close(self):
		'''
		Mark the socket closed and release all resources.

		Once that happens, all future operations on the socket object will fail.

		The remote end will receive EOF indication if supported by protocol.

		Sockets are automatically closed when they are garbage-collected, but it
		is recommended to `close()` them explicitly as soon you finished working
		with them.
		'''

	def bind(self, address):
		'''
		Bind the socket to `address`.

		The socket must not already be bound.
		'''

	@overload
	def listen(self):
		'''
		Enable a server to accept connections.

		A default reasonable value is chosen.
		'''

	@overload
	def listen(self, backlog: int):
		'''
		Enable a server to accept connections.

		`backlog` must be at least 0 (if it’s lower, it will be set to 0); and
		specifies the number of unaccepted connections that the system will allow
		before refusing new connections.
		'''

	def accept(self) -> tuple:
		'''
		Accept a connection.

		The socket must be bound to an address and listening for connections.

		The return value is a pair (conn, address) where conn is a new socket
		object usable to send and receive data on the connection, and address
		is the address bound to the socket on the other end of the connection.
		'''

	def connect(self, address):
		'''Connect to a remote socket at `address`.'''

	def send(self, bytes) -> int:
		'''
		Send data to the socket.

		The socket must be connected to a remote socket.

		Returns number of bytes sent, which may be smaller than the length of
		data ("short write").
		'''

	def sendall(self, bytes) -> int:
		'''
		Send all data to the socket.

		The socket must be connected to a remote socket.

		Unlike `send()`, this method will try to send all of data, by sending
		data chunk by chunk consecutively.

		The behaviour of this method on non-blocking sockets is undefined.

		Due to this, on MicroPython, it’s recommended to use `write()` method
		instead, which has the same "no short writes" policy for blocking sockets,
		and will return number of bytes sent on non-blocking sockets.
		'''

	def recv(self, bufsize: int) -> bytes:
		'''
		Receive data from the socket.

		The return value is a bytes object representing the data received.

		The maximum amount of data to be received at once is specified by
		`bufsize`.
		'''

	def sendto(self, bytes, address):
		'''
		Send data to the socket.

		The socket should not be connected to a remote socket, since the
		destination socket is specified by `address`.
		'''

	def recvfrom(self, bufsize) -> tuple:
		'''
		Receive data from the socket.

		The return value is a pair `(bytes, address)` where `bytes` is a bytes
		object representing the data received and `address` is the address of
		the socket sending the data.
		'''

	def setsockopt(self, level, optname, value):
		'''
		Set the value of the given socket option.

		The needed symbolic constants are defined in the socket module
		(SO_* etc.).

		The `value` can be an integer or a bytes-like object representing a
		buffer.
		'''

	def settimeout(self, value: float | None):
		'''
		Set a timeout on blocking socket operations.

		The `value` argument can be a nonnegative floating point number expressing
		seconds, or None.

		- If a non-zero value is given, subsequent socket operations will raise
		an `OSError` exception if the timeout period value has elapsed before
		the operation has completed.

		- If zero is given, the socket is put in non-blocking mode.

		- If None is given, the socket is put in blocking mode.

		Not every MicroPython port supports this method.
		'''

	def setblocking(self, flag: bool):
		'''
		Set blocking or non-blocking mode of the socket: if `flag` is False, the
		socket is set to non-blocking, else to blocking mode.

		This method is a shorthand for certain `settimeout()` calls:

		- `sock.setblocking(True)` is equivalent to `sock.settimeout(None)`

		- `sock.setblocking(False)` is equivalent to `sock.settimeout(0)`
		'''

	def makefile(self, mode: str = 'rb', buffering: int = 0, /):
		'''
		Return a file object associated with the socket.

		The exact returned type depends on the arguments given to `makefile()`.

		The support is limited to binary modes only (‘rb’, ‘wb’, and ‘rwb’).

		CPython’s arguments: encoding, errors and newline are not supported.

		Difference to CPython:

			As MicroPython doesn’t support buffered streams, values of `buffering`
			parameter is ignored and treated as if it was 0 (unbuffered).

			Closing the file object returned by `makefile()` WILL close the
			original socket as well.
		'''

	@overload
	def read(self) -> bytes:
		'''
		Read up to `size` bytes from the socket.

		Return a bytes object.

		It reads all data available from the socket until EOF; as such the method
		will not return until the socket is closed.

		This function tries to read as much data as requested (no "short reads").

		This may be not possible with non-blocking socket though, and then less
		data will be returned.
		'''

	@overload
	def read(self, size: int) -> bytes:
		'''
		Read up to `size` bytes from the socket.

		Return a bytes object.

		This function tries to read as much data as requested (no "short reads").

		This may be not possible with non-blocking socket though, and then less
		data will be returned.
		'''

	@overload
	def readinto(self, buf) -> int:
		'''
		Read bytes into the `buf`.

		Read at most `len(buf)` bytes.

		Just as `read()`, this method follows "no short reads" policy.

		Return value: number of bytes read and stored into buf.
		'''

	@overload
	def readinto(self, buf, nbytes: int) -> int:
		'''
		Read bytes into the `buf`.

		Read at most that many bytes.

		Just as `read()`, this method follows "no short reads" policy.

		Return value: number of bytes read and stored into buf.
		'''

	def readline(self) -> bytes:
		'''
		Read a line, ending in a newline character.

		Return value: the line read.
		'''

	def write(self, buf) -> int:
		'''
		Write the buffer of bytes to the socket.

		This function will try to write all data to a socket (no "short writes").

		This may be not possible with a non-blocking socket though, and returned
		value will be less than the length of `buf`.

		Return value: number of bytes written.
		'''
