'''
自定义按键驱动

[View button.py](https://gitee.com/walkline/micropython-drivers/blob/master/button.py)
'''
class ButtonException(BaseException):
	...


class Button(object):
	'''
	自定义按键驱动
	
	支持点击和长按两种模式，按键电路适配默认高电平或低电平

	长按模式分为：
	    - 1. 长按超时触发
	    - 2. 长按超时松开触发
	
	参数：
	    - pin: GPIO 引脚，可使用列表或元组批量添加
	    - hold_cb: 按键按下回调函数
	    - release_cb: 按键释放回调函数
	    - click_cb: 单击事件回调函数
	    - press_cb: 长按事件回调函数
	    - timeout: 长按触发超时时间（ms）
	    - default: 按键未按下时状态，高电平或低电平
	    - behavior: 长按触发模式选择
	'''

	DEFAULT_LOW = ...
	'''low when button not pressed'''

	DEFAULT_HIGH = ...
	'''high when button not pressed'''

	BEHAVIOR_HOLD = ...
	'''trigger long press while holding button'''

	BEHAVIOR_RELEASE = ...
	'''trigger long press after release button'''

	def __init__(self, pin: int | list | tuple, hold_cb: callable = None, release_cb: callable = None,
			click_cb: callable = None, press_cb: callable = None, timeout: int = 3000, default: int = DEFAULT_HIGH,
			behavior: int = BEHAVIOR_HOLD, timer_id: int | None = 0):
		'''初始化 Button 实例'''

	def deinit(self):
		...

	def add_button(self, pin: int):
		...

	def __time_diff(self, index: int):
		...

	def timer_callback(self, timer=None):
		...

	@property
	def timeout(self) -> int:
		...

	@timeout.setter
	def timeout(self, value: int):
		...
