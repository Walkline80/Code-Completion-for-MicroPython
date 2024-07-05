'''
simple regular expressions

This module implements a subset of the corresponding `CPython` module, as described
below.

For more information, refer to the original `CPython` documentation: [re](https://docs.python.org/3.5/library/re.html#module-re).

This module implements regular expression operations.

Regular expression syntax supported is a subset of CPython `re` module (and actually
is a subset of POSIX extended regular expressions).

[View Doc](https://docs.micropython.org/en/latest/library/re.html)
'''
# Constants
DEBUG: bool = ...
'''
Flag value, display debug information about compiled expression.

Availability depends on MicroPython port.
'''


class Regex(object):
	'''
	Compiled regular expression.

	Instances of this class are created using `re.compile()`.
	'''
	def match(self, string: str):
		'''
		Similar to the module-level function `match()`.

		Using methods is (much) more efficient if the same regex is applied to
		multiple strings.
		'''

	def search(self, string: str):
		'''
		Similar to the module-level function `search()`.

		Using methods is (much) more efficient if the same regex is applied to
		multiple strings.
		'''

	def sub(self, replace: str, string: str, count: int = 0, flags: int = 0, /):
		'''
		Similar to the module-level function`sub()`.

		Using methods is (much) more efficient if the same regex is applied to
		multiple strings.
		'''

	def split(self, string: str, max_split: int = -1, /) -> list:
		'''
		Split a `string` using regex.

		If `max_split` is given, it specifies maximum number of splits to perform.

		Returns list of strings (there may be up to max_split+1 elements if it’s
		specified).
		'''


class Match(object):
	'''
	Match objects as returned by `match()` and `search()` methods, and passed to
	the replacement function in `sub()`.
	'''
	def group(self, index: int) -> str:
		'''
		Return matching (sub)string.

		`index` is 0 for entire match, 1 and above for each capturing group.

		Only numeric groups are supported.
		'''

	def groups(self) -> tuple:
		'''
		Return a tuple containing all the substrings of the groups of the match.

		Note: availability of this method depends on MicroPython port.
		'''

	def start(self, index: int = None) -> int:
		'''
		Return the index in the original string of the start of the substring
		group that was matched.

		`index` defaults to the entire group, otherwise it will select a group.

		Note: availability of these methods depends on MicroPython port.
		'''

	def end(self, index: int = None) -> int:
		'''
		Return the index in the original string of the end of the substring group
		that was matched.

		`index` defaults to the entire group, otherwise it will select a group.

		Note: availability of these methods depends on MicroPython port.
		'''

	def span(self, index: int = None) -> tuple:
		'''
		Returns the 2-tuple `(match.start(index), match.end(index))`.

		Note: availability of this method depends on MicroPython port.
		'''


# Functions
def compile(regex_str, flags=None) -> Regex:
	'''Compile regular expression, return `regex` object.'''

def match(regex_str: str, string: str) -> Match:
	'''
	Compile `regex_str` and match against `string`.

	Match always happens from starting position in a string.
	'''

def search(regex_str: str, string: str) -> Match:
	'''
	Compile `regex_str` and search it in a `string`.

	Unlike `match`, this will search string for first position which matches regex
	(which still may be 0 if regex is anchored).
	'''

def sub(regex_str: str, replace: str | function, string: str, count: int = 0, flags: int = 0, /) -> str:
	'''
	Compile `regex_str` and search for it in `string`, replacing all matches with
	`replace`, and returning the new string.

	`replace` can be a string or a function.

	If it is a string then escape sequences of the form `\<number>` and `\g<number>`
	can be used to expand to the corresponding group (or an empty string for
	unmatched groups).

	If `replace` is a function then it must take a single argument (the match)
	and should return a replacement string.

	If `count` is specified and non-zero then substitution will stop after this
	many substitutions are made.

	The `flags` argument is ignored.

	Note: availability of this function depends on MicroPython port.
	'''
