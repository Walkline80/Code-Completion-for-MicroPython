'''
wait for events on a set of streams

This module implements a subset of the corresponding CPython module, as described below.

For more information, refer to the original CPython documentation: select.

This module provides functions to efficiently wait for events on multiple streams (select streams which are ready for operations).

[View Doc](https://docs.micropython.org/en/latest/library/select.html)
'''
# Constants
from typing import overload


POLLIN: int = ...
POLLOUT: int = ...
POLLERR: int = ...
POLLHUP: int = ...


class Poll(object):
	# Methods
	def register(self, obj, eventmask: int = POLLIN | POLLOUT):
		'''
		Register `stream` obj for polling.

		`eventmask` is logical OR of:

		- `select.POLLIN` - data available for reading
		- `select.POLLOUT` - more data can be written

		Note that flags like `select.POLLHUP` and `select.POLLERR` are not valid
		as input eventmask (these are unsolicited events which will be returned
		from `poll()` regardless of whether they are asked for).

		This semantics is per POSIX.

		`eventmask` defaults to `select.POLLIN | select.POLLOUT`.

		It is OK to call this function multiple times for the same `obj`.

		Successive calls will update `obj`’s eventmask to the value of `eventmask`
		(i.e. will behave as `modify()`).
		'''

	def unregister(self, obj):
		'''Unregister obj from polling.'''

	def modify(self, obj, eventmask: int):
		'''
		Modify the `eventmask` for `obj`.

		If `obj` is not registered, `OSError` is raised with error of ENOENT.
		'''

	@overload
	def poll(self) -> tuple:
		'''
		Wait for at least one of the registered objects to become ready or have
		an exceptional condition, there is no timeout).

		Returns list of `(`obj`, `event`, …)` tuples.

		There may be other elements in tuple, depending on a platform and version,
		so don’t assume that its size is 2.

		The `event` element specifies which events happened with a stream and is
		a combination of `select.POLL*` constants described above.

		Note that flags `select.POLLHUP` and `select.POLLERR` can be returned at
		any time (even if were not asked for), and must be acted on accordingly
		(the corresponding stream unregistered from poll and likely closed),
		because otherwise all further invocations of `poll()` may return
		immediately with these flags set for this stream again.

		In case of timeout, an empty list is returned.
		'''

	@overload
	def poll(self, timeout: int = -1, /) -> tuple:
		'''
		Wait for at least one of the registered objects to become ready or have
		an exceptional condition.

		Returns list of `(`obj`, `event`, …)` tuples.

		There may be other elements in tuple, depending on a platform and version,
		so don’t assume that its size is 2.

		The `event` element specifies which events happened with a stream and is
		a combination of `select.POLL*` constants described above.

		Note that flags `select.POLLHUP` and `select.POLLERR` can be returned at
		any time (even if were not asked for), and must be acted on accordingly
		(the corresponding stream unregistered from poll and likely closed),
		because otherwise all further invocations of `poll()` may return
		immediately with these flags set for this stream again.

		In case of timeout, an empty list is returned.
		'''

	def ipoll(self, timeout: int = -1, flags: int = 0, /):
		'''
		Like `poll.poll()`, but instead returns an iterator which yields a
		`callee-owned tuple`.

		This function provides an efficient, allocation-free way to poll on
		streams.

		If `flags` is 1, one-shot behaviour for events is employed: streams for
		which events happened will have their event masks automatically reset (
		equivalent to `poll.modify(obj, 0)`), so new events for such a stream
		won’t be processed until new mask is set with `poll.modify()`.

		This behaviour is useful for asynchronous I/O schedulers.

		Difference to CPython:

			This function is a MicroPython extension.
		'''


# Functions
def poll() -> Poll:
	'''Create an instance of the Poll class.'''

def select(rlist, wlist, xlist, timeout=None):
	'''
	Wait for activity on a set of objects.

	This function is provided by some MicroPython ports for compatibility and is
	not efficient.

	Usage of `Poll` is recommended instead.
	'''
