'''
functionality specific to the ESP32

The esp32 module contains functions and classes specifically aimed at controlling
ESP32 modules.

[View Doc](https://docs.micropython.org/en/latest/library/esp32.html)
'''
import typing


# Constants
HEAP_DATA: int = ...
HEAP_EXEC: int = ...

WAKEUP_ALL_LOW: bool = ...
WAKEUP_ANY_HIGH: bool = ...

# Functions
def wake_on_touch(wake: bool):
	'''
	Configure whether or not a touch will wake the device from sleep.

	`wake` should be a boolean value.
	'''

def wake_on_ulp(wake: bool):
	'''
	Configure whether or not the Ultra-Low-Power co-processor can wake the device
	from sleep.

	`wake` should be a boolean value.
	'''

def wake_on_ext0(pin, level: int):
	'''
	Configure how EXT0 wakes the device from sleep.

	- `pin` can be `None` or a valid Pin object.
	- `level` should be `esp32.WAKEUP_ALL_LOW` or `esp32.WAKEUP_ANY_HIGH`.
	'''

def wake_on_ext1(pins: tuple | list | None, level: int):
	'''
	Configure how EXT1 wakes the device from sleep.

	- `pins` can be `None` or a tuple/list of valid Pin objects.

	- `level` should be `esp32.WAKEUP_ALL_LOW` or `esp32.WAKEUP_ANY_HIGH`.
	'''

def gpio_deep_sleep_hold(enable: bool):
	'''
	Configure whether non-RTC GPIO pin configuration is retained during deep-sleep
	mode for held pads.

	`enable` should be a boolean value.
	'''

def raw_temperature() -> int:
	'''
	Read the raw value of the internal temperature sensor, returning an integer.
	'''

def idf_heap_info(capabilities: int) -> list:
	'''
	Returns information about the ESP-IDF heap memory regions.

	One of them contains the MicroPython heap and the others are used by ESP-IDF,
	e.g., for network buffers and other data.

	This data is useful to get a sense of how much memory is available to ESP-IDF
	and the networking stack in particular.

	It may shed some light on situations where ESP-IDF operations fail due to
	allocation failures.

	The `capabilities` parameter corresponds to ESP-IDF’s `MALLOC_CAP_XXX` values
	but the two most useful ones are predefined as `esp32.HEAP_DATA` for data heap
	regions and `esp32.HEAP_EXEC` for executable regions as used by the native code
	emitter.

	The return value is a list of 4-tuples, where each 4-tuple corresponds to one
	heap and contains:

	- total bytes
	- free bytes
	- largest free block
	- minimum free seen over time
	'''


