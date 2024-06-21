'''
MicroPython QRCode CModule

生成并显示指定内容的二维码

[View Doc](https://gitee.com/walkline/micropython-qrcode-cmodule/blob/master/DOCS.md)
'''
# Constants
ECC_LOW = ...
'''7% 容错率'''

ECC_MED = ...
'''15% 容错率'''

ECC_QUART = ...
'''25% 容错率'''

ECC_HIGH = ...
'''30% 容错率'''

VERSION_MIN = ...
'''二维码支持的最低版本：1'''

VERSION_MAX = ...
'''二维码支持的最高版本：40'''

FORMAT_MONO_HLSB = ...
'''指定 `buffer_data()` 函数填充数组的方式，适用于 OLED 屏幕'''

FORMAT_RGB565 = ...
'''指定 `buffer_data()` 函数填充数组的方式，适用于 TFT 屏幕'''


class QRCODE(object):
	'''构建QRCODE对象实例。'''
	def __init__(self, ecc_level=ECC_MED, max_version=VERSION_MAX):
		'''
		- `ecc_level` - 容错等级，默认值 ECC_MED
		- `max_version` - 可生成二维码的最大版本号，默认值 VERSION_MAX
		'''

	# Methods
	def ecc_level(self, level=None):
		'''获取或设置容错等级'''

	def version(self):
		'''获取已生成二维码的版本号'''

	def length(self):
		'''获取已生成二维码的边长'''

	def generate(self, text: str):
		'''使用指定字符串生成二维码'''

	def print(self):
		'''在控制台打印二维码预览图'''

	def raw_data(self):
		'''获取二维码点阵元组数据'''

	def buffer_data(self, byetarray, format: int, scales: int = 1, color: int = 1, bg_color: int = 0):
		'''
		将二维码数据以指定格式填充到数组，其中：

		- `bytearray` - 已初始化大小的 byetarray 数组
		- `format` - 数据格式
		- `scales` - 放大倍数，默认值 1
		- `color` - 前景颜色，默认值 1 或 0xffff
		- `bg_color` - 背景颜色，默认值 0 或 0x0000
		'''
