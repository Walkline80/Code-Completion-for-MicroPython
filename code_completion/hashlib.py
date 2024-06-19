'''
hashing algorithms

This module implements a subset of the corresponding CPython module, as described below.

For more information, refer to the original CPython documentation: hashlib.

This module implements binary data hashing algorithms.

The exact inventory of available algorithms depends on a board.

Among the algorithms which may be implemented:

- SHA256 - The current generation, modern hashing algorithm (of SHA2 series).

	It is suitable for cryptographically-secure purposes.

	Included in the MicroPython core and any board is recommended to provide this, unless it has particular code size constraints.

- SHA1 - A previous generation algorithm.

	Not recommended for new usages, but SHA1 is a part of number of Internet standards and existing applications, so boards targeting network connectivity and interoperability will try to provide this.

- MD5 - A legacy algorithm, not considered cryptographically secure.

	Only selected boards, targeting interoperability with legacy applications, will offer this.

[View Doc](https://docs.micropython.org/en/latest/library/hashlib.html)
'''
class sha256(object):
	def __init__(self, data=None):
		'''Create an SHA256 hasher object and optionally feed data into it.'''

	# Methods
	def update(self, data):
		'''Feed more binary data into hash.'''

	def digest(self) -> bytes:
		'''
		Return hash for all data passed through hash, as a bytes object.

		After this method is called, more data cannot be fed into the hash any longer.
		'''

	def hexdigest(self):
		'''
		This method is NOT implemented.

		Use binascii.hexlify(hash.digest()) to achieve a similar effect.
		'''


class sha1(object):
	def __init__(self, data=None):
		'''Create an SHA1 hasher object and optionally feed data into it.'''

	# Methods
	def update(self, data):
		'''Feed more binary data into hash.'''

	def digest(self) -> bytes:
		'''
		Return hash for all data passed through hash, as a bytes object.

		After this method is called, more data cannot be fed into the hash any longer.
		'''

	def hexdigest(self):
		'''
		This method is NOT implemented.

		Use binascii.hexlify(hash.digest()) to achieve a similar effect.
		'''


class md5(object):
	def __init__(self, data=None):
		'''Create an MD5 hasher object and optionally feed data into it.'''

	# Methods
	def update(self, data):
		'''Feed more binary data into hash.'''

	def digest(self) -> bytes:
		'''
		Return hash for all data passed through hash, as a bytes object.

		After this method is called, more data cannot be fed into the hash any longer.
		'''

	def hexdigest(self):
		'''
		This method is NOT implemented.

		Use binascii.hexlify(hash.digest()) to achieve a similar effect.
		'''
