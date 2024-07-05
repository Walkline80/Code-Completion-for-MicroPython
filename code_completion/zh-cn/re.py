'''
简单正则表达式

此模块实现了相应`CPython`模块的子集，如下所述。

有关更多信息，请参阅原始`CPython`文档：[re](https://docs.python.org/3.5/library/re.html#module-re)。

该模块实现正则表达式操作。

支持的正则表达式语法是 CPython `re`模块的子集（实际上也是 POSIX 扩展正则表达式的子集）。

[查看文档](https://docs.micropython.org/en/latest/library/re.html)
'''
# Constants
DEBUG: bool = ...
'''
标志值，显示编译表达式的调试信息。

可用性取决于 MicroPython 端口。
'''


class Regex(object):
	'''
	已编译的正则表达式。

	该类的实例使用`re.compile()`创建。
	'''
	def match(self, string: str):
		'''
		类似于模块级函数`match()`。

		如果对多个字符串使用相同的正则表达式，则使用本方法的效率更高。
		'''

	def search(self, string: str):
		'''
		类似于模块级函数`search()`。

		如果对多个字符串使用相同的正则表达式，则使用本方法的效率更高。
		'''

	def sub(self, replace: str, string: str, count: int = 0, flags: int = 0, /):
		'''
		类似于模块级函数`sub()`。

		如果对多个字符串使用相同的正则表达式，则使用本方法的效率更高。
		'''

	def split(self, string: str, max_split: int = -1, /) -> list:
		'''
		使用正则表达式分割字符串。

		如果给定了`max_split`，则指定了要执行的最大拆分次数。

		返回字符串列表（如果指定了`max_split`参数，则最多可有`max_split + 1`个元素）。
		'''


class Match(object):
	'''
	匹配对象，由`match()`和`search()`等方法返回，并传递给`sub()`中的替换函数。
	'''
	def group(self, index: int) -> str:
		'''
		返回匹配的（子）字符串。

		`index`为 0 表示整个匹配，1 及以上表示每个捕获组。

		只支持数字组。
		'''

	def groups(self) -> tuple:
		'''
		返回包含匹配组所有子串的元组。

		注：此方法的可用性取决于 MicroPython 端口。
		'''

	def start(self, index: int = None) -> int:
		'''
		返回匹配的子字符串组的起始位置在原始字符串中的索引。

		`index`默认为整个组，否则将选择一个组。

		注意：这些方法的可用性取决于 MicroPython 端口。
		'''

	def end(self, index: int = None) -> int:
		'''
		返回匹配的子字符串组的末尾位置在原始字符串中的索引。

		`index`默认为整个组，否则将选择一个组。

		注意：这些方法的可用性取决于 MicroPython 端口。
		'''

	def span(self, index: int = None) -> tuple:
		'''
		返回双元组 `(match.start(index), match.end(index))`

		注意：此方法的可用性取决于 MicroPython 端口。
		'''


# Functions
def compile(regex_str, flags=None) -> Regex:
	'''编译正则表达式，返回`regex`对象。'''

def match(regex_str: str, string: str) -> Match:
	'''
	编译`regex_str`并与`string`匹配。

	匹配总是从字符串的起始位置开始。
	'''

def search(regex_str: str, string: str) -> Match:
	'''
	编译`regex_str`并在字符串中搜索。

	与`match`不同的是，它将搜索字符串中与正则表达式匹配的第一个位置
	（如果是锚定的，则仍可能为 0）。
	'''

def sub(regex_str: str, replace: str | function, string: str, count: int = 0, flags: int = 0, /) -> str:
	'''
	编译`regex_str`并在`string`中搜索，用`replace`替换所有匹配，并返回新字符串。

	`replace`可以是字符串或函数。

	如果是字符串，则可以使用`\<number>`和`\g<number>`形式的转义序列来扩展到相应的组
	（或空字符串表示未匹配的组）。

	如果`replace`是一个函数，那么它必须接受一个参数（`match`），并返回一个替换字符串。

	如果指定了`count`且非零，那么替换次数达到此值后就会停止。

	同时，`flags`参数将被忽略。

	注意：该函数的可用性取决于 MicroPython 端口。
	'''
