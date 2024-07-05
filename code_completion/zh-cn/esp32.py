'''
ESP32 特有的功能

esp32 模块包含专门用于控制 ESP32 模组的函数和类。

[查看文档](https://docs.micropython.org/en/latest/library/esp32.html)
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
	配置触摸是否会将设备从睡眠状态唤醒。

	`wake`应为布尔值。
	'''

def wake_on_ulp(wake: bool):
	'''
	配置超低功耗协处理器能否从睡眠状态唤醒设备。

	`wake`应为布尔值。
	'''

def wake_on_ext0(pin, level: int):
	'''
	配置 EXT0 如何从睡眠状态唤醒设备。

	`pin`可以是`None`或有效的 Pin 对象。

	`level`应为`esp32.WAKEUP_ALL_LOW`或`esp32.WAKEUP_ANY_HIGH`。
	'''

def wake_on_ext1(pins: tuple | list | None, level: int):
	'''
	配置 EXT1 如何从睡眠状态唤醒设备。

	`pins`可以是`None`或有效 Pin 对象的元组/列表。

	`level`应为`esp32.WAKEUP_ALL_LOW`或`esp32.WAKEUP_ANY_HIGH`。
	'''

def gpio_deep_sleep_hold(enable: bool):
	'''
	配置在深度休眠模式下是否保留非 RTC GPIO 引脚配置。

	`enable`应为布尔值。
	'''

def raw_temperature() -> int:
	'''读取内部温度传感器的原始值，返回一个整数。'''

def idf_heap_info(capabilities: int) -> list:
	'''
	返回有关 ESP-IDF 堆内存区域的信息。

	其中一个区域包含 MicroPython 堆，其他区域由 ESP-IDF 使用，如网络缓冲区和其他数据。

	这些数据有助于了解 ESP-IDF 的可用内存，尤其是网络堆栈的可用内存。

	它可以帮助我们了解 ESP-IDF 因分配失败而导致操作失败的情况。

	`capabilities`参数对应于 ESP-IDF 的`MALLOC_CAP_XXX`值，但两个最有用的参数被预定义为：
	`esp32.HEAP_DATA`（用于数据堆区域）和`esp32.HEAP_EXEC`（用于本地代码生成器使用的可执行区域）。

	返回值是一个四元组列表，其中每个四元组对应一个堆，并包含：

	- 总字节数
	- 空闲字节数
	- 最大空闲块
	- 一段时间内看到的最小空闲字节
	'''


# Flash partitions
class Partition(object):
	'''该类允许访问设备闪存中的分区，并包含启用无线 (OTA) 更新的方法。'''
	# Constants
	BOOT: int = ...
	'''分区将在下次重置时加载'''

	RUNNING: int = ...
	'''当前运行的分区'''

	TYPE_APP: int = ...
	'''用于可引导固件分区（通常标注为`factory`、`ota_0`或`ota_1`）'''

	TYPE_DATA: int = ...
	'''用于其他分区，例如`nvs`、`otadata`、`phy_init`和`vfs'''

	def __init__(self, id: str | int, block_size: int = 4096, /):
		'''
		创建一个代表分区的对象。

		`id`可以是一个字符串，即要检索的分区的标签，也可以是常量之一：`BOOT`或`RUNNING`。

		`block_size`指定单个块的字节大小。
		'''

	@staticmethod
	def find(type: int = TYPE_APP, subtype: int = 0xff, label: str = None,
		block_size: int = 4096) -> list:
		'''
		查找由`type`、`subtype`和`label`指定的分区。

		返回分区对象的列表（可能为空）。

		注意：

			`subtype=0xff`匹配任何子类型，`label=None`匹配任何标签。

		`block_size`指定返回对象使用的单个块的字节大小。
	'''

	def info(self) -> tuple:
		'''
		返回一个六个元组，包含`(type, subtype, addr, size, label, encrypted)`。
		'''

	def readblocks(self, block_num, buf, offset=None):
		'''这些方法实现了`vfs.AbstractBlockDev`所定义的简单和扩展块协议。'''

	def writeblocks(self, block_num, buf, offset=None):
		'''这些方法实现了`vfs.AbstractBlockDev`所定义的简单和扩展块协议。'''

	def ioctl(self, cmd, arg):
		'''这些方法实现了`vfs.AbstractBlockDev`所定义的简单和扩展块协议。'''

	def set_boot(self):
		'''
		将分区设置为启动分区。

		注意：

			更改 OTA 启动分区后，请勿在未执行硬重置或重启电源的情况下进入`deepsleep`状态。

			这样可确保引导加载程序在启动前验证新映像。
		'''

	def get_next_update(self) -> typing.Self:
		'''
		获取此分区后的下一个更新分区，并返回一个新的分区对象。

		典型用法是`Partition(Partition.RUNNING).get_next_update()`，
		它会根据当前运行的分区返回下一个要更新的分区。
		'''

	@classmethod
	def mark_app_valid_cancel_rollback(cls):
		'''
		当前启动成功的信号。

		在新分区首次启动时需要调用`mark_app_valid_cancel_rollback`，以避免下次启动时自动回滚。

		这将使用 ESP-IDF 的 “应用程序回滚”功能（"CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE"），
		如果在未启用该功能的固件上调用，将引发`OSError(-261)`错误。

		在每次启动时调用`mark_app_valid_cancel_rollback`是可以的，但在启动使用 esptool
		烧录的固件时则没有必要。
		'''