# Flash partitions
class Partition(object):
	'''
	This class gives access to the partitions in the device’s flash memory and
	includes methods to enable over-the-air (OTA) updates.
	'''
	# Constants
	BOOT: int = ...
	'''Partition will be booted at the next reset'''

	RUNNING: int = ...
	'''The currently running partition'''

	TYPE_APP: int = ...
	'''
	For bootable firmware partitions (typically labelled `factory`, `ota_0`,
	`ota_1`)
	'''

	TYPE_DATA: int = ...
	'''For other partitions, e.g. `nvs`, `otadata`, `phy_init`, `vfs`'''

	def __init__(self, id: str | int, block_size: int = 4096, /):
		'''
		Create an object representing a partition.

		`id` can be a string which is the label of the partition to retrieve,
		or one of the constants: `BOOT` or `RUNNING`.

		`block_size` specifies the byte size of an individual block.
		'''

	@staticmethod
	def find(type: int = TYPE_APP, subtype: int = 0xff, label: str = None,
		block_size: int = 4096) -> list:
		'''
		Find a partition specified by `type`, `subtype` and `label`.

		Returns a (possibly empty) list of Partition objects.

		Note:

			`subtype=0xff` matches any subtype and `label=None` matches any label.

		- `block_size` specifies the byte size of an individual block used by the
		returned objects.
	'''

	def info(self) -> tuple:
		'''
		Returns a 6-tuple `(type, subtype, addr, size, label, encrypted)`.
		'''

	def readblocks(self, block_num, buf, offset=None):
		'''
		These methods implement the simple and extended block protocol defined by
		`vfs.AbstractBlockDev`.
		'''

	def writeblocks(self, block_num, buf, offset=None):
		'''
		These methods implement the simple and extended block protocol defined by
		`vfs.AbstractBlockDev`.
		'''

	def ioctl(self, cmd, arg):
		'''
		These methods implement the simple and extended block protocol defined by
		`vfs.AbstractBlockDev`.
		'''

	def set_boot(self):
		'''
		Sets the partition as the boot partition.

		Note:

			Do not enter `deepsleep` after changing the OTA boot partition, without
			first performing a hard `reset` or power cycle.

			This ensures the bootloader will validate the new image before booting.
		'''

	def get_next_update(self) -> typing.Self:
		'''
		Gets the next update partition after this one, and returns a new Partition
		object.

		Typical usage is `Partition(Partition.RUNNING).get_next_update()` which
		returns the next partition to update given the current running one.
		'''

	@classmethod
	def mark_app_valid_cancel_rollback(cls):
		'''
		Signals that the current boot is considered successful.

		Calling `mark_app_valid_cancel_rollback` is required on the first boot of a
		new partition to avoid an automatic rollback at the next boot.

		This uses the ESP-IDF "app rollback" feature with
		"CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE" and an `OSError(-261)` is raised if
		called on firmware that doesn’t have the feature enabled.

		It is OK to call `mark_app_valid_cancel_rollback` on every boot and it is
		not necessary when booting firmware that was loaded using esptool.
		'''


# RMT
class RMT(object):
	'''
	The RMT (Remote Control) module, specific to the ESP32, was originally designed
	to send and receive infrared remote control signals.

	However, due to a flexible design and very accurate (as low as 12.5ns) pulse
	generation, it can also be used to transmit or receive many other types of
	digital signals.
	'''
	# Constants
	PULSE_MAX: int = ...
	'''Maximum integer that can be set for a pulse duration'''

	def __init__(self, channel: int, *, pin=None, clock_div: int = 8,
		idle_level: bool = False, tx_carrier: tuple = None):
		'''
		This class provides access to one of the eight RMT channels.

		- `channel` is required and identifies which RMT channel (0-7) will be
		configured.

		- `pin`, also required, configures which Pin is bound to the RMT channel.

		- `clock_div` is an 8-bit clock divider that divides the source clock
		(80MHz) to the RMT channel allowing the resolution to be specified.

		- `idle_level` specifies what level the output will be when no transmission
		is in progress and can be any value that converts to a boolean, with `True`
		representing high voltage and `False` representing low.

		To enable the transmission carrier feature, `tx_carrier` should be a tuple
		of three positive integers:

		- carrier frequency
		- duty percent (`0` to `100`)
		- output level to apply the carrier to (a boolean as per `idle_level`)
		'''

	@staticmethod
	def source_freq() -> int:
		'''
		Returns the source clock frequency.

		Currently the source clock is not configurable so this will always
		return 80MHz.
		'''

	def clock_div(self) -> int:
		'''
		Return the clock divider.

		Note that the channel resolution is `1 / (source_freq / clock_div)`.
		'''

	def wait_done(self, *, timeout: int = 0) -> bool:
		'''
		Returns True if the channel is idle or False if a sequence of pulses
		started with `RMT.write_pulses` is being transmitted.

		If the `timeout` keyword argument is given then block for up to this many
		milliseconds for transmission to complete.
		'''

	def loop(self, enable_loop: bool):
		'''
		Configure looping on the channel.

		`enable_loop` is bool, set to `True` to enable looping on the next call
		to `RMT.write_pulses`.

		If called with `False` while a looping sequence is currently being
		transmitted then the current loop iteration will be completed and then
		transmission will stop.
		'''

	def write_pulses(self, duration: int | tuple | list, data=None):
		'''
		Begin transmitting a sequence. There are three ways to specify this:

		- `Mode 1`: `duration` is a list or tuple of durations.

			The optional `data` argument specifies the initial output level.

			The output level will toggle after each duration.

		- `Mode 2`: `duration` is a positive integer and `data` is a list or tuple
		of output levels.

			`duration` specifies a fixed duration for each.

		- `Mode 3`: `duration` and `data` are lists or tuples of equal length,
		specifying individual durations and the output level for each.

		Durations are in integer units of the channel resolution
		(as described above), between `1` and `PULSE_MAX` units.

		Output levels are any value that can be converted to a boolean, with `True`
		representing high voltage and `False` representing low.

		If transmission of an earlier sequence is in progress then this method
		will block until that transmission is complete before beginning the new
		sequence.

		If looping has been enabled with `RMT.loop`, the sequence will be repeated
		indefinitely.

		Further calls to this method will block until the end of the current loop
		iteration before immediately beginning to loop the new sequence of pulses.

		Looping sequences longer than 126 pulses is not supported by the hardware.
		'''

	@typing.overload
	@staticmethod
	def bitstream_channel() -> int:
		'''
		This function returns the current channel number.

		The default RMT channel is the highest numbered one.
		'''

	@typing.overload
	@staticmethod
	def bitstream_channel(value: int | None) -> int:
		'''
		Select which RMT channel is used by the `machine.bitstream` implementation.

		`value` can be None or a valid RMT channel number.

		The default RMT channel is the highest numbered one.

		Passing in None disables the use of RMT and instead selects a bit-banging
		implementation for `machine.bitstream`.

		Passing in no argument will not change the channel.

		This function returns the current channel number.
		'''


