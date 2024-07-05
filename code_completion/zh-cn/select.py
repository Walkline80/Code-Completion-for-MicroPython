'''
等待一组流上的事件

此模块实现了相应`CPython`模块的子集，如下所述。

更多信息，请参阅`CPython`文档原文：[select](https://docs.python.org/3.5/library/select.html#module-select)。

该模块提供了在多个流上高效等待事件的函数（选择已准备好进行操作的流）。

[查看文档](https://docs.micropython.org/en/latest/library/select.html)
'''
# Constants
POLLIN: int = ...
POLLOUT: int = ...
POLLERR: int = ...
POLLHUP: int = ...


class Poll(object):
	# Methods
	def register(self, obj, eventmask: int = POLLIN | POLLOUT):
		'''
		为轮询注册`stream obj`。

		`eventmask`是以下各项的逻辑或值：

		- `select.POLLIN` - 可读取数据
		- `select.POLLOUT` - 可写入更多数据

		请注意，`select.POLLHUP`和`select.POLLERR`等标志不能作为输入事件掩码
		（这些是非请求事件，无论是否请求，都会从`poll()`返回）。

		这种语义符合 POSIX 标准。

		`eventmask`默认为`select.POLLIN | select.POLLOUT`。

		对同一个`obj`可以多次调用此函数。

		连续调用会将`obj`的事件掩码更新为`eventmask`的值（即行为类似于`modify()`）。
		'''

	def unregister(self, obj):
		'''从轮询中取消注册`obj`。'''

	def modify(self, obj, eventmask: int):
		'''
		修改`obj`的`eventmask`。

		如果`obj`未注册，则会引发`OSError: ENOENT`错误。
		'''

	def poll(self, timeout: int = -1, /) -> tuple:
		'''
		等待至少一个注册对象准备就绪或出现异常情况，可选超时（以毫秒为单位）

		如果未指定`timeout`参数或`timeout`参数为 -1，则无超时。

		返回`(obj, event, …)`元组列表。

		元组中可能还有其他元素，这取决于平台和版本，因此不要认为其大小为 2。

		`event`元素指定流中发生的事件，是上述`select.POLL*`常量的组合。

		请注意，`select.POLLHUP`和`select.POLLERR`这两个标志可以随时返回
		（即使没有被要求返回），而且必须采取相应的措施（从轮询中取消注册相应的流，
		并可能关闭），否则，所有对`poll()`的进一步调用都可能立即返回并再次为该流设置这些标志。

		如果超时，则返回空列表。
		'''

	def ipoll(self, timeout: int = -1, flags: int = 0, /):
		'''
		类似于`poll.poll()`，但返回的是一个迭代器，该迭代器产生一个`callee-owned tuple`。

		该函数提供了一种高效、免分配的流轮询方式。

		如果`flags`为 1，则会对事件采用一次性行为：

			发生事件的流将自动重置其事件掩码（相当于`poll.modify(obj, 0)`），
			因此在使用`poll.modify()`设置新掩码之前，不会处理该流的新事件。

		这种行为对异步 I/O 调度器非常有用。

		与 CPython 的区别：

			此函数是 MicroPython 扩展。
		'''


# Functions
def poll() -> Poll:
	'''创建 Poll 类的实例。'''

def select(rlist, wlist, xlist, timeout=None):
	'''
	等待一组对象的活动。

	一些 MicroPython 端口提供此函数是为了兼容，但效率不高。

	建议使用`Poll`代替。
	'''
