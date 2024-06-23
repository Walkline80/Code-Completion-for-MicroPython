'''
JSON encoding and decoding

This module implements a subset of the corresponding CPython module, as described
below.

For more information, refer to the original CPython documentation: json.

This modules allows to convert between Python objects and the JSON data format.

[View Doc](https://docs.micropython.org/en/latest/library/json.html)
'''
# Functions
def dump(obj, stream, separators=None):
	'''
	Serialise `obj` to a JSON string, writing it to the given `stream`.

	If specified, `separators` should be an (item_separator, key_separator) tuple.

	The default is (', ', ': ').

	To get the most compact JSON representation, you should specify (',', ':')
	to eliminate whitespace.
	'''

def dumps(obj, separators=None):
	'''
	Return `obj` represented as a JSON string.

	The arguments have the same meaning as in dump.
	'''

def load(stream):
	'''
	Parse the given `stream`, interpreting it as a JSON string and deserialising
	the data to a Python object.

	The resulting object is returned.

	Parsing continues until end-of-file is encountered.

	A `ValueError` is raised if the data in stream is not correctly formed.
	'''

def loads(str):
	'''
	Parse the JSON `str` and return an object.

	Raises `ValueError` if the string is not correctly formed.
	'''
