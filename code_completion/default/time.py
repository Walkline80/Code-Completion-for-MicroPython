'''
time related functions

This module implements a subset of the corresponding `CPython` module, as described
below.

For more information, refer to the original `CPython` documentation: [time](https://docs.python.org/3.5/library/time.html#module-time).

The `time` module provides functions for getting the current time and date,
measuring time intervals, and for delays.

[View Doc](https://docs.micropython.org/en/latest/library/time.html)
'''
# Functions
def gmtime(secs: int = None) -> tuple:
	'''
	Convert the time `secs` expressed in seconds since the Epoch into an 8-tuple
	which contains:

		`(year, month, mday, hour, minute, second, weekday, yearday)`

	If `secs` is not provided or None, then the current time from the RTC is used.

	This function returns a date-time tuple in UTC.

	The format of the entries in the 8-tuple are:

	- year includes the century (for example 2014).
	- month is 1-12
	- mday is 1-31
	- hour is 0-23
	- minute is 0-59
	- second is 0-59
	- weekday is 0-6 for Mon-Sun
	- yearday is 1-366
	'''

def localtime(secs: int = None) -> tuple:
	'''
	Convert the time `secs` expressed in seconds since the Epoch into an 8-tuple
	which contains:

		`(year, month, mday, hour, minute, second, weekday, yearday)`

	If `secs` is not provided or None, then the current time from the RTC is used.

	This function returns a date-time tuple in local time.

	The format of the entries in the 8-tuple are:

	- `year` includes the century (for example 2014).
	- `month` is 1-12
	- `mday` is 1-31
	- `hour` is 0-23
	- `minute` is 0-59
	- `second` is 0-59
	- `weekday` is 0-6 for Mon-Sun
	- `yearday` is 1-366
	'''

def mktime(datetime: tuple) -> int:
	'''
	This is inverse function of localtime.

	It’s argument is a full 8-tuple which expresses a time as per localtime.

	It returns an integer which is the number of seconds since Jan 1, 2000.
	'''

def sleep(seconds: int | float):
	'''
	Sleep for the given number of `seconds`.

	Some boards may accept `seconds` as a floating-point number to sleep for a
	fractional number of `seconds`.

	Note that other boards may not accept a floating-point argument, for
	compatibility with them use `sleep_ms()` and `sleep_us()` functions.
	'''

def sleep_ms(ms: int):
	'''
	Delay for given number of milliseconds, should be positive or 0.

	This function will delay for at least the given number of milliseconds, but
	may take longer than that if other processing must take place, for example
	interrupt handlers or other threads.

	Passing in 0 for `ms` will still allow this other processing to occur.

	Use `sleep_us()` for more precise delays.
	'''

def sleep_us(us: int):
	'''
	Delay for given number of microseconds, should be positive or 0.

	This function attempts to provide an accurate delay of at least `us`
	microseconds, but it may take longer if the system has other higher priority
	processing to perform.
	'''

def ticks_ms():
	'''
	Returns an increasing millisecond counter with an arbitrary reference point,
	that wraps around after some value.

	The wrap-around value is not explicitly exposed, but we will refer to it as
	`TICKS_MAX` to simplify discussion.

	Period of the values is `TICKS_PERIOD = TICKS_MAX + 1`.

	`TICKS_PERIOD` is guaranteed to be a power of two, but otherwise may differ
	from port to port.

	The same period value is used for all of `ticks_ms()`, `ticks_us()`,
	`ticks_cpu()` functions (for simplicity).

	Thus, these functions will return a value in range `[0 .. TICKS_MAX]`,
	inclusive, total `TICKS_PERIOD` values.

	Note that only non-negative values are used. For the most part, you should
	treat values returned by these functions as opaque.

	The only operations available for them are `ticks_diff()` and `ticks_add()`
	functions described below.

	Note:

		Performing standard mathematical operations (+, -) or relational operators
		(<, <=, >, >=) directly on these value will lead to invalid result.

		Performing mathematical operations and then passing their results as
		arguments to `ticks_diff()` or `ticks_add()` will also lead to invalid
		results from the latter functions.
	'''

def ticks_us() -> int:
	'''Just like `ticks_ms()`, but in microseconds.'''

def ticks_cpu() -> int:
	'''
	Similar to `ticks_ms()` and `ticks_us()`, but with the highest possible
	resolution in the system.

	This is usually CPU clocks, and that’s why the function is named that way.

	But it doesn’t have to be a CPU clock, some other timing source available
	in a system (e.g. high-resolution timer) can be used instead.

	The exact timing unit (resolution) of this function is not specified on
	time module level, but documentation for a specific port may provide more
	specific information.

	This function is intended for very fine benchmarking or very tight real-time
	loops.

	Avoid using it in portable code.

	Availability: Not every port implements this function.
	'''

def ticks_add(ticks: int, delta: int) -> int:
	'''
	Offset `ticks` value by a given number, which can be either positive or
	negative.

	Given a `ticks` value, this function allows to calculate ticks value `delta`
	ticks before or after it, following modular-arithmetic definition of tick
	values.

	`ticks` parameter must be a direct result of call to `ticks_ms()`, `ticks_us()`
	, or `ticks_cpu()` functions (or from previous call to `ticks_add()`).

	However, `delta` can be an arbitrary integer number or numeric expression.

	`ticks_add()` is useful for calculating deadlines for events/tasks. (Note:
	you must use `ticks_diff()` function to work with deadlines.)
	'''

def ticks_diff(ticks1: int, ticks2: int) -> int:
	'''
	Measure ticks difference between values returned from `ticks_ms()`, `ticks_us()`
	, or `ticks_cpu()` functions, as a signed value which may wrap around.

	The argument order is the same as for subtraction operator, `ticks_diff(ticks1,
	ticks2)` has the same meaning as `ticks1 - ticks2`.
	'''

def time() -> int:
	'''
	Returns the number of seconds, as an integer, since the Epoch, assuming that
	underlying RTC is set and maintained as described above.

	If an RTC is not set, this function returns number of seconds since a
	port-specific reference point in time (for embedded boards without a
	battery-backed RTC, usually since power up or reset).

	If you want to develop portable MicroPython application, you should not rely
	on this function to provide higher than second precision.

	If you need higher precision, absolute timestamps, use `time_ns()`.

	If relative times are acceptable then use the `ticks_ms()` and `ticks_us()`
	functions.

	If you need calendar time, `gmtime()` or `localtime()` without an argument
	is a better choice.
	'''

def time_ns() -> int:
	'''
	Similar to `time()` but returns nanoseconds since the Epoch, as an integer
	(usually a big integer, so will allocate on the heap).
	'''
