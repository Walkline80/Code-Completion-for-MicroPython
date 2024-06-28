'''
控制垃圾回收

此模块实现相应`CPython`模块的子集，如下所述。

有关更多信息，请参阅原始`CPython`文档：[gc](https://docs.python.org/3.5/library/gc.html#module-gc)。

[查看文档](https://docs.micropython.org/en/latest/library/gc.html)
'''
import typing


# Functions
def enable():
	'''启用自动垃圾回收。'''

def disable():
	'''
	禁用自动垃圾回收。

	仍然可以分配堆内存，并且仍然可以使用`gc.collect()`手动启动垃圾回收。
	'''

def collect():
	'''运行垃圾回收。'''

def mem_alloc():
	'''
	返回 Python 代码分配的堆 RAM 的字节数。

	与 CPython 的区别：

		此函数是 MicroPython 扩展。
	'''

def mem_free():
	'''
	返回可供 Python 代码分配的堆 RAM 的字节数，如果此数量未知，则返回`-1`。

	与 CPython 的区别：

		此函数是 MicroPython 扩展。
	'''

@typing.overload
def threshold() -> int:
	'''
	查询额外的 GC 分配阈值。

	函数返回阈值的当前值，`-1`表示禁用了分配阈值。
	'''

@typing.overload
def threshold(amount: int = None):
	'''
	设置额外的 GC 分配阈值。

	通常，只有在无法满足新的分配时，即出现内存不足（OOM）的情况下，才会触发
	垃圾回收。

	如果调用这个函数，除了 OOM 之外，每次分配`amount`字节（总的来说，因为
	上次分配了这么多字节）后，都会触发一次垃圾回收。

	`amount`通常被指定为小于整个堆的大小的值，目的是在堆耗尽之前更早地触发
	垃圾回收，并希望早期的回收能够防止过多的内存碎片。

	这是一种启发式的措施，其效果会因应用程序而异，以及`amount`参数的最佳值。
	'''