# RMT
class RMT(object):
	'''
	RMT（遥控）模块是 ESP32 的专用模块，最初设计用于发送和接收红外遥控信号。

	不过，由于设计灵活，脉冲生成非常精确（低至 12.5ns），它也可用于发送或接收许多其他类型的数字信号。
	'''
	# Constants
	PULSE_MAX: int = ...
	'''脉冲持续时间可设置的最大整数'''

	def __init__(self, channel: int, *, pin=None, clock_div: int = 8,
		idle_level: bool = False, tx_carrier: tuple = None):
		'''
		该类提供对八个 RMT 通道之一的访问。

		- `channel`为必填项，用于确定要配置的 RMT 通道（0-7）。

		- `pin`也是必填项，用于配置哪个引脚与 RMT 通道绑定。

		- `clock_div`是一个 8 位时钟分频器，用于将源时钟（80MHz）分频到 RMT
		通道，以便指定分辨率。

		- `idle_level`指定无传输时的输出电平，可以是任何转换为布尔值的值，
		`True`代表高电压，`False`代表低电压。

		要启用传输载波功能，`tx_carrier`应为三个正整数的元组：

		- 载波频率
		- 占空比（`0`至`100`）
		- 应用载波的输出电平（与`idle_level`相同的布尔值）
		'''

	@staticmethod
	def source_freq() -> int:
		'''
		返回源时钟频率。

		目前，源时钟不可配置，因此将始终返回 80MHz。
		'''

	def clock_div(self) -> int:
		'''
		返回时钟分频器。

		请注意，通道分辨率为`1 / (source_freq / clock_div)`。
		'''

	def wait_done(self, *, timeout: int = 0) -> bool:
		'''
		如果通道处于空闲状态，则返回`True`，如果正在传输以`RMT.write_pulses`开始的脉冲序列，则返回`False`。

		如果给定了`timeout`关键字参数，则会最多阻塞`timeout`毫秒的时间以完成传输。
		'''

	def loop(self, enable_loop: bool):
		'''
		配置通道上的循环。

		`enable_loop`为布尔值，设置为`True`可在下一次调用`RMT.write_pulses`时启用循环。

		如果为`False`，在当前传输循环序列时，当前循环迭代将完成，然后停止传输。
		'''

	def write_pulses(self, duration: int | tuple | list, data=None):
		'''
		开始传输序列。有三种指定方式：

		- `模式 1`：`duration`是一个持续时间列表或元组。

			可选的`data`参数指定初始输出电平。

			输出电平将在每个持续时间后切换。

		- `模式 2`：`duration`为正整数，`data`为输出电平列表或元组。

			`duration`为每个数据指定一个固定的持续时间。

		- `模式 3`：`duration`和`data`是等长的列表或元组，指定了每个持续时间和每个持续时间的输出电平。

		持续时间以通道分辨率的整数单位表示（如上所述），介于`1`和`PULSE_MAX`单位之间。

		输出电平是任何可以转换为布尔值的值，`True`代表高电压，`False`代表低电压。

		如果正在传输先前的序列，则该方法将阻塞，直到传输完成后才开始新的序列。

		如果使用`RMT.loop`启用了循环，则序列将无限重复。

		进一步调用此方法将阻塞到当前循环迭代结束，然后立即开始循环新的脉冲序列。

		硬件不支持超过 126 个脉冲的循环序列。
		'''

	@typing.overload
	@staticmethod
	def bitstream_channel() -> int:
		'''
		此函数将返回当前的通道编号。

		默认的 RMT 通道是编号最高的通道。
		'''

	@typing.overload
	@staticmethod
	def bitstream_channel(value: int | None) -> int:
		'''
		选择一个用于`machine.bitstream`的 RMT 通道。

		`value`可以是`None`或有效的 RMT 通道编号。

		默认的 RMT 通道是编号最高的通道。

		传入`None`会禁用 RMT，并为`machine.bitstream`选择 BitBanging。

		此函数将返回当前的通道编号。
		'''


