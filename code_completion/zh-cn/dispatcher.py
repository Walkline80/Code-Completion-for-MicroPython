'''
MicroPython 定时器调度管理器，可以使用一个定时器管理多个需要定时运行的任务，以节省有限的定时器资源

[View Doc](https://gitee.com/walkline/micropython-timer-dispatcher)
'''
class Worker(object):
	'''定时器任务'''
	def __init__(self, work: callable, period: int, *params): ...

	@property
	def counter(self): ...
	
	@counter.setter
	def counter(self, count): ...

	@property
	def period(self): ...

	def do_work(self): ...


class Dispatcher(object):
	'''定时器任务调度器'''
	__DEFAULT_PERIOD: int = ...

	def __init__(self, timer_id: int = 0): ...

	def deinit(self): ...

	def __worker_callback(self, _): ...

	def add_work(self, work: callable, period: int, *params) -> bool:
		'''
		添加一个调度任务，参数如下：
		- work：任务函数
		- period：任务执行间隔，单位 毫秒
		- params：任务函数参数列表
		'''

	def has_work(self, work: callable) -> bool:
		'''
		判断任务是否在队列中，参数如下：
		- work：任务函数
		'''

	def del_work(self, work: callable = None):
		'''
		删除指定或最后添加的任务，参数如下：
		- work：任务函数，默认值 None
		'''

	def del_works(self):
		'''删除所有任务'''

	def pause(self):
		'''暂停/开启 所有任务'''
	
	def is_paused(self):
		'''判断所有任务是否正在运行'''
