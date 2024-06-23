'''
mathematical functions for complex numbers

This module implements a subset of the corresponding CPython module, as described
below.

For more information, refer to the original CPython documentation: cmath.

The cmath module provides some basic mathematical functions for working with
complex numbers.

Availability: not available on WiPy and ESP8266. Floating point support required
for this module.

[View Doc](https://docs.micropython.org/en/latest/library/cmath.html)
'''
# Constants
e = ...
'''base of the natural logarithm'''

pi = ...
'''the ratio of a circle’s circumference to its diameter'''

# Functions
def cos(z):
	'''Return the cosine of `z`.'''

def exp(z):
	'''Return the exponential of `z`.'''

def log(z):
	'''
	Return the natural logarithm of `z`.

	The branch cut is along the negative real axis.
	'''

def log10(z):
	'''
	Return the base-10 logarithm of `z`.

	The branch cut is along the negative real axis.
	'''

def phase(z):
	'''Returns the phase of the number `z`, in the range (-pi, +pi].'''

def polar(z):
	'''Returns, as a tuple, the polar form of `z`.'''

def rect(r, phi):
	'''Returns the complex number with modulus `r` and phase `phi`.'''

def sin(z):
	'''Return the sine of `z`.'''

def sqrt(z):
	'''Return the square-root of `z`.'''
