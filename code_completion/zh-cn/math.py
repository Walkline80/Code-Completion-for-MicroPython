'''
mathematical functions

This module implements a subset of the corresponding CPython module, as described
below.

For more information, refer to the original CPython documentation: math.

The math module provides some basic mathematical functions for working with
floating-point numbers.

Note: On the pyboard, floating-point numbers have 32-bit precision.

Availability: Not available on WiPy. Floating point support required for this
module.

[View Doc](https://docs.micropython.org/en/latest/library/math.html)
'''
# Functions
def acos(x):
	'''Return the inverse cosine of `x`.'''

def acosh(x):
	'''Return the inverse hyperbolic cosine of `x`.'''

def asin(x):
	'''Return the inverse sine of `x`.'''

def asinh(x):
	'''Return the inverse hyperbolic sine of `x`.'''

def atan(x):
	'''Return the inverse tangent of `x`.'''

def atan2(y, x):
	'''Return the principal value of the inverse tangent of `y/x`.'''

def atanh(x):
	'''Return the inverse hyperbolic tangent of `x`.'''

def ceil(x) -> int:
	'''Return an integer, being `x` rounded towards positive infinity.'''

def copysign(x, y):
	'''Return `x` with the sign of `y`.'''

def cos(x):
	'''Return the cosine of `x`.'''

def cosh(x):
	'''Return the hyperbolic cosine of `x`.'''

def degrees(x):
	'''Return radians `x` converted to degrees.'''

def erf(x):
	'''Return the error function of `x`.'''

def erfc(x):
	'''Return the complementary error function of `x`.'''

def exp(x):
	'''Return the exponential of `x`.'''

def expm1(x):
	'''Return `exp(x) - 1`.'''

def fabs(x):
	'''Return the absolute value of `x`.'''

def floor(x) -> int:
	'''Return an integer, being `x` rounded towards negative infinity.'''

def fmod(x, y):
	'''Return the remainder of `x/y`.'''

def frexp(x):
	'''
	Decomposes a floating-point number into its mantissa and exponent.

	The returned value is the tuple (m, e) such that x == m * 2**e exactly.

	If x == 0 then the function returns (0.0, 0), otherwise the relation 0.5 <=
	abs(m) < 1 holds.
	'''

def gamma(x):
	'''Return the gamma function of `x`.'''

def isfinite(x):
	'''Return True if `x` is finite.'''

def isinf(x):
	'''Return True if `x` is infinite.'''

def isnan(x):
	'''Return True if `x` is not-a-number'''

def ldexp(x, exp):
	'''Return `x * (2**exp)`.'''

def lgamma(x):
	'''Return the natural logarithm of the gamma function of `x`.'''

def log(x):
	'''Return the natural logarithm of `x`.'''

def log10(x):
	'''Return the base-10 logarithm of `x`.'''

def log2(x):
	'''Return the base-2 logarithm of `x`.'''

def modf(x):
	'''
	Return a tuple of two floats, being the fractional and integral parts of `x`.

	Both return values have the same sign as `x`.
	'''

def pow(x, y):
	'''Returns `x` to the power of `y`.'''

def radians(x):
	'''Return degrees `x` converted to radians.'''

def sin(x):
	'''Return the sine of `x`.'''

def sinh(x):
	'''Return the hyperbolic sine of `x`.'''

def sqrt(x):
	'''Return the square root of `x`.'''

def tan(x):
	'''Return the tangent of `x`.'''

def tanh(x):
	'''Return the hyperbolic tangent of `x`.'''

def trunc(x) -> int:
	'''Return an integer, being `x` rounded towards 0.'''

# Constants
e: float = ...
'''base of the natural logarithm'''

pi: float = ...
'''the ratio of a circle’s circumference to its diameter'''
