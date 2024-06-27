'''
JSON 编码和解码

此模块实现相应`CPython`模块的子集，如下所述。

有关更多信息，请参阅原始`CPython文档：[json](https://docs.python.org/3.5/library/json.html#module-json)。

该模块允许在 Python 对象和 JSON 数据格式之间进行转换。

[查看文档](https://docs.micropython.org/en/latest/library/json.html)
'''
# Functions
def dump(obj, stream, separators: tuple = None):
	'''
	将`obj`序列化为 JSON 字符串，将其写入给定的`stream`。

	如果指定，`separators`应为`(item_separator, key_separator)`元组。

	默认值为`(', ', ': ')`。

	若要获得最紧凑的 JSON 表示形式，应指定`(',', ':')以消除空格。
	'''

def dumps(obj, separators: tuple = None) -> str:
	'''
	返回表示为 JSON 字符串的`obj`。

	这些参数的含义与`dump`的含义相同。
	'''

def load(stream):
	'''
	请将给定的`stream`解析为 JSON 字符串，并将数据反序列化为 Python 对象。

	返回生成的对象。

	解析将继续，直到遇到文件结尾。

	如果`stream`中的数据格式不正确，将引发`ValueError`。
	'''

def loads(str: str):
	'''
	解析 JSON 字符串`str`并返回一个对象。

	如果字符串格式不正确，将引发`ValueError`。
	'''
