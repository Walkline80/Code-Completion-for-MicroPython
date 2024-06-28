'''
functions related to the hardware

The machine module contains specific functions related to the hardware on a
particular board.

Most functions in this module allow to achieve direct and unrestricted access
to and control of hardware blocks on a system (like CPU, timers, buses, etc.).

Used incorrectly, this can lead to malfunction, lockups, crashes of your board,
and in extreme cases, hardware damage.

[View Doc](https://docs.micropython.org/en/latest/library/machine.html)
'''
import typing


# Constants
# IRQ wake values.
IDLE: int = ...
SLEEP: int = ...
DEEPSLEEP: int = ...

# Reset causes.
PWRON_RESET: int = ...
HARD_RESET: int = ...
WDT_RESET: int = ...
DEEPSLEEP_RESET: int = ...
SOFT_RESET: int = ...

# Wake-up reasons.
WLAN_WAKE: int = ...
PIN_WAKE: int = ...
RTC_WAKE: int = ...
EXT0_WAKE: int = ...
EXT1_WAKE: int = ...
TIMER_WAKE: int = ...
TOUCHPAD_WAKE: int = ...
ULP_WAKE: int = ...

# Memory access
def mem8():
	'''Read/write 8 bits of memory.'''

def mem16():
	'''Read/write 16 bits of memory.'''

def mem32():
	'''Read/write 32 bits of memory.'''

# Reset related functions
def reset():
	'''Resets the device in a manner similar to pushing the external RESET button.'''

def soft_reset():
	'''
	Performs a soft reset of the interpreter, deleting all Python objects and
	resetting the Python heap.

	It tries to retain the method by which the user is connected to the MicroPython
	REPL (eg serial, USB, Wifi).
	'''

def reset_cause():
	'''
	Get the reset cause.

	See `constants` for the possible return values.
	'''

def bootloader(value=None):
	'''
	Reset the device and enter its bootloader.

	This is typically used to put the device into a state where it can be
	programmed with new firmware.

	Some ports support passing in an optional value argument which can control
	which bootloader to enter, what to pass to it, or other things.
	'''

# Interrupt related functions
def disable_irq():
	'''
	Disable interrupt requests.

	Returns the previous IRQ state which should be considered an opaque value.

	This return value should be passed to the `enable_irq()` function to restore
	interrupts to their original state, before `disable_irq()` was called.
	'''

def enable_irq(state):
	'''
	Re-enable interrupt requests.

	The `state` parameter should be the value that was returned from the most
	recent call to the `disable_irq()` function.
	'''

# Power related functions
def freq(hz=None):
	'''
	Returns the CPU frequency in hertz.

	On some ports this can also be used to set the CPU frequency by passing in hz.
	'''

def idle():
	'''
	Gates the clock to the CPU, useful to reduce power consumption at any time
	during short or long periods.

	Peripherals continue working and execution resumes as soon as any interrupt
	is triggered.

	On many ports this includes system timer interrupt occurring at regular
	intervals on the order of millisecond.
	'''

def sleep():
	'''
	Note: This function is deprecated, use `lightsleep()` instead with no arguments.
	'''

def lightsleep(time_ms: int | None):
	'''
	Stops execution in an attempt to enter a low power state.

	If `time_ms` is specified then this will be the maximum time in milliseconds
	that the sleep will last for.

	Otherwise the sleep can last indefinitely.

	With or without a timeout, execution may resume at any time if there are events
	that require processing.

	Such events, or wake sources, should be configured before sleeping, like Pin
	change or RTC timeout.

	The precise behaviour and power-saving capabilities of lightsleep and deepsleep
	is highly dependent on the underlying hardware, but the general properties are:

	- A lightsleep has full RAM and state retention.

		Upon wake execution is resumed from the point where the sleep was requested,
		with all subsystems operational.
	'''

def deepsleep(time_ms: int | None):
	'''
	Stops execution in an attempt to enter a low power state.

	If `time_ms` is specified then this will be the maximum time in milliseconds
	that the sleep will last for.

	Otherwise the sleep can last indefinitely.

	With or without a timeout, execution may resume at any time if there are events
	that require processing.

	Such events, or wake sources, should be configured before sleeping, like Pin
	change or RTC timeout.

	The precise behaviour and power-saving capabilities of lightsleep and deepsleep
	is highly dependent on the underlying hardware, but the general properties are:

	- A deepsleep may not retain RAM or any other state of the system (for example
	peripherals or network interfaces).

		Upon wake execution is resumed from the main script, similar to a hard or
		power-on reset.

		The `reset_cause()` function will return `machine.DEEPSLEEP` and this can
		be used to distinguish a deepsleep wake from other resets.
	'''

def wake_reason():
	'''
	Get the wake reason.

	See constants for the possible return values.

	Availability: ESP32, WiPy.	
	'''

# Miscellaneous functions
def unique_id() -> bytes:
	'''
	Returns a byte string with a unique identifier of a board/SoC.

	It will vary from a board/SoC instance to another, if underlying hardware
	allows.

	Length varies by hardware (so use substring of a full value if you expect
	a short ID).

	In some MicroPython ports, ID corresponds to the network MAC address.
	'''

def time_pulse_us(pin, pulse_level: int, timeout_us: int = 1000000, /):
	'''
	Time a pulse on the given `pin`, and return the duration of the pulse in
	microseconds.

	The `pulse_level` argument should be 0 to time a low pulse or 1 to time a
	high pulse.

	If the current input value of the `pin` is different to `pulse_level`, the
	function first (*) waits until the `pin` input becomes equal to `pulse_level`,
	then (**) times the duration that the `pin` is equal to `pulse_level`.

	If the `pin` is already equal to `pulse_level` then timing starts straight away.

	The function will return -2 if there was timeout waiting for condition marked
	(*) above, and -1 if there was timeout during the main measurement, marked (**)
	above.

	The timeout is the same for both cases and given by `timeout_us` (which is
	in microseconds).
	'''

