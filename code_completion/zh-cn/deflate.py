'''
Deflate 压缩和解压缩

该模块允许使用`DEFLATE算法`对二进制数据进行压缩和解压缩（通常在 zlib 库和 gzip
压缩工具中使用）。

可用性：

- 在 MicroPython v1.21 中添加。

- 解压缩：通过`MICROPY_PY_DEFLATE`编译选项启用，默认情况下在具有`额外功能`级别
或更高级别的端口上启用（这适用于大多数开发板）。

- 压缩：通过`MICROPY_PY_DEFLATE_COMPRESS`编译选项启用，默认情况下在具有`完整功能`
级别或更高级别的端口上启用（通常需要自行编译固件以启用此功能）。

[查看文档](https://docs.micropython.org/en/latest/library/deflate.html)
'''
# Constants
# Supported values for the format parameter.
AUTO: int = ...
RAW: int = ...
ZLIB: int = ...
GZIP: int = ...


class DeflateIO(object):
	def __init__(self, stream, format: int = AUTO, wbits: int = 0, close: bool = False, /):
		'''
		此类可用于包装任何`类似流`对象的流，例如文件、套接字或流（包括`io.BytesIO`）。

		它本身是一个流，实现了标准的 read/readinto/write/close 方法。

		- `stream`必须是阻塞流。目前不支持非阻塞流。

		- `format`可以设置为任何定义的常量，默认为`AUTO`，解压缩时会自动检测 gzip 或
		zlib 流，压缩时会生成原始流。

		- `wbits`参数设置 DEFLATE 字典窗口大小的 2 进制对数。

			例如，将`wbits`设置为`10`会将窗口大小设置为 1024 字节。

			有效值为`5`到`15`（对应 32 到 32k 字节的窗口大小）。

		如果`wbits`设置为`0`（默认值），则将使用 256 字节的窗口大小进行压缩（就像`wbits`
		设置为 8 一样）。

		对于解压缩，这取决于`format`格式：

		- `RAW`将使用 256 个字节（对应于`wbits`设置为 8）。

		- `ZLIB`（或检测到 zlib 的`AUTO`）将使用 zlib 标头中的值。

		- `GZIP`（或检测到 gzip 的`AUTO`）将使用 32k（对应于设置为 15 的`wbits`）。

		如果`close`设置为`True`，则在关闭`deflate.DeflateIO`流时，底层流将自动关闭。

		如果您想要返回一个包装另一个流的`deflateDeflateIO`流，而不需要调用者知道如何管理底
		层流，这将非常有用。

		如果启用了压缩，给定的`deflateDeflateIO`实例支持读取和写入。

		例如，可以包装双向流（如套接字），从而允许在两个方向上进行压缩/解压缩。
		'''
