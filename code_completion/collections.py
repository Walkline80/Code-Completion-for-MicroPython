'''
collection and container types

This module implements a subset of the corresponding CPython module, as described below.

For more information, refer to the original CPython documentation: collections.

This module implements advanced collection and container types to hold/accumulate various objects.

[View Doc](https://docs.micropython.org/en/latest/library/collections.html)
'''
class deque(object):
	def __init__(self, iterable, maxlen: int, flags=None):
		'''
		Deques (double-ended queues) are a list-like container that support O(1) appends and pops from either side of the deque.

		New deques are created using the following arguments:

		- `iterable` is an iterable used to populate the deque when it is created.

			It can be an empty tuple or list to create a deque that is initially empty.

		- `maxlen` must be specified and the deque will be bounded to this maximum length.

			Once the deque is full, any new items added will discard items from the opposite end.

		- The optional `flags` can be 1 to check for overflow when adding items.

		Deque objects support `bool`, `len`, iteration and subscript load and store.
		'''

	def append(self, x):
		'''
		Add `x` to the right side of the deque.

		Raises `IndexError` if overflow checking is enabled and there is no more room in the queue.
		'''

	def appendleft(self, x):
		'''
		Add `x` to the left side of the deque.

		Raises `IndexError` if overflow checking is enabled and there is no more room in the queue.
		'''

	def pop(self):
		'''
		Remove and return an item from the right side of the deque.

		Raises `IndexError` if no items are present.
		'''

	def popleft(self):
		'''
		Remove and return an item from the left side of the deque.

		Raises `IndexError` if no items are present.
		'''

	def extend(self, iterable):
		'''
		Extend the deque by appending all the items from `iterable` to the right of the deque.

		Raises `IndexError` if overflow checking is enabled and there is no more room in the deque.
		'''


def namedtuple(name: str, fields):
	'''
	This is factory function to create a new namedtuple type with a specific name and set of fields.

	A namedtuple is a subclass of tuple which allows to access its fields not just by numeric index, but also with an attribute access syntax using symbolic field names.

	Fields is a sequence of strings specifying field names.

	For compatibility with CPython it can also be a string with space-separated field named (but this is less efficient).
	'''


class OrderedDict(object):
	'''
	`dict` type subclass which remembers and preserves the order of keys added.

	When ordered dict is iterated over, keys/items are returned in the order they were added.
	'''
