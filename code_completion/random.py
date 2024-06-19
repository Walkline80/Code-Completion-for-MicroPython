'''
generate random numbers

This module implements a pseudo-random number generator (PRNG).

This module implements a subset of the corresponding CPython module, as described below.

For more information, refer to the original CPython documentation: random.

Note:

	The `randrange()`, `randint()` and `choice()` functions are only available if the `MICROPY_PY_RANDOM_EXTRA_FUNCS` configuration option is enabled.

[View Doc](https://docs.micropython.org/en/latest/library/random.html)
'''
# Functions for integers
def getrandbits(n: int) -> int:
	'''Return an integer with `n` random bits (0 <= n <= 32).'''

def randint(a: int, b: int) -> int:
	'''Return a random integer in the range `[a, b]`.'''

def randrange(start: int = None, stop: int = None, step: int = None) -> int:
	'''
	- `randrange(stop)` returns a random integer from the range `[0, stop]`.

	- `randrange(start, stop)` returns a random integer from the range `[start, stop]`.

	- `randrange(start, stop[, step])` returns a random integer from the range `[start, stop]` in steps of `step`.

	For instance, calling randrange(1, 10, 2) will return odd numbers between 1 and 9 inclusive.
	'''

# Functions for floats
def random():
	'''Return a random floating point number in the range [0.0, 1.0).'''

def uniform(a, b):
	'''Return a random floating point number N such that `a` <= N <= `b` for `a` <= `b`, and `b` <= N <= `a` for `b` < `a`.'''

# Other Functions
def seed(n: int = None, /):
	'''
	Initialise the random number generator module with the seed `n` which should be an integer.

	When no argument (or None) is passed in it will (if supported by the port) initialise the PRNG with a true random number (usually a hardware generated random number).

	The None case only works if `MICROPY_PY_RANDOM_SEED_INIT_FUNC` is enabled by the port, otherwise it raises `ValueError`.
	'''

def choice(sequence):
	'''Chooses and returns one item at random from `sequence` (tuple, list or any object that supports the subscript operation).'''