def bitstream(pin, encoding, timing, data, /):
	'''
	Transmits `data` by bit-banging the specified `pin`.

	The `encoding` argument specifies how the bits are encoded, and `timing` is
	an encoding-specific timing specification.
	'''

def rng() -> int:
	'''
	Return a 24-bit software generated random number.

	Availability: WiPy.
	'''


class Pin(object):
	'''
	control I/O pins

	A pin object is used to control I/O pins (also known as GPIO - general-purpose
	input/output).

	Pin objects are commonly associated with a physical pin that can drive an output
	voltage and read input voltages.

	The pin class has methods to set the mode of the pin (IN, OUT, etc) and methods
	to get and set the digital logic level.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.Pin.html)
	'''
	# Constants
	# Selects the pin mode.
	IN: int = ...
	OUT: int = ...
	OPEN_DRAIN: int = ...
	ALT: int = ...
	ALT_OPEN_DRAIN: int = ...
	ANALOG: int = ...

	# Selects whether there is a pull up/down resistor. Use the value None for no pull.
	PULL_UP: int = ...
	PULL_DOWN: int = ...
	PULL_HOLD: int = ...

	# Selects the pin drive strength.
	DRIVE_0: int = ...
	DRIVE_1: int = ...
	DRIVE_2: int = ...
	DRIVE_3: int = ...

	# Selects the IRQ trigger type.
	IRQ_FALLING: int = ...
	IRQ_RISING: int = ...
	IRQ_LOW_LEVEL: int = ...
	IRQ_HIGH_LEVEL: int = ...

	WAKE_LOW: int = ...
	WAKE_HIGH: int = ...

	def __init__(self, id, mode: int = -1, pull: int = -1, *, value=None,
		drive: int = 0, alt: int = -1):
		'''
		Access the pin peripheral (GPIO pin) associated with the given id.

		If additional arguments are given in the constructor then they are used
		to initialise the pin.

		Any settings that are not specified will remain in their previous state.
		'''

	# Methods
	def init(self, mode: int = -1, pull: int = -1, *, value=None, drive: int = 0,
		alt: int = -1):
		'''
		Re-initialise the pin using the given parameters.

		Only those arguments that are specified will be set.

		The rest of the pin peripheral state will remain unchanged.
		'''

	def value(self, x=None):
		'''
		This method allows to set and get the value of the pin, depending on
		whether the argument `x` is supplied or not.
		'''

	def __call__(self, x=None):
		'''
		Pin objects are callable.

		The call method provides a (fast) shortcut to set and get the value of
		the pin.

		It is equivalent to `Pin.value([x])`.
		'''

	def on(self):
		'''Set pin to "1" output level.'''

	def off(self):
		'''Set pin to "0" output level.'''

	def irq(self, handler=None, trigger: int = IRQ_FALLING | IRQ_RISING,
		*, priority: int = 1, wake=None, hard: bool = False):
		'''
		Configure an interrupt `handler` to be called when the trigger source of
		the pin is active.

		If the pin mode is `Pin.IN` then the trigger source is the external value
		on the pin.

		If the pin mode is `Pin.OUT` then the trigger source is the output buffer
		of the pin.

		Otherwise, if the pin mode is `Pin.OPEN_DRAIN` then the trigger source is
		the output buffer for state '0' and the external pin value for state '1'.
		'''

	def low(self):
		'''
		Set pin to "0" output level.

		Availability: nrf, rp2, stm32 ports.
		'''

	def high(self):
		'''
		Set pin to "1" output level.

		Availability: nrf, rp2, stm32 ports.
		'''

	@typing.overload
	def mode(self):
		'''
		Get the pin mode.

		Availability: cc3200, stm32 ports.
		'''

	@typing.overload
	def mode(self, mode):
		'''
		Set the pin mode.

		Availability: cc3200, stm32 ports.
		'''

	@typing.overload
	def pull(self):
		'''
		Get the pin pull state.

		Availability: cc3200, stm32 ports.
		'''

	@typing.overload
	def pull(self, pull):
		'''
		Set the pin pull state.

		Availability: cc3200, stm32 ports.
		'''

	@typing.overload
	def drive(self):
		'''
		Get the pin drive strength.

		Availability: cc3200 port.
		'''

	@typing.overload
	def drive(self, drive):
		'''
		Set the pin drive strength.

		Availability: cc3200 port.
		'''


class Signal(object):
	'''
	control and sense external I/O devices

	The Signal class is a simple extension of the Pin class.

	Unlike Pin, which can be only in "absolute" 0 and 1 states, a Signal can be
	in "asserted" (on) or "deasserted" (off) states, while being inverted
	(active-low) or not.

	In other words, it adds logical inversion support to Pin functionality.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.Signal.html)
	'''
	def __init__(self, obj_or_pin_arguments, *, invert: bool = False):
		'''
		Create a Signal object. There’re two ways to create it:

		- By wrapping existing Pin object - universal method which works for any
		board.

		- By passing required Pin parameters directly to Signal constructor,
		skipping the need to create intermediate Pin object. Available on many,
		but not all boards.

		The arguments are:

		- `pin_obj` is existing Pin object.

		- `pin_arguments` are the same arguments as can be passed to Pin constructor.

		- `invert` - if True, the signal will be inverted (active low).
		'''

	# Methods
	def value(self, x=None):
		'''
		This method allows to set and get the value of the signal, depending on
		whether the argument `x` is supplied or not.
		'''

	def on(self):
		'''Activate signal.'''

	def off(self):
		'''Deactivate signal.'''


