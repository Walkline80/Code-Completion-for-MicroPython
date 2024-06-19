'''
simple BTree database

The btree module implements a simple key-value database using external storage (disk files, or in general case, a random-access stream).

Keys are stored sorted in the database, and besides efficient retrieval by a key value, a database also supports efficient ordered range scans (retrieval of values with the keys in a given range).

On the application interface side, BTree database work as close a possible to a way standard dict type works, one notable difference is that both keys and values must be bytes-like objects (so, if you want to store objects of other types, you need to first serialize them to str or bytes or another type that supports the buffer protocol).

The module is based on the well-known BerkelyDB library, version 1.xx.
'''
# Docs: https://docs.micropython.org/en/latest/library/btree.html

# Functions
def open(stream, *, flags: int = 0, pagesize: int = 0, cachesize: int = 0, minkeypage: int = 0):
	'''
	Open a database from a random-access `stream` (like an open file).

	All other parameters are optional and keyword-only, and allow to tweak advanced parameters of the database operation (most users will not need them):

	- `flags` - Currently unused.

	- `pagesize` - Page size used for the nodes in BTree.

		Acceptable range is 512-65536.

		If 0, a port-specific default will be used, optimized for port’s memory usage and/or performance.

	- `cachesize` - Suggested memory cache size in bytes.

		For a board with enough memory using larger values may improve performance.

		Cache policy is as follows: entire cache is not allocated at once;

		instead, accessing a new page in database will allocate a memory buffer for it, until value specified by cachesize is reached.

		Then, these buffers will be managed using LRU (least recently used) policy.

		More buffers may still be allocated if needed (e.g., if a database contains big keys and/or values).

		Allocated cache buffers aren’t reclaimed.

	- `minkeypage` - Minimum number of keys to store per page. Default value of 0 equivalent to 2.

	Returns a BTree object, which implements a dictionary protocol (set of methods), and some additional methods described below.
	'''

# Methods
def close():
	'''
	Close the database.

	It’s mandatory to close the database at the end of processing, as some unwritten data may be still in the cache.

	Note that this does not close underlying stream with which the database was opened, it should be closed separately (which is also mandatory to make sure that data flushed from buffer to the underlying storage).
	'''

def flush():
	'''Flush any data in cache to the underlying stream.'''

def __getitem__(key):
	'''Standard dictionary methods.'''

def get(key, default=None, /):
	'''Standard dictionary methods.'''

def __setitem__(key, val):
	'''Standard dictionary methods.'''

def __delitem__(key):
	'''Standard dictionary methods.'''

def __contains__(key):
	'''Standard dictionary methods.'''

def __iter__():
	'''
	A BTree object can be iterated over directly (similar to a dictionary) to get access to all keys in order.
	'''

def keys(start_key=None, end_key=None, flags=None):
	'''
	These methods are similar to standard dictionary methods, but also can take optional parameters to iterate over a key sub-range, instead of the entire database.

	Note that for all 3 methods, `start_key` and `end_key` arguments represent key values.

	For example, `values()` method will iterate over values corresponding to they key range given.

	None values for `start_key` means "from the first key", no `end_key` or its value of None means "until the end of database".

	By default, range is inclusive of `start_key` and exclusive of `end_key`, you can include `end_key` in iteration by passing `flags` of btree.INCL.

	You can iterate in descending key direction by passing `flags` of btree.DESC.

	The flags values can be ORed together.
	'''

def values(start_key=None, end_key=None, flags=None):
	'''
	These methods are similar to standard dictionary methods, but also can take optional parameters to iterate over a key sub-range, instead of the entire database.

	Note that for all 3 methods, `start_key` and `end_key` arguments represent key values.

	For example, `values()` method will iterate over values corresponding to they key range given.

	None values for `start_key` means "from the first key", no `end_key` or its value of None means "until the end of database".

	By default, range is inclusive of `start_key` and exclusive of `end_key`, you can include `end_key` in iteration by passing `flags` of btree.INCL.

	You can iterate in descending key direction by passing `flags` of btree.DESC.

	The flags values can be ORed together.
	'''

def items(start_key=None, end_key=None, flags=None):
	'''
	These methods are similar to standard dictionary methods, but also can take optional parameters to iterate over a key sub-range, instead of the entire database.

	Note that for all 3 methods, `start_key` and `end_key` arguments represent key values.

	For example, `values()` method will iterate over values corresponding to they key range given.

	None values for `start_key` means "from the first key", no `end_key` or its value of None means "until the end of database".

	By default, range is inclusive of `start_key` and exclusive of `end_key`, you can include `end_key` in iteration by passing `flags` of btree.INCL.

	You can iterate in descending key direction by passing `flags` of btree.DESC.

	The flags values can be ORed together.
	'''

# Constants
INCL = ...
DESC = ...
