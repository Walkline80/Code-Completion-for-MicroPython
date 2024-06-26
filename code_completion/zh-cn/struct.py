'''
打包和解包原始数据类型

此模块实现相应 CPython 模块的子集，如下所述。

有关详细信息，请参阅原始`CPython`文档：[struct](https://docs.python.org/3.5/library/struct.html#module-struct)。

[查看文档](https://docs.micropython.org/en/latest/library/struct.html)
'''
# Functions
def calcsize(fmt: str) -> int:
	'''返回存储给定`fmt`所需的字节数。'''

def pack(fmt: str, *values) -> bytes:
	'''
	根据格式字符串`fmt`打包`values`数据。

	返回值是对`values`进行编码的字节对象。
	'''

def pack_into(fmt: str, buffer, offset: int, *values):
	'''
	根据格式字符串`fmt`将`values`打包到从`offset`开始的`buffer`中。

	`offset`可能是负数，从`buffer`的末尾开始计数。
	'''

def unpack(fmt: str, data) -> tuple:
	'''
	根据格式字符串`fmt`从`data`中解包数据。

	返回值是包含解包数据的元组。
	'''

def unpack_from(fmt: str, data, offset: int = 0, /) -> tuple:
	'''
	根据格式字符串`fmt`从`offset`开始的`data`解包。

	`offset`可能是负数，从`data`的末尾开始计数。

	返回值是包含解包数据的元组。
	'''
