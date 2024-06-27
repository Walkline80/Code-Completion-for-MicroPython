'''
访问底层平台的识别数据

此模块实现相应`CPython`模块的子集，如下所述。

有关详细信息，请参阅原始`CPython`文档：[platform](https://docs.python.org/3.5/library/platform.html#module-platform)。

此模块尝试检索尽可能多的平台标识数据。

它通过函数 API 提供此信息。

[查看文档](https://docs.micropython.org/en/latest/library/platform.html)
'''
# Functions
def platform() -> str:
	'''
	返回标识基础平台的字符串。

	此字符串按以下顺序由多个子字符串组成，用短划线（-）分隔：

	- 平台系统的名称（例如 Unix、Windows 或 MicroPython）
	- MicroPython 版本
	- 平台的架构
	- 底层平台的版本
	- MicroPython 链接到的 libc 名称及其对应版本的串联

	例如`MicroPython-1.20.0-xtensa-IDFv4.2.4-with-newlib3.0.0`。
	'''

def python_compiler() -> str:
	'''返回一个字符串，标识用于编译 MicroPython 的编译器。'''

def libc_ver():
	'''
	返回字符串元组`(lib, version)`，其中`lib`是 MicroPython 链接到的 libc 的名称，`version`是此 libc 的相应版本。
	'''
