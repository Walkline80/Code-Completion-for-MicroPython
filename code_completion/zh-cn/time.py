'''
时间相关功能

此模块实现相应`CPython`模块的子集，如下所述。

有关更多信息，请参阅原始`CPython`文档：[time](https://docs.python.org/3.5/library/time.html#module-time)。

`time`模块提供用于获取当前时间和日期、测量时间间隔和延迟的功能。

[查看文档](https://docs.micropython.org/en/latest/library/time.html)
'''
# Functions
def gmtime(secs: int = None) -> tuple:
	'''
	将自从新纪元以来以秒为单位表示的时间`secs`转换为包含以下内容的 8 元组：

		`(year, month, mday, hour, minute, second, weekday, yearday)`

	如果未提供`secs`或者为`None`，则使用 RTC 的当前时间。

	此函数以 UTC 格式返回日期时间元组。

	8 元组中条目的格式为：

	- `year`包括世纪（例如 2014 年）。
	- `month`是 1-12
	- `mday`是 1-31
	- `hour`是 0-23
	- `minute`是 0-59
	- `second`是 0-59
	- `weekday`是 0-6（周一至周日）
	- `yearday`是 1-366
	'''

def localtime(secs: int = None) -> tuple:
	'''
	将自从新纪元以来以秒为单位表示的时间`secs`转换为包含以下内容的 8 元组：

		`(year, month, mday, hour, minute, second, weekday, yearday)`

	如果未提供`secs`或者为`None`，则使用 RTC 的当前时间。

	此函数返回本地时间的日期时间元组。

	8 元组中条目的格式为：

	- `year`包括世纪（例如 2014 年）。
	- `month`是 1-12
	- `mday`是 1-31
	- `hour`是 0-23
	- `minute`是 0-59
	- `second`是 0-59
	- `weekday`是 0-6（周一至周日）
	- `yearday`是 1-366
	'''

def mktime(datetime: tuple) -> int:

	'''
	这是`localtime()`的反函数。

	它的参数是一个完整的 8 元组，它表示每个本地时间的时间。

	它返回一个整数，即自 2000 年 1 月 1 日以来的秒数。
	'''

def sleep(seconds: int | float):
	'''
	睡眠给定的`秒数`。

	某些开发板可能接受`秒`作为浮点数，以休眠`秒`的小数。

	请注意，其他开发板可能不接受浮点参数，为了与它们兼容，请使用`sleep_ms()`和`sleep_us()`函数。
	'''

def sleep_ms(ms: int):
	'''
	延迟给定的毫秒数，`ms`应为正数或 0。

	此函数将至少延迟给定的毫秒数，但如果必须进行其他处理，例如中断处理程序或其他线程，则可能需要更长的时间。

	将 0 传递给`ms`仍将允许进行其他处理。

	使用`sleep_us()`以获得更精确的延迟。
	'''

def sleep_us(us: int):
	'''
	延迟给定微秒数，`us`应为正数或 0。

	此函数尝试提供至少`us`微秒的准确延迟，但如果系统要执行其他更高优先级的处理，则可能需要更长的时间。
	'''

def ticks_ms() -> int:
	'''
	返回具有任意引用点的递增毫秒计数器，该计数器在某个值之后进行归零反转。

	反转值没有显式公开，但是为了简化讨论，我们将其称为`TICKS_MAX`。

	反转周期值为`TICKS_PERIOD = TICKS_MAX + 1`。

	`TICKS_PERIOD`保证是 2 的幂，但是在其他情况下可能因端口不同而有所不同。

	所有的`ticks_ms()`、`ticks_us()`、`ticks_cpu()`函数都使用相同的周期值(为了简单起见)。

	因此，这些函数将返回一个范围为`[0 .. TICKS_MAX]`的值，包括总的`TICKS_PERIOD`值。

	请注意，只使用非负值。在大多数情况下，应该将这些函数返回的值视为不透明的。

	它们唯一可用的操作是`ticks_diff()`和`ticks_add()`函数。

	注意:

		直接对这些值执行标准的数学运算(+, -)或关系运算符(<, <=, >, >=)将导致无效的结果。

		执行数学运算，然后将它们的结果作为参数传递给`ticks_diff()`或`ticks_add()`，也会导致后者函数的结果无效。
	'''

def ticks_us() -> int:
	'''就像`ticks_ms()`一样，但以微秒为单位。'''

def ticks_cpu() -> int:
	'''
	类似于`ticks_ms()`和`ticks_us()`，但在系统中具有尽可能高的分辨率。

	这通常是 CPU 时钟，这就是为什么函数被这样命名。

	但是它不一定是一个 CPU 时钟，可以使用系统中其他可用的计时源（例如高分辨率计时器）来代替。

	这个函数的精确计时单元（分辨率）没有在时间模块级别上指定，但是针对特定端口的文档可以提供更具体的信息。

	此功能用于非常精细的基准测试或非常紧凑的实时循环。

	避免在可移植代码中使用它。

	可用性：

		并非每个端口都实现此功能。
	'''

def ticks_add(ticks: int, delta: int) -> int:
	'''
	偏移给定的`ticks`值，可以是正数也可以是负数。

	给定一个`ticks`值，此函数允许在其之前或之后计算`delta`个`ticks`值，遵循模运算定义的`ticks`值。

	`ticks`参数必须是对`ticks_ms()`、`ticks_us()`或`ticks_cpu()`函数的直接调用的结果（或来自先前对`ticks_add()`的调用）。

	然而，`delta`可以是任意整数或数值表达式。

	`ticks_add()`用于计算事件/任务的截止日期。（注意：您必须使用`ticks_diff()`函数来处理截止日期。）
	'''

def ticks_diff(ticks1: int, ticks2: int) -> int:
	'''
	度量从`ticks_ms()`、`ticks_us()`或`ticks_cpu()`函数返回的值之间的差值，作为可以归零反转的有符号值。

	参数顺序与减法运算符相同，`ticks_diff(ticks1, ticks2)`与`ticks1 - ticks2`具有相同的含义。
	'''

def time() -> int:
	'''
	以整数形式返回自新纪元以来的秒数，假设基础 RTC 已按上述方式设置和维护。

	如果未设置 RTC，此函数将返回自端口特定参考点以来的秒数（对于没有电池备份 RTC 的开发版来说，通常是自上电或复位以来）。

	如果要开发可移植的 MicroPython 应用程序，则不应依赖此函数来提供高于秒级的精度。

	如果需要更高精度的绝对时间戳，请使用`time_ns()`。

	如果相对时间是可以接受的，则使用`ticks_ms()`和`ticks_us()`函数。

	如果您需要日历时间，不带参数的`gmtime()`或`localtime()`是更好的选择。
	'''

def time_ns() -> int:
	'''
	类似于`time()`，但返回自新纪元以来的纳秒数，作为整数（通常是一个大整数，因此将在堆上分配）。
	'''
