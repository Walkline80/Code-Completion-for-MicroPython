'''
生成随机数

该模块实现了伪随机数生成器（PRNG）。

此模块实现相应`CPython`模块的子集，如下所述。

有关更多信息，请参阅原始`CPython`文档：[random](https://docs.python.org/3.5/library/random.html#module-random)。

注意：

	`randrange()`、`randint()`和`choice()`函数仅在启用`MICROPY_PY_RANDOM_EXTRA_FUNCS`配置选项时可用。

[查看文档](https://docs.micropython.org/en/latest/library/random.html)
'''
import typing


# Functions for integers
def getrandbits(n: int) -> int:
	'''返回一个具有`n`个随机位的整数（0 <= n <= 32）。'''

def randint(a: int, b: int) -> int:
	'''返回`[a, b]`范围内的随机整数。'''

@typing.overload
def randrange(stop: int) -> int:
	'''返回`[0, stop]`范围内的随机整数。'''

@typing.overload
def randrange(start: int = None, stop: int = None) -> int:
	'''返回`[start, stop]`范围内的随机整数。'''

@typing.overload
def randrange(start: int, stop: int, step: int = None) -> int:
	'''
	以步长`step`从范围`[start, stop]`返回一个随机整数。

	例如，调用`randrange(1, 10, 2)`将返回 1 到 9 之间的奇数。
	'''

# Functions for floats
def random() -> float:
	'''返回`[0.0, 1.0]`范围内的随机浮点数。'''

def uniform(a, b) -> float:
	'''
	返回一个随机浮点数 N，使得当`a <= b`时`a <= N <= b`，当`b < a`时`b <= N <= a`。
	'''

# Other Functions
def seed(n: int = None, /):
	'''
	使用种子`n`初始化随机数生成器模块，种子`n`应为整数。

	当没有传入参数（或 `None`）时，它将（如果端口支持）使用真正的随机数
	（通常是硬件生成的随机数）初始化 PRNG。

	`None`情况仅在端口启用`MICROPY_PY_RANDOM_SEED_INIT_FUNC`时才有效，否则会引发`ValueError`。
	'''

def choice(sequence: typing.Any) -> typing.Any:
	'''
	从`sequence`（元组、列表或任何支持下标操作的对象）中随机选择并返回一个项目。
	'''
