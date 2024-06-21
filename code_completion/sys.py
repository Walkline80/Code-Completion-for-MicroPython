'''
system specific functions

This module implements a subset of the corresponding CPython module, as described below.

For more information, refer to the original CPython documentation: sys.

[View Doc](https://docs.micropython.org/en/latest/library/sys.html)
'''
# Constants
stderr = ...
'''Standard error stream.'''

stdin = ...
'''Standard input stream.'''

stdout = ...
'''Standard output stream.'''

# Functions
def exit(retval: int = 0, /):
	'''
	Terminate current program with a given exit code.

	Underlyingly, this function raise as `SystemExit` exception.

	If an argument is given, its value given as an argument to `SystemExit`.
	'''

def atexit(func: function | None):
	'''
	Register func to be called upon termination.

	`func` must be a callable that takes no arguments, or None to disable the call.

	The atexit function will return the previous value set by this function, which is initially None.

	Difference to CPython:

		This function is a MicroPython extension intended to provide similar functionality to the atexit module in CPython.
	'''

def print_exception(exc, file=stdout, /):
	'''
	Print exception with a traceback to a file-like object `file` (or `sys.stdout` by default).

	Difference to CPython:

		This is simplified version of a function which appears in the traceback module in CPython.

		Unlike `traceback.print_exception()`, this function takes just exception value instead of exception type, exception value, and traceback object; file argument should be positional; further arguments are not supported.

		CPython-compatible traceback module can be found in `micropython-lib`.
	'''

def settrace(tracefunc):
	'''
	Enable tracing of bytecode execution. For details see the CPython documentation.

	This function requires a custom MicroPython build as it is typically not present in pre-built firmware (due to it affecting performance).

	The relevant configuration option is `MICROPY_PY_SYS_SETTRACE`.
	'''

# Constants
argv = ...
'''A mutable list of arguments the current program was started with.'''

byteorder = ...
'''The byte order of the system ("little" or "big").'''

implementation = ...
'''
Object with information about the current Python implementation.

For MicroPython, it has following attributes:

- name - string "micropython"
- version - tuple (major, minor, micro, releaselevel), e.g. (1, 22, 0, ‘’)
- _machine - string describing the underlying machine
- _mpy - supported mpy file-format version (optional attribute)

This object is the recommended way to distinguish MicroPython from other Python implementations (note that it still may not exist in the very minimal ports).

Starting with version 1.22.0-preview, the fourth node releaselevel in `implementation.version` is either an empty string or "preview".

Difference to CPython:

	CPython mandates more attributes for this object, but the actual useful bare minimum is implemented in MicroPython.
'''

maxsize = ...
'''
Maximum value which a native integer type can hold on the current platform, or maximum value representable by MicroPython integer type, if it’s smaller than platform max value (that is the case for MicroPython ports without long int support).

This attribute is useful for detecting "bitness" of a platform (32-bit vs 64-bit, etc.).

It’s recommended to not compare this attribute to some value directly, but instead count number of bits in it:
'''

modules = ...
'''
Dictionary of loaded modules.

On some ports, it may not include builtin modules.
'''

path = ...
'''A mutable list of directories to search for imported modules.'''

platform = ...
'''The platform that MicroPython is running on.'''

ps1 = ...
'''
Mutable attributes holding strings, which are used for the REPL prompt.

The defaults give the standard Python prompt of >>>
'''

ps2 = ...
'''
Mutable attributes holding strings, which are used for the REPL prompt.

The defaults give the standard Python prompt of ....
'''

tracebacklimit = ...
'''
A mutable attribute holding an integer value which is the maximum number of traceback entries to store in an exception.

Set to 0 to disable adding tracebacks. Defaults to 1000.

Note: this is not available on all ports.
'''

version = ...
'''Python language version that this implementation conforms to, as a string.'''

version_info = ...
'''
Python language version that this implementation conforms to, as a tuple of ints.

Difference to CPython:

	Only the first three version numbers (major, minor, micro) are supported and they can be referenced only by index, not by name.
'''