class ADC(object):
	'''
	analog to digital conversion

	The ADC class provides an interface to analog-to-digital converters, and
	represents a single endpoint that can sample a continuous voltage and convert
	it to a discretised value.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.ADC.html)
	'''
	def __init__(self, id, *, sample_ns, atten):
		'''
		Access the ADC associated with a source identified by `id`.

		This `id` may be an integer (usually specifying a channel number), a Pin
		object, or other value supported by the underlying machine.

		If additional keyword-arguments are given then they will configure various
		aspects of the ADC.

		If not given, these settings will take previous or default values.

		The settings are:

		- `sample_ns` is the sampling time in nanoseconds.

		- `atten` specifies the input attenuation.
		'''

	# Methods
	def init(self, *, sample_ns, atten):
		'''
		Apply the given settings to the ADC.

		Only those arguments that are specified will be changed.
		'''

	def block(self):
		'''
		Return the ADCBlock instance associated with this ADC object.

		This method only exists if the port supports the ADCBlock class.
		'''

	def read_u16(self) -> int:
		'''
		Take an analog reading and return an integer in the range 0-65535.

		The return value represents the raw reading taken by the ADC, scaled such
		that the minimum value is 0 and the maximum value is 65535.
		'''

	def read_uv(self) -> int:
		'''
		Take an analog reading and return an integer value with units of microvolts.

		It is up to the particular port whether or not this value is calibrated,
		and how calibration is done.
		'''


class ADCBlock(object):
	'''
	control ADC peripherals

	The ADCBlock class provides access to an ADC peripheral which has a number of
	channels that can be used to sample analog values.

	It allows finer control over configuration of `machine.ADC` objects, which do
	the actual sampling.

	This class is not always available.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.ADCBlock.html)
	'''
	def __init(self, id, *, bits):
		'''
		Access the ADC peripheral identified by `id`, which may be an integer
		or string.

		The `bits` argument, if given, sets the resolution in bits of the
		conversion process.

		If not specified then the previous or default resolution is used.
		'''

	# Methods
	def init(self, *, bits):
		'''
		Configure the ADC peripheral.

		`bits` will set the resolution of the conversion process.
		'''

	def connect(self, channel: int = None, source=None, *, args):
		'''
		Connect up a channel on the ADC peripheral so it is ready for sampling,
		and return an ADC object that represents that connection.

		The `channel` argument must be an integer, and `source` must be an object
		(for example a Pin) which can be connected up for sampling.

		If only `channel` is given then it is configured for sampling.

		If only `source` is given then that object is connected to a default
		channel ready for sampling.

		If both `channel` and `source` are given then they are connected together
		and made ready for sampling.

		Any additional keyword arguments are used to configure the returned ADC
		object, via its init method.
		'''


class PWM(object):
	'''
	pulse width modulation

	This class provides pulse width modulation output.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.PWM.html)
	'''
	def __init__(self, dest, *, freq: int, duty_u16: int, duty_ns: int, invert: bool):
		'''
		Construct and return a new PWM object using the following parameters:

		- `dest` is the entity on which the PWM is output, which is usually a
		`machine.Pin` object, but a port may allow other values, like integers.

		- `freq` should be an integer which sets the frequency in Hz for the
		PWM cycle.

		- `duty_u16` sets the duty cycle as a ratio duty_u16 / 65535.

		- `duty_ns` sets the pulse width in nanoseconds.

		- `invert` inverts the respective output if the value is True

		Setting `freq` may affect other PWM objects if the objects share the same
		underlying PWM generator (this is hardware specific).

		Only one of `duty_u16` and `duty_ns` should be specified at a time.

		`invert` is not available at all ports.
		'''

	# Methods
	def init(self, *, freq: int, duty_u16: int, duty_ns: int):
		'''Modify settings for the PWM object.'''

	def deinit(self):
		'''Disable the PWM output.'''

	@typing.overload
	def freq(self) -> int:
		'''
		Get the current frequency of the PWM output.

		The frequency in Hz is returned.
		'''

	@typing.overload
	def freq(self, value: int):
		'''
		Set the current frequency of the PWM output.

		With a single `value` argument the frequency is set to that value in Hz.

		The method may raise a `ValueError` if the frequency is outside the valid
		range.
		'''

	@typing.overload
	def duty_u16(self) -> int:
		'''
		Get the current duty cycle of the PWM output, as an unsigned 16-bit value
		in the range 0 to 65535 inclusive.

		he duty cycle is returned.
		'''

	@typing.overload
	def duty_u16(self, value: int):
		'''
		Set the current duty cycle of the PWM output, as an unsigned 16-bit value
		in the range 0 to 65535 inclusive.

		With a single `value` argument the duty cycle is set to that value, measured
		as the ratio value / 65535.
		'''

	@typing.overload
	def duty_ns(self) -> int:
		'''
		Get the current pulse width of the PWM output, as a value in nanoseconds.

		The pulse width in nanoseconds is returned.
		'''

	@typing.overload
	def duty_ns(self, value: int):
		'''
		Set the current pulse width of the PWM output, as a value in nanoseconds.

		With a single `value` argument the pulse width is set to that value.
		'''