# Ultra-Low-Power co-processor
class ULP(object):
	'''
	该类可访问 ESP32、ESP32-S2 和 ESP32-S3 芯片上的超低功耗协处理器。

	警告：

		该类不能访问 ESP32-S2 和 ESP32-S3 芯片上的 RISCV ULP 协处理器。
	'''
	def set_wakeup_period(self, period_index: int, period_us: int):
		'''设置唤醒周期。'''

	def load_binary(self, load_addr: int, program_binary):
		'''
		在给定的`load_addr`处将`program_binary`加载到 ULP 中。
		'''

	def run(self, entry_point):
		'''启动在给定`entry_point`运行的 ULP。'''


# Non-Volatile Storage
class NVS(object):
	'''
	该类可访问由 ESP-IDF 管理的非易失性存储器。

	NVS 被划分为多个命名空间，每个命名空间都包含键值对类型。

	键是字符串，值可能是各种整数类型、字符串和二进制对象。

	驱动程序目前仅支持 32 位有符号整数和对象。

	警告：

		对 NVS 的更改需要通过调用`commit`方法提交到闪存。

		如果未调用`commit`方法，下次重置时将丢失更改。
	'''
	def __init__(self, namespace):
		'''创建一个对象，提供对`namespace`的访问（如果不存在，则自动创建）。'''

	def set_i32(self, key: str, value: int):
		'''
		为指定的`key`设置一个 32 位有符号整数`value`。

		记得调用`commit()`。
		'''

	def get_i32(self, key: str) -> int:
		'''
		返回指定`key`的有符号整数值。

		如果键不存在或键值类型不同，则会引发`OSError`。
		'''

	def set_blob(self, key: str, value):
		'''
		为指定的`key`设置二进制对象`value`。

		传入的`value`必须支持缓冲协议，例如`bytes`、`bytearray`、`str`。

		请注意，esp-idf 区分二进制对象和字符串，即使传递的值是字符串，此方法也总是写入一个二进制对象）。

		记得调用`commit()`。
		'''

	def get_blob(self, key: str, buffer: bytearray) -> int:
		'''
		将指定`key`的二进制对象读入`buffer`（必须是`bytearray`）。

		返回实际读取的长度。

		如果键不存在或键的类型不同或缓冲区太小，则会引发`OSError`错误。
		'''

	def erase_key(self, key: str):
		'''擦除键值对。'''

	def commit(self):
		'''将`set_xxx`方法所做的更改提交至闪存。'''
