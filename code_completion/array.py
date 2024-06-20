'''
arrays of numeric data

This module implements a subset of the corresponding CPython module, as described below.

For more information, refer to the original CPython documentation: array.

Supported format codes: `b`, `B`, `h`, `H`, `i`, `I`, `l`, `L`, `q`, `Q`, `f`, `d` (the latter 2 depending on the floating-point support).

[View Doc](https://docs.micropython.org/en/latest/library/array.html)
'''
class array(object):
	def __init__(self, typecode, iterable=None):
		'''
		Create array with elements of given type.

		Initial contents of the array are given by `iterable`.

		If it is not provided, an empty array is created.
		'''

	def append(self, val):
		'''Append new element `val` to the end of array, growing it.'''

	def extend(self, iterable):
		'''Append new elements as contained in `iterable` to the end of array, growing it.'''

	def __getitem__(self, index):
		'''
		Indexed read of the array, called as `a[index]` (where `a` is an `array`).

		Returns a value if index is an `int` and an `array` if `index` is a slice.

		Negative indices count from the end and `IndexError` is thrown if the index is out of range.

		Note:

			`__getitem__` cannot be called directly (`a.__getitem__(index)` fails) and is not present in `__dict__`, however `a[index]` does work.
		'''

	def __setitem__(self, index, value):
		'''
		Indexed write into the array, called as `a[index] = value` (where `a` is an `array`).

		`value` is a single value if `index` is an `int` and an `array` if index is a slice.

		Negative indices count from the end and `IndexError` is thrown if the index is out of range.

		Note:

			`__setitem__` cannot be called directly (`a.__setitem__(index, value)` fails) and is not present in `__dict__`, however `a[index] = value` does work.
		'''

	def __len__(self) -> int:
		'''
		Returns the number of items in the array, called as `len(a)` (where `a` is an `array`).

		Note:

			`__len__` cannot be called directly (`a.__len__()` fails) and the method is not present in `__dict__`, however `len(a)` does work.
		'''

	def __add__(self, other):
		'''
		Return a new `array` that is the concatenation of the array with `other`, called as `a + other` (where `a` and `other` are both `arrays`).

		Note:

			`__add__` cannot be called directly (`a.__add__(other)` fails) and is not present in `__dict__`, however `a + other` does work.
		'''

	def __iadd__(self, other):
		'''
		Concatenates the array with `other` in-place, called as `a += other` (where `a` and `other` are both `arrays`).

		Equivalent to `extend(other)`.

		Note:

			`__iadd__` cannot be called directly (`a.__iadd__(other)` fails) and is not present in `__dict__`, however `a += other` does work.
		'''

	def __repr__(self) -> str:
		'''
		Returns the string representation of the array, called as `str(a)` or `repr(a)` (where `a` is an `array`).

		Returns the string `"array(<type>, [<elements>])"`, where `<type>` is the type code letter for the array and `<elements>` is a comma separated list of the elements of the array.

		Note:

			`__repr__` cannot be called directly (`a.__repr__()` fails) and is not present in `__dict__`, however `str(a)` and `repr(a)` both work.
		'''