class UART(object):
	'''
	duplex serial communication bus

	UART implements the standard `UART/USART` duplex serial communications protocol.

	At the physical level it consists of 2 lines: `RX` and `TX`.

	The unit of communication is a character (not to be confused with a string
	character) which can be 8 or 9 bits wide.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.UART.html)
	'''
	# Constants
	INV_TX: int = ...
	INV_RX: int = ...
	INV_RTS: int = ...
	INV_CTS: int = ...
	RTS: int = ...
	CTS: int = ...

	RX_ANY: int = ...
	'''IRQ trigger sources. Availability: WiPy.'''

	def __init__(self, id):
		'''Construct a UART object of the given id.'''

	# Methods
	def init(self, baudrate: int = 9600, bits: int = 8, parity: int = None,
		stop: int = 1, *, args):
		'''
		Initialise the UART bus with the given parameters:

		- `baudrate` is the clock rate.
		- `bits` is the number of bits per character, 7, 8 or 9.
		- `parity` is the parity, None, 0 (even) or 1 (odd).
		- `stop` is the number of stop bits, 1 or 2.

		Additional keyword-only parameters that may be supported by a port are:

		- `tx` specifies the TX pin to use.
		- `rx` specifies the RX pin to use.
		- `rts` specifies the RTS (output) pin to use for hardware receive flow control.
		- `cts` specifies the CTS (input) pin to use for hardware transmit flow control.
		- `txbuf` specifies the length in characters of the TX buffer.
		- `rxbuf` specifies the length in characters of the RX buffer.
		- `timeout` specifies the time to wait for the first character (in ms).
		- `timeout_char` specifies the time to wait between characters (in ms).
		- `invert` specifies which lines to invert.

			- 0 will not invert lines (idle state of both lines is logic high).
			- `UART.INV_TX` will invert TX line (idle state of TX line now logic low).
			- `UART.INV_RX` will invert RX line (idle state of RX line now logic low).
			- `UART.INV_TX | UART.INV_RX` will invert both lines (idle state at logic low).

		- `flow` specifies which hardware flow control signals to use. The value is a bitmask.

			- 0 will ignore hardware flow control signals.
			- `UART.RTS` will enable receive flow control by using the RTS output pin to signal if the receive FIFO has sufficient space to accept more data.
			- `UART.CTS` will enable transmit flow control by pausing transmission when the CTS input pin signals that the receiver is running low on buffer space.
			- `UART.RTS | UART.CTS` will enable both, for full hardware flow control.
		'''

	def deinit(self):
		'''Turn off the UART bus.'''

	def any(self) -> int:
		'''
		Returns an integer counting the number of characters that can be read
		without blocking.

		It will return 0 if there are no characters available and a positive
		number if there are characters.

		The method may return 1 even if there is more than one character available
		for reading.
		'''

	@typing.overload
	def read(self) -> bytes | None:
		'''
		Read characters.

		It may return sooner if a timeout is reached.

		The timeout is configurable in the constructor.

		Return value: a bytes object containing the bytes read in.

		Returns None on timeout.
		'''

	@typing.overload
	def read(self, nbytes: int) -> bytes | None:
		'''
		Read characters.

		Read `nbytes` at most that many bytes, otherwise read as much data as
		possible.

		It may return sooner if a timeout is reached.

		The timeout is configurable in the constructor.

		Return value: a bytes object containing the bytes read in.

		Returns None on timeout.
		'''

	@typing.overload
	def readinto(self, buf) -> int | None:
		'''
		Read bytes into the `buf`.

		Read at most `len(buf)` bytes.

		It may return sooner if a timeout is reached.

		The timeout is configurable in the constructor.

		Return value: number of bytes read and stored into buf or None on timeout.
		'''

	@typing.overload
	def readinto(self, buf, nbytes: int) -> int | None:
		'''
		Read bytes into the `buf`.

		Read `nbytes` at most that many bytes.

		It may return sooner if a timeout is reached.

		The timeout is configurable in the constructor.

		Return value: number of bytes read and stored into buf or None on timeout.
		'''

	def readline(self):
		'''
		Read a line, ending in a newline character.

		It may return sooner if a timeout is reached.

		The timeout is configurable in the constructor.

		Return value: the line read or None on timeout.
		'''

	def write(self, buf) -> int | None:
		'''
		Write the buffer of bytes to the bus.

		Return value: number of bytes written or None on timeout.
		'''

	def sendbreak(self):
		'''
		Send a break condition on the bus.

		This drives the bus low for a duration longer than required for a normal
		transmission of a character.
		'''

	def irq(self, trigger, priority=1, handler=None, wake=IDLE):
		'''
		Create a callback to be triggered when data is received on the UART.

		- `trigger` can only be `UART.RX_ANY`

		- `priority` level of the interrupt.

			Can take values in the range 1-7.

			Higher values represent higher priorities.

		- `handler` an optional function to be called when new characters arrive.

		- `wake` can only be `machine.IDLE`.

		Returns an irq object.

		Availability: WiPy.
		'''

	def flush(self):
		'''
		Waits until all data has been sent.

		In case of a timeout, an exception is raised.

		The timeout duration depends on the tx buffer size and the baud rate.

		Unless flow control is enabled, a timeout should not occur.

		Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, renesas-ra
		'''

	def txdone(self) -> bool:
		'''
		Tells whether all data has been sent or no data transfer is happening.

		In this case, it returns True. If a data transmission is ongoing it
		returns False.

		Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, renesas-ra
		'''


