'''
复数的数学函数

此模块实现相应`CPython`模块的子集，如下所述。

有关更多信息，请参阅原始`CPython`文档：[cmath](https://docs.python.org/3.5/library/cmath.html#module-cmath)。

`cmath`模块提供了一些用于处理复数的基本数学函数。

可用性：在 WiPy 和 ESP8266 上不可用。此模块需要浮点支持。

[查看文档](https://docs.micropython.org/en/latest/library/cmath.html)
'''
# Constants
e: float = ...
'''自然对数的底'''

pi: float = ...
'''圆的周长与其直径的比值'''

# Functions
def cos(z):
	'''返回`z`的余弦.'''

def exp(z):
	'''返回`z`的指数。'''

def log(z):
	'''
	返回`z`的自然对数。

	分支沿负实轴切割。
	'''

def log10(z):
	'''
	返回`z`的以 10 为底的对数。

	分支沿负实轴切割。
	'''

def phase(z):
	'''返回数字`z`的相位，范围为`(-pi, +pi)`。'''

def polar(z) -> tuple:
	'''以元组形式返回`z`的极化形式。'''

def rect(r, phi):
	'''返回具有模数`r`和相位`phi`的复数。'''

def sin(z):
	'''返回`z`的正弦。'''

def sqrt(z):
	'''返回`z`的平方根。'''
