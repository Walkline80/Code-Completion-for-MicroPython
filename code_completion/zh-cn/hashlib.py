'''
哈希算法

此模块实现相应`CPython`模块的子集，如下所述。

有关更多信息，请参阅原始`CPython`文档：[hashlib](https://docs.python.org/3.5/library/hashlib.html#module-hashlib)。

该模块实现二进制数据哈希算法。可用算法的确切清单取决于开发板。

可能实现的算法包括：

- SHA256 - 当前一代的现代哈希算法（SHA2 系列）.

	它适用于加密安全目的。

	包含在 MicroPython 内核中，建议任何板提供此功能，除非它有特定的代码大小限制。

- SHA1 - 上一代算法.

	不建议用于新用途，但 SHA1 是许多 Internet 标准和现有应用程序的一部分，因此以网络连接
	和互操作性为目标的开发板将尝试提供这一点。

- MD5 - 一种遗留算法，不被认为是加密安全的.

	只有选定的开发板，针对与传统应用的互操作性，才会提供这一功能。

[查看文档](https://docs.micropython.org/en/latest/library/hashlib.html)
'''
class sha256(object):
	def __init__(self, data=None):
		'''创建一个 SHA256 哈希对象，并选择性地输入`data`到其中。'''

	# Methods
	def update(self, data):
		'''将更多二进制`data`输入到哈希中。'''

	def digest(self) -> bytes:
		'''
		返回通过哈希传递的所有数据的哈希值，作为字节对象。

		调用此方法后，无法再将更多数据馈送到哈希中。
		'''

	def hexdigest(self):
		'''
		此方法未实现。

		使用`binascii.hexlify(hash.digest())`达到类似的效果。
		'''


class sha1(object):
	def __init__(self, data=None):
		'''创建一个 SHA1 哈希对象，并选择性地输入`data`到其中。'''

	# Methods
	def update(self, data):
		'''将更多二进制`data`输入到哈希中。'''

	def digest(self) -> bytes:
		'''
		返回通过哈希传递的所有数据的哈希值，作为字节对象。

		调用此方法后，无法再将更多数据馈送到哈希中。
		'''

	def hexdigest(self):
		'''
		此方法未实现。

		使用`binascii.hexlify(hash.digest())`达到类似的效果。
		'''


class md5(object):
	def __init__(self, data=None):
		'''创建一个 MD5 哈希对象，并选择性地输入`data`到其中。'''

	# Methods
	def update(self, data):
		'''将更多二进制`data`输入到哈希中。'''

	def digest(self) -> bytes:
		'''
		返回通过哈希传递的所有数据的哈希值，作为字节对象。

		调用此方法后，无法再将更多数据馈送到哈希中。
		'''

	def hexdigest(self):
		'''
		此方法未实现。

		使用`binascii.hexlify(hash.digest())`达到类似的效果。
		'''
