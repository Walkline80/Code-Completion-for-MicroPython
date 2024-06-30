'''
集合和容器类型

此模块实现相应`CPython`模块的子集，如下所述。

有关详细信息，请参阅原始`CPython`文档：[collections](https://docs.python.org/3.5/library/collections.html#module-collections)。

该模块实现了高级收集和容器类型，以保存/累积各种对象。

[查看文档](https://docs.micropython.org/en/latest/library/collections.html)
'''
import typing


class deque(object):
	def __init__(self, iterable, maxlen: int, flags: int = None):
		'''
		Deques（双端队列）是一个类似列表的容器，它支持 O(1) 追加和从 deque 的任一侧弹出。

		使用以下参数创建新的 deques：

		- `iterable`是一个迭代对象，用于在创建 deque 时填充它。

			它可以是空元组或列表，以创建最初为空的 deque。

		- `maxlen`必须被指定，并且 deque 将被限制到此最大长度。

			一旦 deque 已满，添加任何新项目都将从另一端丢弃相应数量的项目。

		- 可选的`flags`可以是 1，用于在添加项目时检查溢出。

		Deque 对象支持`bool`、`len`、迭代和下标加载和存储。
		'''

	def append(self, x):
		'''
		将`x`添加到 deque 的右侧。

		如果启用了溢出检查并且队列中没有更多空间，则引发`IndexError`。
		'''

	def appendleft(self, x):
		'''
		将`x`添加到 deque 的左侧。

		如果启用了溢出检查并且队列中没有更多空间，则引发`IndexError`。
		'''

	def pop(self) -> typing.Any:
		'''
		从 deque 的右侧移除并返回一个项目。

		如果不存在任何项，则引发`IndexError`。
		'''

	def popleft(self) -> typing.Any:
		'''
		从 deque 的左侧移除并返回一个项目。

		如果不存在任何项，则引发`IndexError`。
		'''

	def extend(self, iterable):
		'''
		通过将`iterable`中的所有项目附加到 deque 的右侧来扩展 deque。

		如果启用了溢出检查并且 deque 中没有更多空间，则引发`IndexError`。
		'''


def namedtuple(name: str, fields):
	'''
	这是工厂函数，用于创建具有特定名称和字段集的新命名元组类型。

	命名元组是元组的子类，它不仅允许通过数字索引访问其字段，还允许使用符号字段名称的属性访问
	语法访问其字段。

	字段是指定字段名称的字符串序列。

	为了与`CPython`兼容，它也可以是一个带有空格分隔字段的字符串（但效率较低）。
	'''


class OrderedDict(object):
	'''
	`dict`类型的子类，用于记住并保留添加的键的顺序。

	当有序字典迭代时，键/项将按添加顺序返回。
	'''