class SPI(object):
	'''
	a Serial Peripheral Interface bus protocol (controller side)

	[View Doc](https://docs.micropython.org/en/latest/library/machine.SPI.html)
	'''
	# Constants
	CONTROLLER = ...
	'''
	for initialising the SPI bus to controller

	this is only used for the WiPy
	'''

	MSB: int = ...
	'''set the first bit to be the most significant bit'''

	LSB: int = ...
	'''set the first bit to be the least significant bit'''

	def __init__(self, id):
		'''
		Construct an SPI object on the given bus, `id`. Values of `id` depend on
		a particular port and its hardware.

		Values 0, 1, etc. are commonly used to select hardware SPI block #0, #1,
		etc.

		With no additional parameters, the SPI object is created but not initialised
		(it has the settings from the last initialisation of the bus, if any).

		If extra arguments are given, the bus is initialised.
		'''

	# Methods
	def init(self, baudrate: int = 1000000, *, polarity: int = 0, phase: int = 0,
		bits: int = 8, firstbit: int = MSB, sck=None, mosi=None, miso=None, pins=None):
		'''
		Initialise the SPI bus with the given parameters:

		- `baudrate` is the SCK clock rate.
		- `polarity` can be 0 or 1, and is the level the idle clock line sits at.
		- `phase` can be 0 or 1 to sample data on the first or second clock edge
		respectively.
		- `bits` is the width in bits of each transfer. Only 8 is guaranteed to
		be supported by all hardware.
		- `firstbit` can be SPI.MSB or SPI.LSB.
		- `sck`, `mosi`, `miso` are pins (machine.Pin) objects to use for bus
		signals.

			For most hardware SPI blocks (as selected by id parameter to the
			constructor), pins are fixed and cannot be changed.

			In some cases, hardware blocks allow 2-3 alternative pin sets for a
			hardware SPI block.

			Arbitrary pin assignments are possible only for a bitbanging SPI
			driver (id = -1).

		- `pins` - WiPy port doesn’t use sck, mosi, miso arguments, and instead
		allows to specify them as a tuple of pins parameter.

		In the case of hardware SPI the actual clock frequency may be lower than
		the requested baudrate.

		This is dependent on the platform hardware.

		The actual rate may be determined by printing the SPI object.
		'''

	def deinit(self):
		'''Turn off the SPI bus.'''

	def read(self, nbytes: int, write=0x00) -> bytes:
		'''
		Read a number of bytes specified by `nbytes` while continuously writing
		the single byte given by `write`.

		Returns a bytes object with the data that was read.
		'''

	def readinto(self, buf, write=0x00) -> None:
		'''
		Read into the buffer specified by `buf` while continuously writing the
		single byte given by `write`.

		Returns None.

		Note: on WiPy this function returns the number of bytes read.
		'''

	def write(self, buf):
		'''
		Write the bytes contained in `buf`.

		Returns None.

		Note: on WiPy this function returns the number of bytes written.
		'''

	def write_readinto(self, write_buf, read_buf) -> None:
		'''
		Write the bytes from `write_buf` while reading into `read_buf`.

		The buffers can be the same or different, but both buffers must have the
		same length.

		Returns None.

		Note: on WiPy this function returns the number of bytes written.
		'''


class SoftSPI(object):
	'''
	a Serial Peripheral Interface bus protocol (controller side)

	[View Doc](https://docs.micropython.org/en/latest/library/machine.SPI.html)
	'''
	# Constants
	CONTROLLER = ...
	'''
	for initialising the SPI bus to controller

	this is only used for the WiPy
	'''

	MSB: int = ...
	'''set the first bit to be the most significant bit'''

	LSB: int = ...
	'''set the first bit to be the least significant bit'''

	def __init__(self, baudrate: int = 500000, *, polarity: int = 0, phase: int = 0,
		bits: int = 8, firstbit: int = MSB, sck=None, mosi=None, miso=None):
		'''
		Construct a new software SPI object.

		Additional parameters must be given, usually at least `sck`, `mosi` and
		`miso`, and these are used to initialise the bus.
		'''

	# Methods
	def init(self, baudrate: int = 1000000, *, polarity: int = 0, phase: int = 0,
		bits: int = 8, firstbit: int = MSB, sck=None, mosi=None, miso=None, pins=None):
		'''
		Initialise the SPI bus with the given parameters:

		- `baudrate` is the SCK clock rate.
		- `polarity` can be 0 or 1, and is the level the idle clock line sits at.
		- `phase` can be 0 or 1 to sample data on the first or second clock edge
		respectively.
		- `bits` is the width in bits of each transfer. Only 8 is guaranteed to
		be supported by all hardware.
		- `firstbit` can be SPI.MSB or SPI.LSB.
		- `sck`, `mosi`, `miso` are pins (machine.Pin) objects to use for bus
		signals.

			For most hardware SPI blocks (as selected by id parameter to the
			constructor), pins are fixed and cannot be changed.

			In some cases, hardware blocks allow 2-3 alternative pin sets for a
			hardware SPI block.

			Arbitrary pin assignments are possible only for a bitbanging SPI
			driver (id = -1).

		- `pins` - WiPy port doesn’t use sck, mosi, miso arguments, and instead
		allows to specify them as a tuple of pins parameter.

		In the case of hardware SPI the actual clock frequency may be lower than
		the requested baudrate.

		This is dependent on the platform hardware.

		The actual rate may be determined by printing the SPI object.
		'''

	def deinit(self):
		'''Turn off the SPI bus.'''

	def read(self, nbytes: int, write=0x00) -> bytes:
		'''
		Read a number of bytes specified by `nbytes` while continuously writing
		the single byte given by `write`.

		Returns a bytes object with the data that was read.
		'''

	def readinto(self, buf, write=0x00) -> None:
		'''
		Read into the buffer specified by `buf` while continuously writing the
		single byte given by `write`.

		Returns None.

		Note: on WiPy this function returns the number of bytes read.
		'''

	def write(self, buf) -> None:
		'''
		Write the bytes contained in `buf`.

		Returns None.

		Note: on WiPy this function returns the number of bytes written.
		'''

	def write_readinto(self, write_buf, read_buf) -> None:
		'''
		Write the bytes from `write_buf` while reading into `read_buf`.

		The buffers can be the same or different, but both buffers must have the
		same length.

		Returns None.

		Note: on WiPy this function returns the number of bytes written.
		'''


