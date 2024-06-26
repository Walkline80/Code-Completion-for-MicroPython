'''
二进制/ASCII 转换

此模块实现相应`CPython`模块的子集，如下所述。

有关更多信息，请参阅原始`CPython`文档：[binascii](https://docs.python.org/3.5/library/binascii.html#module-binascii)。

该模块以 ASCII 形式（双向）实现二进制数据与其各种编码之间的转换。

[查看文档](https://docs.micropython.org/en/latest/library/binascii.html)
'''
# Functions
def hexlify(data, sep=None) -> bytes:
	'''
	将`data`对象中的字节转换为十六进制表示形式。

	返回一个字节对象。

	如果提供了附加参数`sep`，则将其用作十六进制值之间的分隔符。
	'''

def unhexlify(data) -> bytes:
	'''
	将十六进制的`data`转换为二进制表示。

	返回字节字符串。

	（即`hexlify`的反操作）
	'''

def a2b_base64(data) -> bytes:
	'''
	解码 base64 编码的`data`，忽略输入中的无效字符。

	符合 [RFC 2045 s.6.8](https://tools.ietf.org/html/rfc2045#section-6.8)。

	返回一个字节对象。
	'''

def b2a_base64(data, *, newline=True) -> bytes:
	'''
	以 base64 格式对二进制数据进行编码，如 [RFC 3548](https://tools.ietf.org/html/rfc3548.html) 中所示。

	如果`newline`为`True`，则返回一个编码后以换行结尾的字节对象数据。
	'''
