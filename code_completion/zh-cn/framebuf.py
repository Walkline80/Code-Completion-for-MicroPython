'''
帧缓冲区操作

该模块提供了一个通用帧缓冲区，可用于创建位图图像，然后可以将其发送到显示设备。

[查看文档](https://docs.micropython.org/en/latest/library/framebuf.html)
'''
import typing


class FrameBuffer(object):
	'''
	FrameBuffer 类提供了一个像素缓冲区，可以使用像素、线条、矩形、椭圆、多边形、文本甚至其他
	FrameBuffer 进行绘制。

	在生成显示设备输出时，它很有用。
	'''
	# Constants
	# Monochrome (1-bit) color format. 
	MONO_VLSB: int = ...
	MONO_HLSB: int = ...
	MONO_HMSB: int = ...

	RGB565: int = ...
	'''红绿蓝（16 位，5+6+5）颜色格式'''

	GS2_HMSB: int = ...
	'''灰度（2 位）颜色格式'''

	GS4_HMSB: int = ...
	'''灰度（4 位）颜色格式'''

	GS8: int = ...
	'''灰度（8 位）颜色格式'''

	def __init__(self, buffer, width: int, height: int, format: int, stride: int, /):
		'''
		构造 FrameBuffer 对象。参数包括：

		- `buffer`是具有缓冲区协议的对象，该缓冲区必须足够大，以包含由 FrameBuffer 的宽度、高度和格式定义的每个像素。

		- `width`是 FrameBuffer 的宽度（以像素为单位）

		- `height`是 FrameBuffer 的高度（以像素为单位）

		- `format`指定 FrameBuffer 中使用的像素类型

			允许的值列在常量中。

			它们设置用于对颜色值进行编码的位数以及这些位在缓冲区中的布局。

			如果将颜色值 c 传递给方法，则 c 是一个小整数，其编码依赖于 FrameBuffer 的格式。

		- `stride`是 FrameBuffer 中每条水平像素线之间的像素数。

			默认值为`width`，但在另一个较大的 FrameBuffer 或屏幕中实现 FrameBuffer 时可能需要调整。

			缓冲区大小必须适应增加的步长。

		必须指定有效的`buffer`、`width`、`height`、`format`和可选的`stride`。

		无效的缓冲区大小或尺寸可能会导致意外错误。
		'''

	# Drawing primitive shapes
	def fill(self, c):
		'''用指定的颜色填充整个 FrameBuffer。'''

	@typing.overload
	def pixel(self, x: int, y: int):
		'''获取指定像素的颜色值。'''

	@typing.overload
	def pixel(self, x: int, y: int, c):
		'''将指定的像素设置为给定的颜色。'''

	def hline(self, x: int, y: int, w: int, c):
		'''
		使用给定的颜色和 1 像素的厚度从一组坐标中绘制一条线。

		`hline()`方法绘制给定长度的水平线。
		'''

	def vline(self, x: int, y: int, h: int, c):
		'''
		使用给定的颜色和 1 像素的厚度从一组坐标中绘制一条线。

		`vline()`方法绘制给定长度的垂直线。
		'''

	def line(self, x1: int, y1: int, x2: int, y2: int, c):
		'''
		使用给定的颜色和 1 像素的厚度从一组坐标中绘制一条线。

		`line()`方法将线绘制到第二组坐标。
		'''

	def rect(self, x: int, y: int, w: int, h: int, c, f: bool = False):
		'''
		以给定的位置、大小和颜色绘制一个矩形。

		可选参数`f`可以设置为`True`以填充矩形。

		否则，只会绘制一个像素轮廓。
		'''

	def ellipse(self, x: int, y: int, xr: int, yr: int, c, f: bool = False, m=None):
		'''
		在给定位置绘制一个椭圆。

		半径`xr`和`yr`定义几何图形，如果值相等则绘制一个圆形。

		`c`参数定义颜色。

		可选参数`f`可以设置为`True`以填充椭圆。

		否则，只会绘制一个像素轮廓。

		可选参数`m`允许将绘图限制在椭圆的某些象限内。

		LS 四位确定要绘制的象限，位 0 指定 Q1、位 1 指定 Q2、位 2 指定 Q3 以及位 3 指定 Q4。

		象限按逆时针方向编号，Q1 位于右上方。
		'''

	def poly(self, x: int, y: int, coords, c, f: bool = False):
		'''
		给定坐标列表，使用给定颜色在给定的 x、y 位置绘制任意（凸或凹）闭合多边形。

		`coords`必须指定为整数`array`，例如`array('h', [x0, y0, x1, y1, ...xn, yn])`。

		可选参数`f`可以设置为`True`以填充多边形。

		否则，只会绘制一个像素轮廓。
		'''

	# Drawing text
	def text(self, s: str, x: int, y: int, c=None):
		'''
		使用坐标作为文本的左上角将文本写入 FrameBuffer。

		文本的颜色可以由可选参数定义，但否则为默认值 1。

		所有字符的尺寸均为 8x8 像素，目前无法更改字体。
		'''

	# Other methods
	def scroll(self, xstep: int, ystep: int):
		'''
		按给定向量移动 FrameBuffer 的内容。

		这可能会在 FrameBuffer 中留下以前颜色的占用空间。
		'''

	def blit(self, fbuf, x: int, y: int, key: int = -1, palette=None):
		'''
		在给定坐标处的当前 FrameBuffer 之上绘制另一个 FrameBuffer。

		如果指定了`key`，则它应该是一个颜色整数，相应的颜色将被视为透明的：不会绘制具有该颜色值的所有像素。

		如果指定了`palette`，则将`key`与`palette`中的值进行比较，而不是直接与`fbuf`中的值进行比较。

		`palette`参数允许在具有不同格式的 FrameBuffer 之间进行位图复制。

		典型用法是将单色或灰度字形/图标渲染到彩色显示设备上。

		`palette`是一个 FrameBuffer 实例，其格式是当前 FrameBuffer 的格式。

		`palette`高度为一个像素，其像素宽度为源 FrameBuffer 中的颜色数。

		N 位源的`palette`需要 2**N 像素； 单色源的`palette`将有 2 个像素，分别代表背景色和前景色。

		应用程序为`palette`中的每个像素分配一种颜色。

		当前像素的颜色将是`palette`像素的颜色，其`x`位置是相应源像素的颜色。
		'''