class I2C(object):
	'''
	a two-wire serial protocol

	I2C is a two-wire protocol for communicating between devices.

	At the physical level it consists of 2 wires: SCL and SDA, the clock and data
	lines respectively.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.I2C.html)
	'''
	def __init__(self, id, *, scl, sda, freq: int = 400000, timeout: int = 50000):
		'''
		Construct and return a new I2C object using the following parameters:

		- `id` identifies a particular I2C peripheral. Allowed values for depend
		on the particular port/board
		- `scl` should be a pin object specifying the pin to use for SCL.
		- `sda` should be a pin object specifying the pin to use for SDA.
		- `freq` should be an integer which sets the maximum frequency for SCL.
		- `timeout` is the maximum time in microseconds to allow for I2C transactions.

			This parameter is not allowed on some ports.
		'''

	# General Methods
	def init(self, scl, sda, *, freq: int = 400000):
		'''
		Initialise the I2C bus with the given arguments:

		- `scl` is a pin object for the SCL line
		- `sda` is a pin object for the SDA line
		- `freq` is the SCL clock rate

		In the case of hardware I2C the actual clock frequency may be lower than
		the requested frequency.

		This is dependent on the platform hardware.

		The actual rate may be determined by printing the I2C object.
		'''

	def deinit(self):
		'''
		Turn off the I2C bus.

		Availability: WiPy.
		'''

	def scan(self):
		'''
		Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list
		of those that respond.

		A device responds if it pulls the SDA line low after its address (including
		a write bit) is sent on the bus.
		'''

	# Standard bus operations
	def readfrom(self, addr, nbytes: int, stop: bool = True, /) -> bytes:
		'''
		Read `nbytes` from the peripheral specified by `addr`.

		If `stop` is true then a STOP condition is generated at the end of the
		transfer.

		Returns a bytes object with the data read.
		'''

	def readfrom_into(self, addr, buf, stop: bool = True, /) -> None:
		'''
		Read into `buf` from the peripheral specified by `addr`.

		The number of bytes read will be the length of `buf`.

		If `stop` is true then a STOP condition is generated at the end of the
		transfer.

		The method returns None.
		'''

	def writeto(self, addr, buf, stop: bool = True, /) -> int:
		'''
		Write the bytes from `buf` to the peripheral specified by `addr`.

		If a NACK is received following the write of a byte from `buf` then the
		remaining bytes are not sent.

		If `stop` is true then a STOP condition is generated at the end of the
		transfer, even if a NACK is received.

		The function returns the number of ACKs that were received.
		'''

	def writevto(self, addr, vector, stop: bool = True, /) -> None:
		'''
		Write the bytes contained in `vector` to the peripheral specified by `addr`.

		`vector` should be a tuple or list of objects with the buffer protocol.

		The `addr` is sent once and then the bytes from each object in vector are
		written out sequentially.

		The objects in `vector` may be zero bytes in length in which case they don’t
		contribute to the output.

		If a NACK is received following the write of a byte from one of the objects
		in vector then the remaining bytes, and any remaining objects, are not sent.

		If `stop` is true then a STOP condition is generated at the end of the
		transfer, even if a NACK is received.

		The function returns the number of ACKs that were received.
		'''

	# Memory operations
	def readfrom_mem(self, addr, memaddr, nbytes: int, *, addrsize: int = 8) -> bytes:
		'''
		Read `nbytes` from the peripheral specified by `addr` starting from the
		memory address specified by `memaddr`.

		The argument `addrsize` specifies the address size in bits.

		Returns a bytes object with the data read.
		'''

	def readfrom_mem_into(self, addr, memaddr, buf, *, addrsize=8) -> None:
		'''
		Read into `buf` from the peripheral specified by `addr` starting from the
		memory address specified by `memaddr`.

		The number of bytes read is the length of `buf`.

		The argument `addrsize` specifies the address size in bits (on ESP8266
		this argument is not recognised and the address size is always 8 bits).

		The method returns None.
		'''

	def writeto_mem(self, addr, memaddr, buf, *, addrsize: int = 8) -> None:
		'''
		Write `buf` to the peripheral specified by `addr` starting from the memory
		address specified by `memaddr`.

		The argument `addrsize` specifies the address size in bits (on ESP8266 this
		argument is not recognised and the address size is always 8 bits).

		The method returns None.
		'''


