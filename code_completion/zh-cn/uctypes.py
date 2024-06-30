'''
以结构化方式访问二进制数据

该模块实现了 MicroPython 的`外部数据接口`。

它背后的想法类似于 CPython 的`ctypes`模块，但实际的 API 是不同的，针对小尺寸进行了简化和优化。

该模块的基本思想是定义与 C 语言所允许的大致相同的功能的数据结构布局，然后使用熟悉的点语法访问它以引用子字段。

[查看文档](https://docs.micropython.org/en/latest/library/uctypes.html)
'''
# Constants
# Integer types for structure descriptors.
# Constants for 8, 16, 32, and 64 bit types are provided, both signed and unsigned.
UINT8: int = ...
INT8: int = ...
UINT16: int = ...
INT16: int = ...
UINT32: int = ...
INT32: int = ...
UINT64: int = ...
INT64: int = ...

# Floating-point types for structure descriptors.
FLOAT32: int = ...
FLOAT64: int = ...

BFUINT8: int = ...
BFINT8: int = ...
BFUINT16: int = ...
BFINT16: int = ...
BFUINT32: int = ...
BFINT32: int = ...
BF_POS: int = ...
BF_LEN: int = ...
SHORT: int = ...
USHORT: int = ...
INT: int = ...
UINT: int = ...
LONG: int = ...
ULONG: int = ...
LONGLONG: int = ...
ULONGLONG: int = ...

VOID: int = ...
'''
`VOID`是`UINT8`的别名，用于方便地定义 C 的 void 指针：`(uctypes.PTR, uctypes.VOID)`。
'''

# Type constants for pointers and arrays.
# Note that there is no explicit constant for structures, it’s implicit: an
# aggregate type without PTR or ARRAY flags is a structure.
PTR: int = ...
ARRAY: int = ...

LITTLE_ENDIAN: int = ...
'''
小端填充结构的布局类型。

填充意味着每个字段占用的字节数与描述符中定义的字节数完全相同，即对齐方式为 1。
'''

BIG_ENDIAN: int = ...
'''大端填充结构的布局类型。'''

NATIVE: int = ...
'''
原生结构的布局类型

数据字节序和对齐方式符合运行 MicroPython 的系统的 ABI。
'''


class struct(object):
	def __init__(self, addr: int, descriptor: dict, layout_type: int = NATIVE, /):
		'''
		根据内存中的结构地址、描述符（编码为字典）和布局类型实例化`外部数据结构`对象。
		'''


def sizeof(struct, layout_type: int = NATIVE, /) -> int:
	'''
	返回数据结构的大小（以字节为单位）。

	`struct`参数可以是结构类，也可以是特定的实例化结构对象（或其聚合字段）。
	'''

def addressof(obj) -> int:
	'''
	返回对象的地址。

	参数应该是字节、字节数组或其他支持缓冲区协议的对象（此缓冲区的地址是实际返回的地址）。
	'''

def bytes_at(addr: int, size: int) -> bytes:
	'''
	将给定地址和大小的内存捕获为字节对象。

	由于 bytes 对象是不可变的，因此内存实际上是复制到 bytes 对象中的，因此如果以后内存
	内容发生变化，创建的对象将保留原始值。
	'''

def bytearray_at(addr: int, size: int) -> bytearray:
	'''
	将给定地址和大小的内存捕获为 bytearray 对象。

	与`bytes_at()`函数不同，内存是通过引用捕获的，因此它也可以写入，并且你还可以访问给定
	内存地址的当前值。
	'''
