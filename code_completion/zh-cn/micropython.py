'''
访问和控制 MicroPython 内部

[查看文档](https://docs.micropython.org/en/latest/library/micropython.html)
'''
import typing


# Functions
def const(expr: int):
	'''
	用于声明表达式是一个常量，以便编译器可以对其进行优化。

	此函数的使用方法应如下::

	    from micropython import const

	    CONST_X = const(123)
	    CONST_Y = const(2 * CONST_X + 1)

	以这种方式声明的常量仍然可以作为全局变量从声明它们的模块外部访问。

	另一方面，如果一个常量以下划线开头，那么它是隐藏的，它不能作为全局变量使用，并且在执行
	过程中不会占用任何内存。

	这个`const`函数由 MicroPython 解析器直接识别，并作为`micropython`模块的一部分
	提供，主要是为了可以按照上述模式编写在 CPython 和 MicroPython 下运行的脚本。
	'''

@typing.overload
def opt_level() -> int:
	'''返回当前优化级别。'''

@typing.overload
def opt_level(level: int = 0):
	'''
	此函数设置后续脚本编译的优化级别，并返回`None`。

	优化级别控制以下编译功能：

	- 断言：在级别 0 上，断言语句被启用并编译为字节码；在级别 1 及更高级别，不会编译断言。
	- 内置`__debug__`变量：在级别 0 时，此变量扩展为`True`；在级别 1 及更高时，它会扩展为`False`。
	- 源代码行号：在级别 0、1 和 2 中，源代码行号与字节码一起存储，以便异常可以报告它们出现的行号；在级别 3 及更高级别，不存储行号。

	默认优化级别通常为 0 级。
	'''

def alloc_emergency_exception_buf(size: int):
	'''
	为紧急异常缓冲区分配 RAM 的字节大小（100 字节最为合适）。

	缓冲区用于在正常 RAM 分配失败的情况下（例如在中断处理程序中）创建异常，因此在这些情况下提供有用的回溯信息。

	使用此函数的一个好方法是将其放在主脚本的开头（例如`boot.py`或`main.py`），然后紧急异常缓冲区将对它后面的所有代码处于活动状态。
	'''

@typing.overload
def mem_info():
	'''
	打印有关当前使用的内存的信息。

	打印的信息与端口实现相关，但当前包括使用的堆栈数量。
	'''

@typing.overload
def mem_info(verbose: typing.Any):
	'''
	打印有关当前使用的内存的信息。

	打印的信息与端口实现相关，它会打印出整个堆，指示哪些块被使用，哪些块是空闲的。
	'''

@typing.overload
def qstr_info():
	'''
	打印有关当前被截留的字符串的信息。

	打印的信息与端口实现相关，但目前包括中介字符串的数量和它们 RAM 的使用量。
	'''

@typing.overload
def qstr_info(verbose):
	'''
	打印有关当前被截留的字符串的额外信息。

	打印的信息与端口实现相关，它会打印出所有 RAM 中嵌的字符串的名称。
	'''

def stack_use() -> int:
	'''
	返回一个整数，表示当前已使用的栈的数量。

	它的绝对值不是特别有用，而是应该用于计算不同的点对栈使用的差异。
	'''

def heap_lock():
	'''
	锁定堆。

	锁定时，不会发生内存分配，如果尝试分配堆，将引发`MemoryError`。

	这个函数可以嵌套，即`heap_lock()`可以连续调用多次，锁定深度会增加，然后`heap_unlock()`必须调用相同的次数才能使堆再次可用。
	'''

def heap_unlock() -> int:
	'''
	解锁堆。

	`heap_unlock()`以非负整数的形式返回当前锁定深度（前者解锁后），0 表示堆未锁定。

	如果 REPL 在堆锁定的情况下处于活动状态，则它将被强制解锁。
	'''

def heap_locked() -> bool:
	'''
	如果堆当前处于锁定状态，则返回`True`值。

	如果 REPL 在堆锁定的情况下处于活动状态，则它将被强制解锁。

	注意：

		默认情况下，`heap_locked()`在大多数端口上不可用，需要开启`MICROPY_PY_MICROPYTHON_HEAP_LOCKED`编译选项。
	'''

def kbd_intr(chr: int = 3):
	'''
	设置将引发`KeyboardInterrupt`异常的特性。

	默认情况下，在脚本执行期间将其设置为 3，对应于 Ctrl-C。

	将 -1 传递给此函数将禁用 Ctrl-C 捕获，传递 3 将恢复它。

	此函数可用于防止在通常用于 REPL 的传入字符流上捕获 Ctrl-C，以防该流用于其他目的。
	'''

def schedule(func: function, arg):
	'''
	将函数`func`安排为“很快”执行。

	该函数将`arg`作为其单个参数传递。

	“很快”意味着 MicroPython 运行时将尽最大努力尽早执行该函数，因为它也在努力提高效率，并且满足以下条件：

	- 一个调度函数永远不会抢占另一个调度函数。

	- 调度函数始终在“操作码之间”执行，这意味着所有基本的 Python 操作（例如附加到列表）都保证是原子级别的。

	- 给定的端口可以定义“关键区域”，在这些区域内永远不会执行计划功能。

		函数可以在关键区域内调度，但在退出该区域之前不会执行。

		关键区域的一个示例是抢占中断处理程序（IRQ）。

	此函数的用途是调度来自抢占式 IRQ 的回调。

	这样的 IRQ 对在 IRQ 中运行的代码施加了限制（例如，堆可能被锁定），并且安排稍后调用的函数将解除这些限制。

	注意：

		如果从抢占式 IRQ 调用`schedule()`，则当不允许分配内存并且要传递给`schedule()`的回调是绑定方法时，直接传递此方法将失败。

		这是因为创建对绑定方法的引用会导致内存分配。

		解决方法是在类构造函数中创建对方法的引用，并将该引用传递给`schedule()`。

	有一个有限的队列来保存调度函数，如果队列已满，`schedule()`将引发`RuntimeError`。
	'''
