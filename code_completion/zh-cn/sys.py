'''
系统特定功能

此模块实现相应`CPython`模块的子集，如下所述。

有关详细信息，请参阅原始`CPython`文档：[sys](https://docs.python.org/3.5/library/sys.html#module-sys)。

[查看文档](https://docs.micropython.org/en/latest/library/sys.html)
'''
# Constants
stderr = ...
'''标准错误流。'''

stdin = ...
'''标准输入流。'''

stdout = ...
'''标准输出流。'''

argv: list = ...
'''启动当前程序时使用的可变列表参数。'''

byteorder: str = ...
'''系统的字节顺序（`little`或'big`）。'''

implementation: tuple = ...
'''
包含有关当前 Python 实现的信息的对象。

对于 MicroPython，它具有以下属性：

- `name` - 字符串 "micropython"
- `version` - 元组（主要版本号、次要版本号、微型版本号、发布级别），例如 （1, 22, 0, ''）
- `_machine` - 描述底层计算机的字符串
- `_mpy` - 支持的 MPY 文件格式版本（可选属性）

此对象是将 MicroPython 与其他 Python 实现区分开来的推荐方法（请注意，它可能仍然不存在于非常小的端口中）。

从版本 1.22.0-preview 开始，`implementation.version`中的第四个节点 `releaselevel`要么是空字符串，
要么是`preview`。

与 CPython 的区别：

	CPython 为此对象要求更多属性，但是在 MicroPython 中只实现实际有用的一少部分。
'''

maxsize: int = ...
'''
本机整数类型在当前平台上可以保存的最大值，或者说 MicroPython 整数类型可表示的最大值（如果它小于平台最大值），
对于没有 long int 支持的 MicroPython 端口就是这种情况。

此属性可用于检测平台的位数（32 位与 64 位等）。

建议不要将此属性直接与某个值进行比较，而是计算其中的位数。
'''

modules: dict = ...
'''
已加载模块的字典。

在某些端口上，它可能不包括内置模块。
'''

path: list = ...
'''用于搜索导入模块的可变目录列表。'''

platform: str = ...
'''运行 MicroPython 的平台。'''

ps1: str = ...
'''
保存字符串的可变属性，用于 REPL 提示符。

默认值给出的标准 Python 提示符为 ">>>"
'''

ps2: str = ...
'''
保存字符串的可变属性，用于 REPL 提示符。

默认值给出的标准 Python 提示符为 "...."
'''

tracebacklimit: int = ...
'''
一个可变属性，包含一个整数值，该值是异常中要存储的最大回溯条目数。

设置为 0 可禁用添加回溯。默认值为 1000。

注意：并非在所有端口上都可用。
'''

version: str = ...
'''此实现符合的 Python 语言版本，以字符串形式出现。'''

version_info: tuple = ...
'''
此实现符合的 Python 语言版本，作为 int 元组。

与 CPython 的区别：

	仅支持前三个版本号（主要版本号、次要版本号、微型版本号），并且只能按索引引用，而不能按名称引用。
'''

# Functions
def exit(retval: int = 0, /):
	'''
	使用给定的退出代码终止当前程序。

	实际上，此函数会引发为`SystemExit`异常。

	如果给定一个参数，则将其值作为`SystemExit`的参数给出。
	'''

def atexit(func: function | None):
	'''
	注册终止时调用的函数。

	`func`必须是无参数的可调用对象，或者是`None`以禁用调用。

	`atexit`函数将返回此函数设置的上一个值，该值最初为`None`。

	与 CPython 的区别：

		此函数是一个 MicroPython 扩展，旨在提供与 CPython 中的`atexit`模块类似的功能。
	'''

def print_exception(exc, file=stdout, /):
	'''
	打印异常，并追溯到类似文件的对象`file`（默认为`sys.stdout`）。

	与 CPython 的区别：

		这是出现在 CPython 的回溯模块中的函数的简化版本。

		与`traceback.print_exception()`不同，此函数只接受异常值，而不是异常类型、异常值和回溯对象;
		`file`参数应该是位置性的; 不支持进一步的参数。

		兼容 CPython 的回溯模块可以在`micropython-lib`中找到。
	'''

def settrace(tracefunc):
	'''
	启用字节码执行跟踪。有关详细信息，请参阅 CPython 文档。

	此函数需要自定义编译 MicroPython 固件，因为它通常不存在于预编译的固件中（因为它会影响性能）。

	相关配置选项为`MICROPY_PY_SYS_SETTRACE`。
	'''
