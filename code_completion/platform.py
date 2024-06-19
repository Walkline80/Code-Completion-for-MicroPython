'''
access to underlying platform’s identifying data

This module implements a subset of the corresponding CPython module, as described below.

For more information, refer to the original CPython documentation: platform.

This module tries to retrieve as much platform-identifying data as possible.

It makes this information available via function APIs.

[View Doc](https://docs.micropython.org/en/latest/library/platform.html)
'''
# Functions
def platform():
	'''
	Returns a string identifying the underlying platform.

	This string is composed of several substrings in the following order, delimited by dashes (-):

	- the name of the platform system (e.g. Unix, Windows or MicroPython)
	- the MicroPython version
	- the architecture of the platform
	- the version of the underlying platform
	- the concatenation of the name of the libc that MicroPython is linked to and its corresponding version.

	For example, this could be "MicroPython-1.20.0-xtensa-IDFv4.2.4-with-newlib3.0.0".
	'''

def python_compiler():
	'''Returns a string identifying the compiler used for compiling MicroPython.'''

def libc_ver():
	'''
	Returns a tuple of strings (lib, version), where lib is the name of the libc that MicroPython is linked to,

	and version the corresponding version of this libc.
	'''