class SoftI2C(object):
	'''
	a two-wire serial protocol

	I2C is a two-wire protocol for communicating between devices.

	At the physical level it consists of 2 wires: SCL and SDA, the clock and data
	lines respectively.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.I2C.html)
	'''
	def __init__(self, scl, sda, *, freq: int = 400000, timeout: int = 50000):
		'''
		Construct a new software I2C object. The parameters are:

		- `scl` should be a pin object specifying the pin to use for SCL.
		- `sda` should be a pin object specifying the pin to use for SDA.
		- `freq` should be an integer which sets the maximum frequency for SCL.
		- `timeout` is the maximum time in microseconds to wait for clock stretching
		(SCL held low by another device on the bus), after which an OSError(ETIMEDOUT) exception is raised.
		'''

	# General Methods
	def init(self, scl, sda, *, freq=400000):
		'''
		Initialise the I2C bus with the given arguments:

		- `scl` is a pin object for the SCL line
		- `sda` is a pin object for the SDA line
		- `freq` is the SCL clock rate

		In the case of hardware I2C the actual clock frequency may be lower than
		the requested frequency.

		This is dependent on the platform hardware.

		The actual rate may be determined by printing the I2C object.
		'''

	def deinit(self):
		'''
		Turn off the I2C bus.

		Availability: WiPy.
		'''

	def scan(self):
		'''
		Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list
		of those that respond.

		A device responds if it pulls the SDA line low after its address (including
		a write bit) is sent on the bus.
		'''

	# Primitive I2C operations.
	# These methods are only available on the `machine.SoftI2C` class.
	def start(self):
		'''Generate a START condition on the bus (SDA transitions to low while SCL is high).'''

	def stop(self):
		'''Generate a STOP condition on the bus (SDA transitions to high while SCL is high).'''

	def readinto(self, buf, nack: bool = True, /):
		'''
		Reads bytes from the bus and stores them into `buf`.

		The number of bytes read is the length of `buf`.

		An ACK will be sent on the bus after receiving all but the last byte.

		After the last byte is received, if `nack` is true then a NACK will be sent,
		otherwise an ACK will be sent (and in this case the peripheral assumes more
		bytes are going to be read in a later call).
		'''

	def write(self, buf) -> int:
		'''
		Write the bytes from `buf` to the bus.

		Checks that an ACK is received after each byte and stops transmitting the
		remaining bytes if a NACK is received.

		The function returns the number of ACKs that were received.
		'''

	# Standard bus operations
	def readfrom(self, addr, nbytes: int, stop: bool = True, /) -> bytes:
		'''
		Read `nbytes` from the peripheral specified by `addr`.

		If `stop` is true then a STOP condition is generated at the end of the
		transfer.

		Returns a bytes object with the data read.
		'''

	def readfrom_into(self, addr, buf, stop: bool = True, /) -> None:
		'''
		Read into `buf` from the peripheral specified by `addr`.

		The number of bytes read will be the length of `buf`.

		If `stop` is true then a STOP condition is generated at the end of the
		transfer.

		The method returns None.
		'''

	def writeto(self, addr, buf, stop: bool = True, /) -> int:
		'''
		Write the bytes from `buf` to the peripheral specified by `addr`.

		If a NACK is received following the write of a byte from `buf` then the
		remaining bytes are not sent.

		If `stop` is true then a STOP condition is generated at the end of the
		transfer, even if a NACK is received.

		The function returns the number of ACKs that were received.
		'''

	def writevto(self, addr, vector, stop: bool = True, /) -> int:
		'''
		Write the bytes contained in `vector` to the peripheral specified by `addr`.

		`vector` should be a tuple or list of objects with the buffer protocol.

		The `addr` is sent once and then the bytes from each object in vector are
		written out sequentially.

		The objects in `vector` may be zero bytes in length in which case they
		don’t contribute to the output.

		If a NACK is received following the write of a byte from one of the objects
		in vector then the remaining bytes, and any remaining objects, are not sent.

		If `stop` is true then a STOP condition is generated at the end of the
		transfer, even if a NACK is received.

		The function returns the number of ACKs that were received.
		'''

	# Memory operations
	def readfrom_mem(self, addr, memaddr, nbytes: int, *, addrsize: int = 8) -> bytes:
		'''
		Read `nbytes` from the peripheral specified by `addr` starting from the
		memory address specified by `memaddr`.

		The argument `addrsize` specifies the address size in bits.

		Returns a bytes object with the data read.
		'''

	def readfrom_mem_into(self, addr, memaddr, buf, *, addrsize=8) -> None:
		'''
		Read into `buf` from the peripheral specified by `addr` starting from the
		memory address specified by `memaddr`.

		The number of bytes read is the length of `buf`.

		The argument `addrsize` specifies the address size in bits (on ESP8266 this
		argument is not recognised and the address size is always 8 bits).

		The method returns None.
		'''

	def writeto_mem(self, addr, memaddr, buf, *, addrsize: int = 8) -> None:
		'''
		Write `buf` to the peripheral specified by `addr` starting from the memory
		address specified by `memaddr`.

		The argument `addrsize` specifies the address size in bits (on ESP8266
		this argument is not recognised and the address size is always 8 bits).

		The method returns None.
		'''


class I2S(object):
	'''
	Inter-IC Sound bus protocol

	I2S is a synchronous serial protocol used to connect digital audio devices.

	At the physical level, a bus consists of 3 lines: SCK, WS, SD.

	The I2S class supports controller operation. Peripheral operation is not supported.

	The I2S class is currently available as a Technical Preview.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.I2S.html)
	'''
	# Constants
	RX: int = ...
	'''for initialising the I2S bus mode to receive'''

	TX: int = ...
	'''for initialising the I2S bus mode to transmit'''

	STEREO: int = ...
	'''for initialising the I2S bus format to stereo'''

	MONO: int = ...
	'''for initialising the I2S bus format to mono'''

	def __init__(self, id, *, sck, ws, sd, mck=None, mode, bits, format, rate, ibuf):
		'''
		Construct an I2S object of the given id:

		- `id` identifies a particular I2S bus; it is board and port specific

		Keyword-only parameters that are supported on all ports:

		- `sck` is a pin object for the serial clock line
		- `ws` is a pin object for the word select line
		- `sd` is a pin object for the serial data line
		- `mck` is a pin object for the master clock line; master clock frequency
		is sampling rate * 256
		- `mode` specifies receive or transmit
		- `bits` specifies sample size (bits), 16 or 32
		- `format` specifies channel format, STEREO or MONO
		- `rate` specifies audio sampling rate (Hz); this is the frequency of
		the ws signal
		- `ibuf` specifies internal buffer length (bytes)
		'''

	# Methods
	def init(self, sck, *, args):
		'''see Constructor for argument descriptions'''

	def deinit(self):
		'''Deinitialize the I2S bus'''

	def readinto(self, buf) -> int:
		'''
		Read audio samples into the buffer specified by `buf`.

		`buf` must support the buffer protocol, such as bytearray or array.

		`buf` byte ordering is little-endian.

		For Stereo format, left channel sample precedes right channel sample.

		For Mono format, the left channel sample data is used.

		Returns number of bytes read
		'''

	def write(self, buf) -> int:
		'''
		Write audio samples contained in `buf`.

		`buf` must support the buffer protocol, such as bytearray or array.

		`buf` byte ordering is little-endian.

		For Stereo format, left channel sample precedes right channel sample.

		For Mono format, the sample data is written to both the right and left
		channels.

		Returns number of bytes written
		'''

	def irq(self, handler):
		'''
		Set a callback. `handler` is called when buf is emptied (write method)
		or becomes full (readinto method).

		Setting a callback changes the write and readinto methods to non-blocking
		operation.

		`handler` is called in the context of the MicroPython scheduler.
		'''

	@staticmethod
	def shift(*, buf, bits, shift):
		'''
		bitwise shift of all samples contained in `buf`.

		`bits` specifies sample size in bits.

		`shift` specifies the number of bits to shift each sample.

		Positive for left shift, negative for right shift.

		Typically used for volume control.

		Each bit shift changes sample volume by `6dB`.
		'''


