'''
与 ESP8266 和 ESP32 相关的功能

esp 模块包含与 ESP8266 和 ESP32 模组相关的特定功能。

有些功能只能在其中一个端口上使用。

[查看文档](https://docs.micropython.org/en/latest/library/esp.html)
'''
import typing


# Constants
SLEEP_NONE = ...
SLEEP_MODEM = ...
SLEEP_LIGHT = ...

# Functions
@typing.overload
def sleep_type() -> int:
	'''
	获取睡眠类型。

	可能的睡眠类型被定义为常量：

	- `SLEEP_NONE` - 启用所有功能

	- `SLEEP_MODEM` - 调制解调器睡眠，关闭 WiFi 调制解调器电路

	- `SLEEP_LIGHT` - 轻度睡眠，关闭 WiFi 调制解调器电路并定期暂停处理器

	注意：

		仅适用于 ESP8266
	'''

@typing.overload
def sleep_type(sleep_type: int):
	'''
	将睡眠类型设置为`sleep_type`。

	可能的睡眠类型被定义为常量：

	- `SLEEP_NONE` - 启用所有功能

	- `SLEEP_MODEM` - 调制解调器睡眠，关闭 WiFi 调制解调器电路

	- `SLEEP_LIGHT` - 轻度睡眠，关闭 WiFi 调制解调器电路并定期暂停处理器运行

	在可能的情况下，系统会自动进入设定的睡眠模式。

	注意：

		仅适用于 ESP8266
	'''

def deepsleep(time_us: int = 0, /):
	'''
	进入深度睡眠。

	除 RTC 时钟电路外，整个模块断电，如果 16 引脚连接到复位引脚，则可在指定时间后重启模块。

	否则，模块将进入休眠状态，直至手动复位。

	注意：

		仅适用于 ESP8266 - 在 ESP32 上使用`machine.deepsleep()`代替。
	'''

def flash_id():
	'''
	读取闪存的设备 ID。

	注意：

		仅适用于 ESP8266
	'''

def flash_size() -> int:
	'''读取闪存的总大小。'''

def flash_user_start() -> int:
	'''读取用户闪存空间开始的内存偏移量。'''

def flash_read(byte_offset, length_or_buffer): ...

def flash_write(byte_offset, bytes): ...

def flash_erase(sector_no): ...

def osdebug(uart_no, level: int = None):
	'''
	更改操作系统串行调试日志信息的级别。

	启动时，操作系统串行调试日志信息仅限于错误输出。

	该函数的行为取决于传递给它的参数，支持以下组合：

	- `osdebug(None)`恢复默认的操作系统调试日志信息级别（`LOG_ERROR`）
	- `osdebug(0)`启用所有可用的操作系统调试日志信息（在默认构建配置中为`LOG_INFO`）
	- `osdebug(0, level)`将操作系统调试日志信息级别设置为指定值。日志级别被定义为常量：

		- `LOG_NONE` - 无日志输出
		- `LOG_ERROR` - 严重错误，软件模块无法自行恢复
		- `LOG_WARN` - 已采取恢复措施的错误情况
		- `LOG_INFO` - 描述正常事件流程的信息消息
		- `LOG_DEBUG` - 正常使用中不需要的额外信息（值、指针、大小等）
		- `LOG_VERBOSE` - 较大块的调试信息，或可能导致输出泛滥的频繁信息

	注意：

		`LOG_DEBUG`和`LOG_VERBOSE`默认不编译到 MicroPython 二进制文件中，以节省文件大小。

		要查看这些日志级别的任何输出，需要使用修改过的 "`sdkconfig`"源文件进行自定义编译。

		在“原始 REPL”模式下，ESP32 上的日志输出会自动暂停，以防止出现通信问题。

		这意味着在使用`mpremote run`和类似工具时，永远看不到操作系统级别的日志。

		这是 ESP32 形式的函数。
	'''

def set_native_code_location(start: int = None, length: int = None):
	'''
	设置本地代码编译后的执行位置。

	当`@micropython.native`、`@micropython.viper`和`@micropython.asm_xtensa`装饰器被应用到函数时，本地代码就会被执行。

	ESP8266 必须从 iRAM 或较低的 1MByte 闪存（内存映射）中执行代码，该函数控制代码的位置。

	如果`start`和`length`均为`None`，则本地代码位置将被设置为 iRAM1 区域末端未使用的内存部分。

	这部分未使用内存的大小取决于固件，通常很小（约 500 字节），足以存储几个很小的函数。

	使用 iRAM1 区域的好处是不会因为写入而耗尽。

	如果`start`和`length`都不是`None`，那么它们应该是整数。

	`start应指定存储本地代码的闪存开头的字节偏移量。

	`length`指定从`start`开始存储本地代码的闪存字节数。

	`start`和`length`应该是扇区大小（4096 字节）的倍数。

	在写入闪存之前，闪存会被自动擦除，因此请确保使用的闪存区域不被其他设备（例如固件或文件系统）使用。

	使用闪存存储本地代码时，`start + length`必须小于或等于 1MB。

	请注意，如果反复擦除（和写入），闪存可能会被耗尽，因此请谨慎使用此功能。

	特别是在每次启动（包括从深度睡眠唤醒）时，都需要重新编译和重写本地代码到闪存中。

	在使用 iRAM1 或闪存的上述两种情况下，如果指定区域已没有剩余空间，那么在函数上使用本地装饰器将导致在编译该函数时出现`MemoryError`异常。

	注意：

		仅适用于 ESP8266
	'''
