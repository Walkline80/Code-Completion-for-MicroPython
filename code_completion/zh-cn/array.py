'''
数值数据数组

此模块实现相应`CPython`模块的子集，如下所述。

有关更多信息，请参阅原始`CPython`文档：[array](https://docs.python.org/3.5/library/array.html#module-array)。

支持的格式代码：'b'、'B'、'h'、'H'、'i'、'I'、'l'、'L'、'q'、'Q'、'f'、'd'（后 2 种取决于浮点支持）。

[查看文档](https://docs.micropython.org/en/latest/library/array.html)
'''
import typing


class array(object):
	def __init__(self, typecode: str, iterable=None):
		'''
		使用给定类型的元素创建数组。

		数组的初始内容由`iterable`给出，如未提供，则创建一个空数组。
		'''

	def append(self, val):
		'''将新元素`val`附加到数组的末尾，使其增长。'''

	def extend(self, iterable):
		'''
		将`iterable`中包含的新元素附加到数组的末尾，使其增长。
		'''

	def __getitem__(self, index) -> typing.Any:
		'''
		数组的索引读取，调用方法为`a[index]`（其中`a`是`array`）。

		如果`index`是`int`，则返回一个值，如果`index`是切片，则返回一个`array`。

		负索引从末尾开始计数，如果索引超出范围，则抛出`IndexError`。

		注意：

			`__getitem__`不能直接调用（`a.__getitem__(index)`会失败）并且不在
			`__dict__`中出现，但`a[index]`有效。
		'''

	def __setitem__(self, index, value):
		'''
		索引写入数组，调用方法为`a[index] = value`（其中`a`是`array`）。

		如果`index`是`int`，则`value`是单个值，如果`index`是切片，则为`array`。

		负索引从末尾开始计数，如果索引超出范围，则抛出`IndexError`。

		注意：

			`__setitem__`不能直接调用（`a.__setitem__(index, value)`会失败）并且不在
			`__dict__`中出现，但`a[index] = value`有效。
		'''

	def __len__(self) -> int:
		'''
		返回数组中的项目数，调用方法为`len(a)`（其中`a`是`array`）。

		注意：

			`__len__`不能直接调用（`a.__len__()`会失败）并且不在`__dict__`中出现，但
			`len(a)`有效。
		'''

	def __add__(self, other) -> typing.Any:
		'''
		返回一个新的`array`，它是数组与`other`的串联，调用方法为`a + other`（其中`a`和`other`都是`arrays`）。

		注意：

			`__add__`不能直接调用（`a.__add__(other)`会失败）并且不在`__dict__`中出现，但
			`a + other`有效。
		'''

	def __iadd__(self, other):
		'''
		将数组与`other`就地连接起来，调用方法为`a += other`（其中`a`和`other`都是`arrays`）。

		相当于`extend(other)`。

		注意：

			`__iadd__`不能直接调用（`a.__iadd__(other)`会失败）并且不在`__dict__`中出现，但
			`a += other`有效。
		'''

	def __repr__(self) -> str:
		'''
		返回数组的字符串表示形式，调用方法为`str(a)`或`repr(a)`（其中`a`是`array`）。

		返回字符串`"array(<type>, [<elements>])"`，其中`<type>`是数组的类型代码格式字母，
		`<elements>`是数组元素的逗号分隔列表。

		注意：

			`__repr__`不能直接调用（`a.__repr__()`会失败）并且不在`__dict__`中出现，但
			`str(a)`和`repr(a)`有效。
		'''