# Ultra-Low-Power co-processor
class ULP(object):
	'''
	This class gives access to the Ultra Low Power (ULP) co-processor on the
	ESP32, ESP32-S2 and ESP32-S3 chips.

	Warning:

		This class does not provide access to the RISCV ULP co-processor available
		on the ESP32-S2 and ESP32-S3 chips.
	'''
	def set_wakeup_period(self, period_index: int, period_us: int):
		'''Set the wake-up period.'''

	def load_binary(self, load_addr: int, program_binary):
		'''Load a `program_binary` into the ULP at the given `load_addr`.'''

	def run(self, entry_point):
		'''Start the ULP running at the given entry_point.'''


# Non-Volatile Storage
class NVS(object):
	'''
	This class gives access to the Non-Volatile storage managed by ESP-IDF.

	The NVS is partitioned into namespaces and each namespace contains typed
	key-value pairs.

	The keys are strings and the values may be various integer types, strings,
	and binary blobs.

	The driver currently only supports 32-bit signed integers and blobs.

	Warning:

		Changes to NVS need to be committed to flash by calling the `commit` method.

		Failure to call `commit` results in changes being lost at the next reset.
	'''
	def __init__(self, namespace):
		'''
		Create an object providing access to a `namespace` (which is automatically
		created if not present).
		'''

	def set_i32(self, key: str, value: int):
		'''
		Sets a 32-bit signed integer `value` for the specified `key`.

		Remember to call commit!
		'''

	def get_i32(self, key: str) -> int:
		'''
		Returns the signed integer value for the specified `key`.

		Raises an `OSError` if the key does not exist or has a different type.
		'''

	def set_blob(self, key: str, value):
		'''
		Sets a binary blob `value` for the specified `key`.

		The `value` passed in must support the buffer protocol, e.g. `bytes`,
		`bytearray`, `str`.

		(Note that esp-idf distinguishes blobs and strings, this method always
		writes a blob even if a string is passed in as value.)

		Remember to call commit!
		'''

	def get_blob(self, key: str, buffer: bytearray) -> int:
		'''
		Reads the value of the blob for the specified `key` into the `buffer`,
		which must be a `bytearray`.

		Returns the actual length read.

		Raises an `OSError` if the key does not exist, has a different type, or
		if the buffer is too small.
		'''

	def erase_key(self, key: str):
		'''Erases a key-value pair.'''

	def commit(self):
		'''Commits changes made by `set_xxx` methods to flash.'''
