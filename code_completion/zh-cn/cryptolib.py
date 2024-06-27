'''
加密密码

[查看文档](https://docs.micropython.org/en/latest/library/cryptolib.html)
'''
class aes(object):
	@classmethod
	def __init__(cls, key, mode: int, IV=None):
		'''
		初始化密码对象，适用于加密/解密。

		注意：初始化后，密码对象只能用于加密和解密。

		不支持在`encrypt()`之后运行`decrypt()`操作，反之亦然。

		参数包括：

		- `key`是加密/解密密钥（类似字节）。

		- `mode`为：

			- `1`（或`cryptolib.MODE_ECB`（如果存在））用于电子代码簿（ECB）。
			- `2`（或`cryptolib.MODE_CBC`（如果存在））用于密码块链接（CBC）。
			- `6`（或`cryptolib.MODE_CTR`（如果存在））用于计数器模式（CTR）。

		- `IV`是 CBC 模式的初始化向量。

		- 对于计数器模式，`IV`是计数器的初始值。
		'''

	# Methods
	def encrypt(self, in_buf, out_buf=None):
		'''
		加密`in_buf`。如果没有给出`out_buf`，则结果将作为新分配的字节对象返回。

		否则，结果将写入可变缓冲区`out_buf`。

		`in_buf`和`out_buf`也可以指同一个可变缓冲区，在这种情况下，数据是就地加密的。
		'''

	def decrypt(self, in_buf, out_buf=None):
		'''与`encrypt()`相似，但用于解密。'''