class RTC(object):
	'''
	real time clock

	The RTC is an independent clock that keeps track of the date and time.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.RTC.html)
	'''
	# Constants
	ALARM0: int = ...
	'''irq trigger source'''

	def __init__(self, id: int = 0):
		'''Create an RTC object.'''

	@typing.overload
	def datetime(self):
		'''
		Get the date and time of the RTC.

		This method returns an 8-tuple with the current date and time.

		The 8-tuple has the following format:

		`(year, month, day, weekday, hours, minutes, seconds, subseconds)`
		'''

	# Methods
	@typing.overload
	def datetime(self, datetimetuple: tuple):
		'''
		Set the date and time of the RTC.

		With argument (being an 8-tuple) it sets the date and time.

		The 8-tuple has the following format:

		`(year, month, day, weekday, hours, minutes, seconds, subseconds)`
		'''

	def init(self, datetime: tuple):
		'''
		Initialise the RTC.

		`datetime` is a tuple of the form:

		`(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])`
		'''

	def now(self):
		'''Get get the current datetime tuple.'''

	def deinit(self):
		'''Resets the RTC to the time of January 1, 2015 and starts running it again.'''

	def alarm(self, id, time, *, repeat: bool = False):
		'''
		Set the RTC alarm.

		`time` might be either a millisecond value to program the alarm to current
		`time + time_in_ms` in the future, or a datetimetuple.

		If the `time` passed is in milliseconds, `repeat` can be set to True to
		make the alarm periodic.
		'''

	def alarm_left(self, alarm_id: int = 0):
		'''Get the number of milliseconds left before the alarm expires.'''

	def cancel(self, alarm_id: int = 0):
		'''Cancel a running alarm.'''

	def irq(self, *, trigger: int, handler=None, wake: int = IDLE):
		'''
		Create an irq object triggered by a real time clock alarm.

		- `trigger` must be `RTC.ALARM0`
		- `handler` is the function to be called when the callback is triggered.
		- `wake` specifies the sleep mode from where this interrupt can wake up
		the system.
		'''

	@typing.overload
	def memory(self) -> bytes:
		'''
		Reads RTC memory and returns a bytes object.

		The maximum length of RTC user memory is 2048 bytes by default on esp32,
		and 492 bytes on esp8266.

		Availability: esp32, esp8266 ports.
		'''

	@typing.overload
	def memory(self, data):
		'''
		Write data to the RTC memory, where data is any object which supports the
		buffer protocol (including `bytes`, `bytearray`, `memoryview` and
		`array.array`).

		Data written to RTC user memory is persistent across restarts, including
		`machine.soft_reset()` and `machine.deepsleep()`.

		The maximum length of RTC user memory is 2048 bytes by default on esp32,
		and 492 bytes on esp8266.

		Availability: esp32, esp8266 ports.
		'''


class Timer(object):
	'''
	control hardware timers

	Hardware timers deal with timing of periods and events.

	Timers are perhaps the most flexible and heterogeneous kind of hardware in
	MCUs and SoCs, differently greatly from a model to a model.

	MicroPython’s Timer class defines a baseline operation of executing a callback
	with a given period (or once after some delay), and allow specific boards
	to define more non-standard behaviour (which thus won’t be portable to other
	boards).

	[View Doc](https://docs.micropython.org/en/latest/library/machine.Timer.html)
	'''
	# Constants
	# Timer operating mode.
	ONE_SHOT: int = ...
	PERIODIC: int = ...

	def __init__(self, id: int):
		'''
		Construct a new timer object of the given `id`.

		`id` of -1 constructs a virtual timer (if supported by a board).

		`id` shall not be passed as a keyword argument.

		See `init` for parameters of initialisation.
		'''

	# Methods
	def init(self, *, mode: int = PERIODIC, freq: int = -1, period: int = -1,
		callback: function=None):
		'''
		Initialise the timer.

		Keyword arguments:

		- `mode` can be one of:

			- `Timer.ONE_SHOT` - The timer runs once until the configured `period` of the channel expires.
			- `Timer.PERIODIC` - The timer runs periodically at the configured frequency of the channel.

		- `freq` - The timer frequency, in units of Hz.

			The upper bound of the frequency is dependent on the port.

			When both the `freq` and `period` arguments are given, `freq` has a
			higher priority and `period` is ignored.

		- `period` - The timer period, in milliseconds.
		- `callback` - The callable to call upon expiration of the timer period.

			The `callback` must take one argument, which is passed the Timer object.

			The `callback` argument shall be specified.

			Otherwise an exception will occur upon timer expiration: `TypeError:
			'NoneType' object isn't callable`
		'''

	def deinit(self):
		'''
		Deinitialises the timer.

		Stops the timer, and disables the timer peripheral.
		'''


class WDT(object):
	'''
	watchdog timer

	The WDT is used to restart the system when the application crashes and ends
	up into a non recoverable state.

	Once started it cannot be stopped or reconfigured in any way.

	After enabling, the application must "feed" the watchdog periodically to
	prevent it from expiring and resetting the system.

	Availability of this class: pyboard, WiPy, esp8266, esp32, rp2040, mimxrt.

	[View Doc](https://docs.micropython.org/en/latest/library/machine.WDT.html)
	'''
	def __init__(self, id: int = 0, timeout: int = 5000):
		'''
		Create a WDT object and start it.

		The `timeout` must be given in milliseconds.

		Once it is running the `timeout` cannot be changed and the WDT cannot be
		stopped either.

		Notes:

			On the esp8266 a timeout cannot be specified, it is determined by the
			underlying system.

			On rp2040 devices, the maximum timeout is 8388 ms.
		'''

	# Methods
	def feed(self):
		'''
		Feed the WDT to prevent it from resetting the system.

		The application should place this call in a sensible place ensuring that
		the WDT is only fed after verifying that everything is functioning correctly.
		'''
