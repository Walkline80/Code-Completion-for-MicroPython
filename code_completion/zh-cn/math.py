'''
数学函数

此模块实现相应`CPython`模块的子集，如下所述。有关详细信息，请参阅原始`CPython`文档：[math](https://docs.python.org/3.5/library/math.html#module-math)。

`math`模块提供了一些用于处理浮点数的基本数学函数。

注意：在 pyboard 上，浮点数具有 32 位精度。

可用性：在 WiPy 上不可用。此模块需要浮点支持。

[查看文档](https://docs.micropython.org/en/latest/library/math.html)
'''
# Constants
e: float = ...
'''自然对数的底'''

pi: float = ...
'''圆的周长与其直径的比值'''

# Functions
def acos(x):
	'''返回`x`的反余弦。'''

def acosh(x):
	'''返回`x`的反双曲余弦。'''

def asin(x):
	'''返回`x`的反正弦。'''

def asinh(x):
	'''返回`x`的反双曲正弦。'''

def atan(x):
	'''返回`x`的反正切。'''

def atan2(y, x):
	'''返回`y/x`的反正切的主值。'''

def atanh(x):
	'''返回`x`的反双曲正切。'''

def ceil(x) -> int:
	'''返回一个整数，将`x`舍入到正无穷大。'''

def copysign(x, y):
	'''返回带有符号`y`的`x`。'''

def cos(x):
	'''返回`x`的余弦。'''

def cosh(x):
	'''返回`x`的双曲余弦。'''

def degrees(x):
	'''将弧度`x`转换为度数。'''

def erf(x):
	'''返回`x`的错误函数。'''

def erfc(x):
	'''返回`x`的互补误差函数。'''

def exp(x):
	'''返回`x`的指数。'''

def expm1(x):
	'''返回`exp(x) - 1`。'''

def fabs(x):
	'''返回`x`的绝对值。'''

def floor(x) -> int:
	'''返回一个整数，将`x`舍入到负无穷大。'''

def fmod(x, y):
	'''返回`x/y`的余数。'''

def frexp(x) -> tuple:
	'''
	将浮点数分解为其尾数和指数。

	返回的值是元组`(m, e)`，使得`x == m * 2**e`成立。

	如果`x == 0`，则函数返回`(0.0， 0)`，否则关系式`0.5 <= abs(m) < 1`成立。
	'''

def gamma(x):
	'''返回`x`的 gamma 函数。'''

def isfinite(x) -> bool:
	'''如果`x`是有限的，则返回`True`。'''

def isinf(x) -> bool:
	'''如果`x`无穷大，则返回`True`。'''

def isnan(x) -> bool:
	'''如果`x`不是数字，则返回`True`'''

def ldexp(x, exp):
	'''返回`x * (2**exp)`。'''

def lgamma(x):
	'''返回`x`的 gamma 函数的自然对数。'''

def log(x):
	'''返回`x`的自然对数。'''

def log10(x):
	'''返回`x`的以 10 为底的对数。'''

def log2(x):
	'''返回`x`的以 2 为底的对数。'''

def modf(x):
	'''
	返回两个浮点数的元组，它们是`x`的分数和整数部分。

	两个返回值都具有与`x`相同的符号。
	'''

def pow(x, y):
	'''返回`x`的`y`次方。'''

def radians(x):
	'''将度数`x`转换为弧度。'''

def sin(x):
	'''返回`x`的正弦值。'''

def sinh(x):
	'''返回`x`的双曲正弦。'''

def sqrt(x):
	'''返回`x`的平方根。'''

def tan(x):
	'''返回`x`的正切。'''

def tanh(x):
	'''返回`x`的双曲正切。'''

def trunc(x) -> int:
	'''返回一个整数，将`x`舍入到 0。'''
