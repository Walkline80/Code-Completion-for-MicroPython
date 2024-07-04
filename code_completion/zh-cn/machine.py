'''
与硬件相关的功能

`machine`模块包含与特定开发板上的硬件相关的特定功能。

该模块中的大多数功能允许直接和不受限制地访问和控制系统上的硬件（如 CPU、定时器、总线等）。

使用不当可能会导致开发板故障、锁定、崩溃，在极端情况下还会导致硬件损坏。

[查看文档](https://docs.micropython.org/en/latest/library/machine.html)
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
	'''读/写 8 位内存。'''

def mem16():
	'''读/写 16 位内存。'''

def mem32():
	'''读/写 32 位内存。'''

# Reset related functions
def reset():
	'''以类似于按下外部 RESET 按钮的方式重置设备。'''

def soft_reset():
	'''
	执行解释器的软重置，删除所有 Python 对象并重置 Python 堆。

	它试图保留用户连接到 MicroPython REPL 的方法（例如串行，USB，Wifi）。
	'''

def reset_cause():
	'''获取重置原因。'''

def bootloader(value=None):
	'''
	重置设备并进入其引导加载程序。

	这通常用于将设备置于可以使用新固件进行编程的状态。

	某些端口支持传入可选的`value`参数，该参数可以控制要输入哪个引导加载程序、传递给它什么或其它内容。
	'''

# Interrupt related functions
def disable_irq() -> int:
	'''
	禁用中断请求。

	返回应被视为不透明值的上一个 IRQ 状态。

	应将此返回值传递给`enable_irq()`函数，以将中断恢复到其原始状态。
	'''

def enable_irq(state: int):
	'''
	重新启用中断请求。

	`state`参数应该是最近调用`disable_irq()`函数时返回的值。
	'''

# Power related functions
@typing.overload
def freq() -> int:
	'''返回 CPU 频率（以赫兹为单位）。'''

@typing.overload
def freq(hz: int):
	'''在某些端口上，这可用于通过传入`hz`来设置 CPU 频率。'''

def idle():
	'''
	将时钟连接到 CPU，有助于在短期或长期内随时降低功耗。

	外设继续工作，一旦触发任何中断，执行就会恢复。

	在许多端口上，这包括以毫秒级的定期间隔发生的系统定时器中断。
	'''

def sleep():
	'''
	注意：

		此函数已弃用，请改为不带参数调用`lightsleep()`作为替代。
	'''

def lightsleep(time_ms: int | None):
	'''
	停止执行以尝试进入低功耗状态。

	如果指定了`time_ms`，则这将是睡眠持续的最长时间（以毫秒为单位）。

	否则，睡眠可以无限期地持续下去。

	无论是否超时，如果存在需要处理的事件，则可以随时恢复执行。

	此类事件或唤醒源应在休眠前配置，例如引脚更改或`RTC`超时。

	lightsleep 的精确行为和节能功能高度依赖于底层硬件，但一般属性为：

	- lightsleep 具有完整的 RAM 和状态保留。

		唤醒后，从请求睡眠的点恢复执行，所有子系统都处于运行状态。
	'''

def deepsleep(time_ms: int | None):
	'''
	停止执行以尝试进入低功耗状态。

	如果指定了`time_ms`，则这将是睡眠持续的最长时间（以毫秒为单位）。

	否则，睡眠可以无限期地持续下去。

	无论是否超时，如果存在需要处理的事件，则可以随时恢复执行。

	此类事件或唤醒源应在休眠前配置，例如引脚更改或`RTC`超时。

	deepsleep 的精确行为和节能功能高度依赖于底层硬件，但一般属性为：

	- 深度睡眠可能不会保留 RAM 或系统的任何其他状态（例如外围设备或网络接口）。

		唤醒后，从主脚本恢复执行，类似于硬重置或开机重置。

		`reset_cause()`函数将返回`machine.DEEPSLEEP`，这可用于将深度睡眠唤醒与其他重置区分开来。
	'''

def wake_reason():
	'''
	获取唤醒原因。

	可用性：ESP32、WiPy。	
	'''

# Miscellaneous functions
def unique_id() -> bytes:
	'''
	返回具有开发板/SoC 唯一标识符的字节字符串。

	如果底层硬件允许，它将因开发板/SoC 实例而异。

	长度因硬件而异（因此，如果需要短 ID，请使用完整值的子字符串）。

	在某些 MicroPython 端口中，ID 对应于网络 MAC 地址。
	'''

def time_pulse_us(pin, pulse_level: int, timeout_us: int = 1000000, /) -> int:
	'''
	在给定的`pin`上对脉冲进行计时，并返回脉冲的持续时间（以微秒为单位）。

	`pulse_level`参数为 0 时为低脉冲计时，为 1 时为高脉冲计时。

	如果`pin`的当前输入值与`pulse_level`不同，则函数首先（*）等待`pin`输入等于`pulse_level`，然后（**）乘以`pin`等于`pulse_level`的持续时间。

	如果`pin`已经等于`pulse_level`，则计时立即开始。

	如果在上面标记为（*）的条件有超时等待，则该函数将返回 -2，如果上面标记为（**）的在主测量期间出现超时，则该函数将返回 -1。

	两种情况下的超时是相同的，由`timeout_us`（以微秒为单位）给出。
	'''

def bitstream(pin, encoding, timing, data, /):
	'''
	通过对指定的`pin`进行 BitBanging 来传输`data`。

	`encoding`参数指定如何对位进行编码，`timing`是特定于编码的时序规范。
	'''

def rng() -> int:
	'''
	返回一个 24 位软件生成的随机数。

	可用性：WiPy。
	'''


class Pin(object):
	'''
	控制 I/O 引脚

	引脚对象用于控制 I/O 引脚（也称为 GPIO - 通用输入/输出）。

	引脚对象通常与物理引脚相关联，该引脚可以驱动输出电压并读取输入电压。

	引脚类具有设置引脚模式（IN、OUT 等）的方法以及获取和设置数字逻辑电平的方法。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.Pin.html)
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
		访问与给定`ID`关联的引脚外设（GPIO 引脚）。

		如果在构造函数中给出了其他参数，则它们将用于初始化引脚。

		任何未指定的设置都将保持其以前的状态。
		'''

	# Methods
	def init(self, mode: int = -1, pull: int = -1, *, value=None, drive: int = 0,
		alt: int = -1):
		'''
		使用给定参数重新初始化引脚。

		仅设置指定的参数。

		引脚外设状态的其余部分将保持不变。
		'''

	@typing.overload
	def value(self) -> int:
		'''获取引脚的值。'''

	@typing.overload
	def value(self, x):
		'''设置引脚的值。'''

	def __call__(self, x=None):
		'''
		Pin 对象是可调用的。

		call 方法提供了一个（快速）快捷方式来设置和获取引脚的值::

		    pin = Pin(2, Pin.OUT)
		    pin(1)
			pin()

		它等效于`Pin.value(x)`。
		'''

	def on(self):
		'''将引脚输出电平设置为“1”。'''

	def off(self):
		'''将引脚输出电平设置为“0”。'''

	def irq(self, handler=None, trigger: int = IRQ_FALLING | IRQ_RISING,
		*, priority: int = 1, wake=None, hard: bool = False):
		'''
		配置一个中断`handler`，在引脚触发源激活时调用。

		如果引脚模式为`Pin.IN`，则触发源是引脚上的外部值。

		如果引脚模式为`Pin.OUT`，则触发源是引脚的输出缓冲区。

		否则，如果引脚模式为`Pin.OPEN_DRAIN`，则触发源是状态为“0”的输出缓冲区和状态为“1”的外部引脚值。
		'''

	def low(self):
		'''
		将引脚输出电平设置为“0”。

		可用性：nrf、rp2、stm32 端口。
		'''

	def high(self):
		'''
		将引脚输出电平设置为“1”。

		可用性：nrf、rp2、stm32 端口。
		'''

	@typing.overload
	def mode(self) -> int:
		'''
		获取引脚模式。

		可用性：cc3200、stm32 端口。
		'''

	@typing.overload
	def mode(self, mode: int):
		'''
		设置引脚模式。

		可用性：cc3200、stm32 端口。
		'''

	@typing.overload
	def pull(self) -> int:
		'''
		获取引脚上下拉状态。

		可用性：cc3200、stm32 端口。
		'''

	@typing.overload
	def pull(self, pull: int):
		'''
		设置引脚上下拉状态。

		可用性：cc3200、stm32 端口。
		'''

	@typing.overload
	def drive(self) -> int:
		'''
		获取引脚驱动强度。

		可用性：cc3200 端口。
		'''

	@typing.overload
	def drive(self, drive: int):
		'''
		设置引脚驱动强度。

		可用性：cc3200 端口。
		'''


class Signal(object):
	'''
	控制和检测外部 I/O 设备

	Signal 类是`Pin`类的简单扩展。

	与只能处于“绝对”0 和 1 状态的 Pin 不同，Signal 可以处于“断言”（开）或“断言”（关）状态，同时可以反相（低电平有效）或不反相。

	换句话说，它为引脚功能增加了逻辑反转支持。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.Signal.html)
	'''
	def __init__(self, pin_obj_or_pin_arguments, *, invert: bool = False):
		'''
		创建 Signal 对象。有两种创建方式：

		- 通过封装现有的 Pin 对象，这是一种通用方法，适用于任何开发板。

		- 直接将所需的 Pin 参数传递给 Signal 构造函数，无需创建中间 Pin 对象。

			在许多开发板上都可以使用、 但并非所有电路板。

		参数如下：

		- `pin_obj` 是现有的 Pin 对象。

		- `pin_arguments` 与传递给 Pin 构造函数的参数相同。

		- `invert` - 如果为`True`，信号将反相（低电平有效）。
		'''

	# Methods
	@typing.overload
	def value(self) -> int:
		'''获取信号的值。'''

	@typing.overload
	def value(self, x):
		'''设置信号的值。'''

	def on(self):
		'''启用信号。'''

	def off(self):
		'''停用信号。'''


class ADCBlock(object):
	'''
	控制 ADC 外设

	ADCBlock 类提供了对 ADC 外设的访问，该外设有多个通道，可用于对模拟值进行采样。

	它允许更精细地控制`machine.ADC`对象的配置，该对象进行实际采样。

	该类并非始终可用。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.ADCBlock.html)
	'''
	def __init__(self, id, *, bits: int | str = None):
		'''
		访问由`id`标识的 ADC 外围设备，id 可以是整数或字符串。

		如果给定参数`bits`，则设置转换过程的分辨率（以位为单位）。

		如果未指定，则使用先前或默认分辨率。
		'''

	# Methods
	def init(self, *, bits: int | str):
		'''
		配置 ADC 外围设备。

		`bits`用于设置转换过程的分辨率。
		'''

	def connect(self, channel: int = None, source=None, *, kwargs):
		'''
		连接 ADC 外围设备上的一个通道，使其可以进行采样，并返回一个代表该连接的 ADC 对象。

		`channel`参数必须是整数，`source`参数必须是可连接用于采样的对象（例如引脚）。

		如果只给出`channel`参数，则配置为采样。

		如果只给出`source`，则该对象将连接到一个默认通道以备采样。

		如果同时给出`channel`和`source`，则会将它们连接在一起并准备采样。

		任何附加关键字参数都将用于通过其`init`方法配置返回的 ADC 对象。
		'''


class ADC(object):
	'''
	模数转换

	ADC 类为模数转换器提供了一个接口，代表了一个可以对连续电压进行采样并将其转换为离散值的单个端点。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.ADC.html)
	'''
	def __init__(self, id, *, sample_ns: int = None, atten: int = None):
		'''
		访问与`id`标识的源相关联的 ADC。

		该`id`可以是一个整数（通常指定一个通道号）、一个`Pin`对象或底层机器支持的其它值。

		如果给定了附加的关键字参数，它们将配置 ADC 的各个方面。

		如果没有给出，这些设置将采用以前的值或默认值。

		这些设置是：

		- `sample_ns`是采样时间（以纳秒为单位）。

		- `atten` 指定输入衰减。
		'''

	# Methods
	def init(self, *, sample_ns: int = None, atten: int = None):
		'''
		将给定的设置应用到 ADC。

		只有指定的参数才会被更改。
		'''

	def block(self) -> ADCBlock:
		'''
		返回与此 ADC 对象相关联的`ADCBlock`实例。

		此方法仅在端口支持`ADCBlock`类时存在。
		'''

	def read_u16(self) -> int:
		'''
		读取模拟读数并返回一个范围在`0-65535`之间的整数。

		返回值表示 ADC 采集的原始读数，其比例为 最小值为 0，最大值为 65535。
		'''

	def read_uv(self) -> int:
		'''
		读取模拟读数并返回整数值（以微伏（mv）为单位）。

		该值是否校准取决于特定端口、以及如何校准。
		'''


class PWM(object):
	'''
	脉宽调制

	该类提供脉冲宽度调制输出。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.PWM.html)
	'''
	def __init__(self, dest, *, freq: int, duty_u16: int, duty_ns: int, invert: bool):
		'''
		使用以下参数构造并返回一个新的 PWM 对象：

		- `dest`是输出 PWM 的实体，通常是`machine.Pin`对象，但端口可能允许其他值，如整数。

		- `freq`应为整数，用于设置 PWM 周期的频率（赫兹）。

		- `duty_u16`以`duty_u16 / 65535`的比率设置占空比。

		- `duty_ns`设置脉冲宽度（以纳秒为单位）。

		- `invert`如果值为`True`，则反相相应的输出。

		如果其他 PWM 对象共享相同的底层 PWM 发生器，则设置`freq`可能会影响这些对象（这是硬件特性）。

		每次只能指定`duty_u16`和`duty_ns`中的一个。

		并非所有端口都可以使用`invert`参数。
		'''

	# Methods
	def init(self, *, freq: int, duty_u16: int, duty_ns: int):
		'''修改 PWM 对象的设置。'''

	def deinit(self):
		'''禁用 PWM 输出。'''

	@typing.overload
	def freq(self) -> int:
		'''获取 PWM 输出的当前频率，返回频率（赫兹）。'''

	@typing.overload
	def freq(self, value: int):
		'''
		设置 PWM 当前输出的频率。

		频率将被设置为`value`（以赫兹为单位）。

		如果频率超出有效范围，该方法可能会引发`ValueError`错误。
		'''

	@typing.overload
	def duty_u16(self) -> int:
		'''
		以 16 位无符号数值形式获取 PWM 当前输出的占空比，范围为 0 至 65535（含
		65535），返回占空比。
		'''

	@typing.overload
	def duty_u16(self, value: int):
		'''
		设置 PWM 当前输出的占空比，数值为 0 至 65535（含 65535）范围内的无符号 16 位数值。

		占空比设置为`value`值，以`value / 65535`来衡量。
		'''

	@typing.overload
	def duty_ns(self) -> int:
		'''获取 PWM 当前输出的脉冲宽度（以纳秒为单位）。'''

	@typing.overload
	def duty_ns(self, value: int):
		'''
		设置 PWM 当前输出的脉冲宽度（以纳秒为单位）。

		脉冲宽度将设置为`value`。
		'''


class UART(object):
	'''
	双工串行通信总线

	UART 实现了标准的 UART/USART 双工串行通信协议。

	在物理层面上，它由 2 条线路组成：RX 和 TX。

	通信单位是字符（不要与字符串混淆），宽度可以是 8 或 9 位。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.UART.html)
	'''
	# Constants
	INV_TX: int = ...
	INV_RX: int = ...
	INV_RTS: int = ...
	INV_CTS: int = ...
	RTS: int = ...
	CTS: int = ...

	RX_ANY: int = ...
	'''IRQ 触发源。可用性：WiPy.'''

	def __init__(self, id: int):
		'''根据给定的`id`构造 UART 对象。'''

	# Methods
	def init(self, baudrate: int = 9600, bits: int = 8, parity: int = None,
		stop: int = 1, *, kwargs):
		'''
		使用给定参数初始化 UART 总线：

		- `baudrate`是时钟频率。
		- `bits`是每个字符的位数，7、8 或 9。
		- `parity`为奇偶校验，`None`、0（偶数）或 1（奇数）。
		- `stop`是停止位，1 或 2。

		端口可能支持的其他关键字参数包括：

		- `tx`指定要使用的 TX 引脚
		- `rx`指定要使用的 RX 引脚
		- `rts`指定用于硬件接收流量控制的 RTS（输出）引脚
		- `cts`指定用于硬件发送流量控制的 CTS（输入）引脚
		- `txbuf`指定 TX 缓冲区的长度（以字符为单位）
		- `rxbuf`指定 RX 缓冲区的长度（以字符为单位）
		- `timeout`指定等待第一个字符的时间（毫秒）
		- `timeout_char`指定字符之间的等待时间（毫秒）
		- `invert`指定要反转的行：

			- `0` - 不会反转线路（两条线路的空闲状态均为逻辑高电平）。
			- `UART.INV_TX` - 将反相 TX 线路（TX 线路的空闲状态现在为逻辑低电平）。
			- `UART.INV_RX` - 将反相 RX 线路（RX 线路的空闲状态现在为逻辑低电平）。
			- `UART.INV_TX | UART.INV_RX` - 将反相两条线路（空闲状态为逻辑低电平）。

		- `flow`指定要使用的硬件流量控制信号。该值是一个位掩码。

			- `0` - 将忽略硬件流量控制信号。
			- `UART.RTS` - 将使用 RTS 输出引脚来指示接收 FIFO 是否有足够空间接收更多数据，从而启用接收流控制。
			- `UART.CTS` - 当 CTS 输入引脚发出接收器缓冲区空间不足的信号时，将暂停传输，从而启用传输流控制。
			- `UART.RTS | UART.CTS` - 将同时启用这两个功能，以实现完全的硬件流量控制。
		'''

	def deinit(self):
		'''关闭 UART 总线。'''

	def any(self) -> int:
		'''
		返回一个整数，表示在不阻塞的情况下可以读取的字符数。

		如果没有可读取的字符，则返回 0；如果有可读取的字符，则返回正数。

		即使有多个字符可供读取，该方法也可能返回 1。
		'''

	@typing.overload
	def read(self) -> bytes | None:
		'''
		读取尽可能多的字节数据。

		如果超时，可能会提前返回，超时时间可在构造函数中配置。

		返回值：包含读入字节的字节对象，超时时返回`None`。
		'''

	@typing.overload
	def read(self, nbytes: int) -> bytes | None:
		'''
		读取最多`nbytes`个字节数据。

		如果超时，可能会提前返回，超时时间可在构造函数中配置。

		返回值：包含读入字节的字节对象，超时时返回`None`。
		'''

	@typing.overload
	def readinto(self, buf) -> int | None:
		'''
		读取字节数据并保存到`buf`中。

		最多读取`len(buf)`字节。

		如果超时，可能会提前返回，超时可在构造函数中配置。

		返回值：读取并存储到`buf`中的字节数，超时时返回`None`。
		'''

	@typing.overload
	def readinto(self, buf, nbytes: int) -> int | None:
		'''
		读取字节数据并保存到`buf`中。

		最多读取`nbytes`的字节数。

		如果超时，可能会提前返回，超时可在构造函数中配置。

		返回值：读取并存储到`buf`中的字节数，超时时返回`None`。
		'''

	def readline(self) -> bytes | None:
		'''
		读取一行数据，以换行符结束。

		如果超时，可能会提前返回，超时时间可在构造函数中配置。

		返回值：读取的行数据，超时时返回`None`。
		'''

	def write(self, buf) -> int | None:
		'''
		将缓冲区中的字节写入总线。

		返回值：写入的字节数，超时时返回`None`。
		'''

	def sendbreak(self):
		'''
		在总线上发送中断条件。

		这将使总线处于低电平，持续时间超过正常传输一个字符所需的时间。
		'''

	def irq(self, trigger: int = RX_ANY, priority=1, handler=None, wake: int = IDLE):
		'''
		创建一个回调，以便在 UART 接收到数据时触发。

		- `trigger`只能是`UART.RX_ANY`

		- `priority`是中断的级别，取值范围为 1-7，数值越大，优先级越高

		- `handler`是新字符到达时调用的可选函数。

		- `wake`只能是`machine.IDLE`。

		返回一个 irq 对象。

		可用性：WiPy.
		'''

	def flush(self):
		'''
		等待所有数据发送完毕。

		如果超时，则会出现异常。

		超时持续时间取决于发送缓冲区大小和波特率。

		除非启用了流量控制，否则不应发生超时。

		可用性：rp2、esp32、esp8266、mimxrt、cc3200、stm32、nrf ports、renesas-ra
		'''

	def txdone(self) -> bool:
		'''
		说明是否所有数据都已发送或没有数据传输。

		在这种情况下，它返回`True`。

		如果正在传输数据，则返回`False`。

		可用性：rp2、esp32、esp8266、mimxrt、cc3200、stm32、nrf ports、renesas-ra
		'''


class SPI(object):
	'''
	串行外设接口总线协议（控制器端）

	SPI 是由控制器驱动的同步串行协议。

	在物理层面上，总线由 3 条线路组成：SCK、MOSI、MISO。

	多个设备可以共享同一总线。

	每个设备都应有一个单独的第 4 个信号 CS（芯片选择），用于选择总线上的特定设备进行通信。

	CS 信号的管理应在用户代码中进行（通过`machine.Pin`类）。

	硬件 SPI 通过 `machine.SPI` 类实现。

	硬件 SPI 使用系统的底层硬件支持来执行读/写操作，通常效率高、速度快，但可能对可使用的引脚有限制。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.SPI.html)
	'''
	# Constants
	CONTROLLER = ...
	'''用于初始化控制器的 SPI 总线，仅用于 WiPy'''

	MSB: int = ...
	'''设置数据第一位为最高位'''

	LSB: int = ...
	'''设置数据第一位为最低位'''

	def __init__(self, id: int):
		'''
		在给定`id`的总线上构建 SPI 对象。`id`的值取决于特定端口及其硬件。

		0、1 等值通常用于选择硬件 SPI 块 #0、#1 等。

		在没有额外参数的情况下，SPI 对象将被创建，但不会被初始化（如果有的话，它将保留上次初始化总线时的设置）。

		如果给出额外参数，总线将被初始化（初始化参数见`SPI.init`）。
		'''

	# Methods
	def init(self, baudrate: int = 1000000, *, polarity: int = 0, phase: int = 0,
		bits: int = 8, firstbit: int = MSB, sck=None, mosi=None, miso=None, pins: tuple = None):
		'''
		使用给定参数初始化 SPI 总线，参数如下：

		- `baudrate`是 SCK 时钟速率
		- `polarity`可以是 0 或 1，是空闲时钟线的电平状态
		- `phase`可以是 0 或 1，分别用于在第一个或第二个时钟沿采样数据
		- `bits`是每次传输的比特宽度，只有 8 位是可以保证在所有硬件上都被支持的
		- `firstbit`可以是`SPI.MSB`或`SPI.LSB`
		- `sck`、`mosi`、`miso`是用于总线信号的引脚（`machine.Pin`）对象

			对于大多数硬件 SPI 块（由构造函数的`id`参数选择），引脚是固定的，不能更改。

			在某些情况下，硬件块允许为硬件 SPI 块设置 2-3 个引脚。

			只有 BitBanging SPI 驱动程序（`id` = -1）才可以任意分配引脚。

		- `pins` - WiPy 端口不使用 `sck`、`mosi`、`miso`参数，而是允许以`pins`参数的元组形式指定。

		在硬件 SPI 的情况下，实际时钟频率可能低于请求的波特率，这取决于平台硬件。

		实际波特率可以通过打印 SPI 对象来确定。
		'''

	def deinit(self):
		'''关闭 SPI 总线。'''

	def read(self, nbytes: int, write=0x00) -> bytes:
		'''
		读取由`nbytes`指定数量的字节，同时连续写入由`write`指定的单字节。

		返回一个字节对象，其中包含已读取的数据。
		'''

	def readinto(self, buf, write=0x00):
		'''
		数据读入`buf`指定的缓冲区，同时连续写入`write`指定的单字节。

		返回`None`。

		注：在 WiPy 上，此函数返回读取的字节数。
		'''

	def write(self, buf):
		'''
		写入`buf`中包含的字节。

		返回`None`。

		注：在 WiPy 上，此函数返回写入的字节数。
		'''

	def write_readinto(self, write_buf, read_buf):
		'''
		从`write_buf`中写入字节，同时向`read_buf`中读取字节。

		两个缓冲区可以相同也可以不同，但它们的长度必须相同。

		返回`None`。

		注：在 WiPy 上，此函数返回写入的字节数。
		'''


class SoftSPI(object):
	'''
	串行外设接口总线协议（控制器端）

	SPI 是由控制器驱动的同步串行协议。

	在物理层面上，总线由 3 条线路组成：SCK、MOSI、MISO。

	多个设备可以共享同一总线。

	每个设备都应有一个单独的第 4 个信号 CS（芯片选择），用于选择总线上的特定设备进行通信。

	CS 信号的管理应在用户代码中进行（通过`machine.Pin`类）。

	软件 SPI 通过 BitBanging 实现，可用于任何引脚，但效率较低。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.SPI.html)
	'''
	# Constants
	CONTROLLER = ...
	'''用于初始化控制器的 SPI 总线，仅用于 WiPy'''

	MSB: int = ...
	'''设置数据第一位为最高位'''

	LSB: int = ...
	'''设置数据第一位为最低位'''

	def __init__(self, baudrate: int = 500000, *, polarity: int = 0, phase: int = 0,
		bits: int = 8, firstbit: int = MSB, sck=None, mosi=None, miso=None):
		'''
		构造一个软件 SPI 对象。

		必须给出附加参数，通常至少包括`sck`、`mosi`和`miso`，这些参数用于初始化总线。

		有关参数的说明，请参考`SPI.init`。
		'''

	# Methods
	def init(self, baudrate: int = 1000000, *, polarity: int = 0, phase: int = 0,
		bits: int = 8, firstbit: int = MSB, sck=None, mosi=None, miso=None, pins: tuple = None):
		'''
		使用给定参数初始化 SPI 总线，参数如下：

		- `baudrate`是 SCK 时钟速率
		- `polarity`可以是 0 或 1，是空闲时钟线的电平状态
		- `phase`可以是 0 或 1，分别用于在第一个或第二个时钟沿采样数据
		- `bits`是每次传输的比特宽度，只有 8 位是可以保证在所有硬件上都被支持的
		- `firstbit`可以是`SPI.MSB`或`SPI.LSB`
		- `sck`、`mosi`、`miso`是用于总线信号的引脚（`machine.Pin`）对象
		- `pins` - WiPy 端口不使用 `sck`、`mosi`、`miso`参数，而是允许以`pins`参数的元组形式指定。

		实际波特率可以通过打印 SPI 对象来确定。
		'''

	def deinit(self):
		'''关闭 SPI 总线。'''

	def read(self, nbytes: int, write=0x00) -> bytes:
		'''
		读取由`nbytes`指定数量的字节，同时连续写入由`write`指定的单字节。

		返回一个字节对象，其中包含已读取的数据。
		'''

	def readinto(self, buf, write=0x00):
		'''
		数据读入`buf`指定的缓冲区，同时连续写入`write`指定的单字节。

		返回`None`。

		注：在 WiPy 上，此函数返回读取的字节数。
		'''

	def write(self, buf):
		'''
		写入`buf`中包含的字节。

		返回`None`。

		注：在 WiPy 上，此函数返回写入的字节数。
		'''

	def write_readinto(self, write_buf, read_buf):
		'''
		从`write_buf`中写入字节，同时向`read_buf`中读取字节。

		两个缓冲区可以相同也可以不同，但它们的长度必须相同。

		返回`None`。

		注：在 WiPy 上，此函数返回写入的字节数。
		'''


class I2C(object):
	'''
	双线串行协议

	I2C 是一种用于设备间通信的双线协议。

	在物理层面上，它由两根线组成：SCL 和 SDA 分别是时钟线和数据线。

	I2C 对象是根据特定总线创建的。它们可以在创建时初始化，也可以在创建后初始化。

	打印 I2C 对象可获得有关其配置的信息。

	硬件 I2C 可通过`machine.I2C`类实现。

	硬件 I2C 使用系统的底层硬件支持来执行读/写操作，通常效率高、速度快，但可能对可使用的引脚有限制。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.I2C.html)
	'''
	def __init__(self, id, *, scl, sda, freq: int = 400000, timeout: int = 50000):
		'''
		使用以下参数构造并返回一个 I2C 对象：

		- `id`标识特定的 I2C 外围设备。允许的值取决于取决于特定端口/开发板
		- `scl`应是一个引脚对象，指定用于 SCL 的引脚
		- `sda`应是一个引脚对象，指定用于 SDA 的引脚
		- `freq`是一个整数，用于设置 SCL 的最大频率
		- `timeout`是允许 I2C 处理事务的最长时间（以微秒为单位）

			某些端口不允许使用此参数。
		'''

	# General Methods
	def init(self, scl, sda, *, freq: int = 400000):
		'''
		使用给定参数初始化 I2C 总线：

		- `scl`是 SCL 线的引脚对象
		- `sda`是 SDA 线的引脚对象
		- `freq`是 SCL 时钟频率

		在硬件 I2C 的情况下，实际时钟频率可能低于所要求的频率，这取决于平台硬件。

		实际频率可通过打印 I2C 对象来确定。
		'''

	def deinit(self):
		'''关闭 I2C 总线。可用性：WiPy。'''

	def scan(self) -> list:
		'''
		扫描介于`0x08`和`0x77`之间的所有 I2C 地址，并返回有响应的设备列表。

		如果设备在总线上发送地址（包括写入位）后将 SDA 线拉至低电平，则该设备响应。
		'''

	# Standard bus operations
	def readfrom(self, addr: int, nbytes: int, stop: bool = True, /) -> bytes:
		'''
		从`addr`指定的外设中读取`nbytes`数据。

		如果`stop`为`True`，则在传输结束时产生一个 STOP 条件。

		返回包含读取数据的字节对象。
		'''

	def readfrom_into(self, addr: int, buf, stop: bool = True, /):
		'''
		从`addr`指定的外设读取数据到`buf`。

		读取的字节数为`buf`的长度。

		如果`stop`为`True`，则在传输结束时会生成一个 STOP 条件。

		该方法返回`None`。
		'''

	def writeto(self, addr: int, buf, stop: bool = True, /) -> int:
		'''
		将`buf`的数据写入由`addr`指定的外设。

		如果在从`buf`中写入字节后收到 NACK，则不会发送剩余字节。

		如果`stop`为`True`，即使收到 NACK，也会在传输结束时产生 STOP 条件。

		函数返回收到的 ACK 数量。
		'''

	def writevto(self, addr: int, vector: tuple | list, stop: bool = True, /) -> int:
		'''
		将`vector`中包含的字节写入`addr`指定的外设。

		`vector`应是一个具有缓冲协议的元组或对象列表。

		先发送一次`addr`，然后按顺序写出`vector`中每个对象的字节。

		在这种情况下，`vector`中的对象长度可能为零字节，它们不参与输出。

		如果从`vector`中的一个对象写入字节后收到 NACK，则不会发送剩余的字节和任何剩余的对象。

		如果`stop`为`True`，即使收到 NACK，也会在传输结束时产生 STOP 条件。

		函数返回收到的 ACK 数量。
		'''

	# Memory operations
	def readfrom_mem(self, addr: int, memaddr: int, nbytes: int, *, addrsize: int = 8) -> bytes:
		'''
		从`addr`指定的外设中读取`nbytes`数据，从`memaddr`指定的内存地址开始。

		参数`addrsize`指定地址大小（以位为单位）。

		返回包含读取数据的字节对象。
		'''

	def readfrom_mem_into(self, addr: int, memaddr: int, buf, *, addrsize=8):
		'''
		从`addr`指定的外设读取数据到`buf`，从`memaddr`指定的内存地址开始。

		读取的字节数是`buf`的长度。

		参数`addrsize`指定地址大小（以位为单位）。（在 ESP8266 上，该参数不被识别，地址大小始终为 8 位）。

		该方法返回`None`。
		'''

	def writeto_mem(self, addr: int, memaddr: int, buf, *, addrsize: int = 8):
		'''
		将`buf`的数据写入由`addr`指定的外设，从`memaddr`指定的内存地址开始。

		参数`addrsize`指定地址大小（以位为单位）。（在 ESP8266 上，该参数不被识别，地址大小始终为 8 位）。

		该方法返回`None`。
		'''


class SoftI2C(object):
	'''
	双线串行协议

	I2C 是一种用于设备间通信的双线协议。

	在物理层面上，它由两根线组成：SCL 和 SDA 分别是时钟线和数据线。

	I2C 对象是根据特定总线创建的。它们可以在创建时初始化，也可以在创建后初始化。

	打印 I2C 对象可获得有关其配置的信息。

	软件 I2C 可通过`machine.SoftI2C`类实现。

	软件 I2C 通过 BitBanging 实现，可用于任何引脚，但效率较低。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.I2C.html)
	'''
	def __init__(self, scl, sda, *, freq: int = 400000, timeout: int = 50000):
		'''
		使用以下参数构造并返回一个软件 I2C 对象：

		- `scl`应是一个引脚对象，指定用于 SCL 的引脚。
		- `sda`应是一个引脚对象，指定用于 SDA 的引脚。
		- `freq`是一个整数，用于设置 SCL 的最大频率。
		- `timeout`是等待时钟拉伸（SCL 被总线上的其他设备保持为低电平）的最长时间（以微秒为单位）

			超过该时间将引发`OSError(ETIMEDOUT)`异常。
		'''

	# General Methods
	def init(self, scl, sda, *, freq=400000):
		'''
		使用给定参数初始化 I2C 总线：

		- `scl`是 SCL 线的引脚对象
		- `sda`是 SDA 线的引脚对象
		- `freq`是 SCL 时钟频率

		实际频率可通过打印 I2C 对象来确定。
		'''

	def deinit(self):
		'''
		关闭 I2C 总线。

		可用性：WiPy。
		'''

	def scan(self) -> list:
		'''
		扫描介于`0x08`和`0x77`之间的所有 I2C 地址，并返回有响应的设备列表。

		如果设备在总线上发送地址（包括写入位）后将 SDA 线拉至低电平，则该设备响应。
		'''

	# Primitive I2C operations.
	# These methods are only available on the `machine.SoftI2C` class.
	def start(self):
		'''在总线上产生一个启动条件（SDA 转换为低电平，同时 SCL 为高电平）。'''

	def stop(self):
		'''在总线上产生 STOP 条件（SCL 为高电平时 SDA 变为高电平）。'''

	def readinto(self, buf, nack: bool = True, /):
		'''
		从总线读取字节数据并存储到 `buf`。

		读取的字节数就是`buf`的长度。

		收到除最后一个字节外的所有字节后，总线上将发送一个 ACK。

		在接收到最后一个字节后，如果`nack`为`True`，则发送 NACK，否则发送 ACK
		（在这种情况下，外设假定将在以后的调用中读取更多字节）。
		'''

	def write(self, buf) -> int:
		'''
		将`buf`中的字节数据写入总线。

		检查每个字节后是否收到 ACK，如果收到 NACK，则停止传输剩余字节。

		函数将返回收到的 ACK 数量。
		'''

	# Standard bus operations
	def readfrom(self, addr: int, nbytes: int, stop: bool = True, /) -> bytes:
		'''
		从`addr`指定的外设中读取`nbytes`数据。

		如果`stop`为`True`，则在传输结束时产生一个 STOP 条件。

		返回包含读取数据的字节对象。
		'''

	def readfrom_into(self, addr: int, buf, stop: bool = True, /):
		'''
		从`addr`指定的外设读取数据到`buf`。

		读取的字节数为`buf`的长度。

		如果`stop`为`True`，则在传输结束时会生成一个 STOP 条件。

		该方法返回`None`。
		'''

	def writeto(self, addr: int, buf, stop: bool = True, /) -> int:
		'''
		将`buf`的数据写入由`addr`指定的外设。

		如果在从`buf`中写入字节后收到 NACK，则不会发送剩余字节。

		如果`stop`为`True`，即使收到 NACK，也会在传输结束时产生 STOP 条件。

		函数返回收到的 ACK 数量。
		'''

	def writevto(self, addr: int, vector: tuple | list, stop: bool = True, /) -> int:
		'''
		将`vector`中包含的字节写入`addr`指定的外设。

		`vector`应是一个具有缓冲协议的元组或对象列表。

		先发送一次`addr`，然后按顺序写出`vector`中每个对象的字节。

		在这种情况下，`vector`中的对象长度可能为零字节，它们不参与输出。

		如果从`vector`中的一个对象写入字节后收到 NACK，则不会发送剩余的字节和任何剩余的对象。

		如果`stop`为`True`，即使收到 NACK，也会在传输结束时产生 STOP 条件。

		函数返回收到的 ACK 数量。
		'''

	# Memory operations
	def readfrom_mem(self, addr: int, memaddr: int, nbytes: int, *, addrsize: int = 8) -> bytes:
		'''
		从`addr`指定的外设中读取`nbytes`数据，从`memaddr`指定的内存地址开始。

		参数`addrsize`指定地址大小（以位为单位）。

		返回包含读取数据的字节对象。
		'''

	def readfrom_mem_into(self, addr: int, memaddr: int, buf, *, addrsize=8):
		'''
		从`addr`指定的外设读取数据到`buf`，从`memaddr`指定的内存地址开始。

		读取的字节数是`buf`的长度。

		参数`addrsize`指定地址大小（以位为单位）。（在 ESP8266 上，该参数不被识别，地址大小始终为 8 位）。

		该方法返回`None`。
		'''

	def writeto_mem(self, addr: int, memaddr: int, buf, *, addrsize: int = 8):
		'''
		将`buf`的数据写入由`addr`指定的外设，从`memaddr`指定的内存地址开始。

		参数`addrsize`指定地址大小（以位为单位）。（在 ESP8266 上，该参数不被识别，地址大小始终为 8 位）。

		该方法返回`None`。
		'''


class I2S(object):
	'''
	Inter-IC 声音总线协议

	I2S 是一种同步串行协议，用于连接数字音频设备。

	在物理层面上，总线由 3 条线路组成：SCK、WS、SD。

	I2S 类支持控制器操作。不支持外设操作。

	I2S 类目前为技术预览版。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.I2S.html)
	'''
	# Constants
	RX: int = ...
	'''用于将 I2S 总线模式初始化为接收'''

	TX: int = ...
	'''用于将 I2S 总线模式初始化为发送'''

	STEREO: int = ...
	'''用于将 I2S 总线格式初始化为立体声格式'''

	MONO: int = ...
	'''用于将 I2S 总线格式初始化为单声道'''

	def __init__(self, id: int, *, sck, ws, sd, mck=None, mode, bits, format, rate, ibuf):
		'''
		根据给定的 ID 构建 I2S 对象：

		- `id`标识特定的 I2S 总线，它与开发板和端口相关

		所有端口都支持的关键字参数：

		- `sck`是串行时钟线的引脚对象
		- `ws`是字选择线路的引脚对象
		- `sd`是串行数据线的引脚对象
		- `mck`是主时钟线的引脚对象，主时钟频率为采样率 * 256
		- `mode`指定接收或发送
		- `bits`指定采样大小（位），16 或 32
		- `format`指定通道格式，立体声或单声道
		- `rate`指定音频采样率（赫兹），这是`ws`信号的频率
		- `ibuf`指定内部缓冲区长度（字节）
		'''

	# Methods
	def init(self, sck, *, kwargs):
		'''参数说明见构造函数。'''

	def deinit(self):
		'''取消 I2S 总线初始化。'''

	def readinto(self, buf) -> int:
		'''
		将音频采样数据读入`buf`指定的缓冲区。

		`buf`必须支持缓冲区协议，如字节数组或数组。

		`buf`字节排序为 little-endian。

		对于立体声格式，左声道采样先于右声道采样。

		对于单声道格式，则使用左声道采样数据。

		返回读取的字节数。
		'''

	def write(self, buf) -> int:
		'''
		写入包含在`buf`中的音频样本。

		`buf`必须支持缓冲协议，如字节数组或数组。

		`buf`字节排序为 little-endian。

		对于立体声格式，左声道采样先于右声道采样。

		对于单声道格式，采样数据同时写入左右声道。

		返回写入的字节数。
		'''

	def irq(self, handler: function):
		'''
		设置回调。

		当`buf`被清空（`write`方法）或变满（`readinto`方法）时，`handler`将被调用。

		设置回调会将`write`和`readinto`方法改为非阻塞操作。

		`handler`会在 MicroPython 调度器的上下文中调用。
		'''

	@staticmethod
	def shift(*, buf, bits: int, shift: int):
		'''
		对`buf`中的所有样本进行位移。

		`bits`指定样本大小（以位为单位）。

		`shift`指定对每个样本进行位移的位数。

		正数表示左移，负数表示右移，通常用于音量控制。

		每移动一位，采样音量就会改变 6dB。
		'''


class RTC(object):
	'''
	实时时钟

	实时时钟是一个独立的时钟，用于记录日期和时间。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.RTC.html)
	'''
	# Constants
	ALARM0: int = ...
	'''中断请求触发源'''

	def __init__(self, id: int = 0):
		'''创建 RTC 对象。'''

	@typing.overload
	def datetime(self):
		'''
		获取 RTC 的日期和时间。

		该方法返回一个包含当前日期和时间的 8 元组。

		8 元组的格式如下::

		    (year, month, day, weekday, hours, minutes, seconds, subseconds)

		`subseconds`字段的含义取决于硬件。
		'''

	# Methods
	@typing.overload
	def datetime(self, datetimetuple: tuple):
		'''
		设置 RTC 的日期和时间。

		通过参数（8 元组）设置日期和时间。

		8 元组格式如下::

		    (year, month, day, weekday, hours, minutes, seconds, subseconds)

		`subseconds`字段的含义取决于硬件。
		'''

	def init(self, datetime: tuple):
		'''
		初始化 RTC。

		`datetime`是一个元组，其形式为::

		    (year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
		'''

	def now(self) -> tuple:
		'''获取当前日期时间元组。'''

	def deinit(self):
		'''将 RTC 重置为 2015 年 1 月 1 日的时间，并重新开始运行。'''

	def alarm(self, id, time: int | tuple, *, repeat: bool = False):
		'''
		设置 RTC 闹钟。

		`time`可以是毫秒值（用于将闹钟设置为当前时间 + `time`），也可以是数据时间元组（datetimetuple）。

		如果传入的时间是毫秒值，则可将`repeat`设为`True`，使闹钟周期性响起。
		'''

	def alarm_left(self, alarm_id: int = 0) -> int:
		'''获取闹钟过期前剩余的毫秒数。'''

	def cancel(self, alarm_id: int = 0):
		'''取消正在运行的闹钟。'''

	def irq(self, *, trigger: int, handler: function = None, wake: int = IDLE):
		'''
		创建一个由实时时钟闹钟触发的 irq 对象。

		- `trigger`必须是`RTC.ALARM0`
		- `handler`是触发回调时要调用的函数
		- `wake`指定睡眠模式，该中断可从睡眠模式唤醒系统
		'''

	@typing.overload
	def memory(self) -> bytes:
		'''
		读取 RTC 内存并返回字节对象。

		RTC 用户内存的最大长度在 esp32 上默认为 2048 字节，在 esp8266 上默认为 492 字节。

		可用性：esp32、esp8266 端口。
		'''

	@typing.overload
	def memory(self, data):
		'''
		向 RTC 内存写入数据，其中`data`是任何支持缓冲协议的对象（包括`bytes`、`bytearray`、`memoryview`和`array.array`）。

		写入 RTC 用户内存的数据在重启（包括`machine.soft_reset()`和`machine.deepsleep()`）后会持续存在。

		RTC 用户内存的最大长度在 esp32 上默认为 2048 字节，在 esp8266 上默认为 492 字节。

		可用性：esp32、esp8266 端口。
		'''


class Timer(object):
	'''
	控制硬件计时器

	硬件定时器处理周期和事件的定时。

	定时器可能是 MCU 和 SoC 中最灵活、最异构的一种硬件，不同型号的定时器差别很大。

	MicroPython 的定时器类定义了在给定周期内执行回调（或在一定延迟后执行一次）的基本操作，
	并允许特定开发板定义更多非标准行为（因此无法移植到其他开发板）。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.Timer.html)
	'''
	# Constants
	# Timer operating mode.
	ONE_SHOT: int = ...
	PERIODIC: int = ...

	def __init__(self, id: int):
		'''
		根据给定的`id`构造一个新的计时器对象。

		`id`为-1时会构造一个虚拟定时器（如果开发板支持）。

		`id`不能作为关键字参数传递。

		初始化参数参见 `Timer.init`。
		'''

	# Methods
	def init(self, *, mode: int = PERIODIC, freq: int = -1, period: int = -1,
		callback: function=None):
		'''
		初始化计时器。

		关键字参数：

		- `mode`可以是以下其中之一：

			- `Timer.ONE_SHOT` - 定时器运行一次，直到通道配置的`period`过期。
			- `Timer.PERIODIC` - 定时器以通道的配置频率定期运行。

		- `freq` - 定时器频率（以赫兹为单位）

			频率上限取决于端口。

			当同时给出`freq`和`period`参数时，`freq`优先，`period`被忽略。

		- `period` - 定时器周期（以毫秒为单位）
		- `callback` - 定时器周期结束时调用的回调程序

			`callback`必须包含一个参数，该参数传递给定时器对象。

			必须指定`callback`参数，否则，定时器到期时将出现异常：
			`TypeError: 'NoneType' object isn't callable`
		'''

	def deinit(self):
		'''
		取消初始化定时器。

		停止定时器，并禁用定时器外设。
		'''


class WDT(object):
	'''
	看门狗定时器

	当应用程序崩溃并进入不可恢复的状态时，看门狗定时器用于重新启动系统。

	看门狗定时器一旦启动，就不能以任何方式停止或重新配置。

	启用后，应用程序必须定期“喂养”看门狗，以防止其过期并重置系统。

	该类的可用性：pyboard、WiPy、esp8266、esp32、rp2040、mimxrt。

	[查看文档](https://docs.micropython.org/en/latest/library/machine.WDT.html)
	'''
	def __init__(self, id: int = 0, timeout: int = 5000):
		'''
		创建 WDT 对象并启动它。

		`timeout`必须以毫秒为单位。

		一旦运行，`timeout`不可更改，WDT 也不可停止。

		注意：

			esp8266 无法指定超时时间，超时时间由底层系统决定。

			在 rp2040 设备上，最大超时为 8388 毫秒。
		'''

	# Methods
	def feed(self):
		'''
		投喂 WDT 以防止其重置系统。

		应用程序应将此调用放在合理的位置，确保只有在验证一切运行正常后才投喂 WDT。
		'''
