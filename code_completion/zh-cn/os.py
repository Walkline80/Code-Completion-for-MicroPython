'''
基本“操作系统”服务

此模块实现相应`CPython`模块的子集，如下所述。

有关详细信息，请参阅原始`CPython`文档：[os](https://docs.python.org/3.5/library/os.html#module-os)。

`os`模块包含文件系统访问和挂载、终端重定向和复制以及`uname`和`urandom`函数。

[查看文档](https://docs.micropython.org/en/latest/library/os.html)
'''
import typing


# General functions
def uname() -> tuple:
	'''
	返回一个元组（可能是命名元组），其中包含有关基础计算机和/或其操作系统的信息。

	元组有五个字段，顺序如下，每个字段都是一个字符串：

	- `sysname` – 底层系统的名称
	- `nodename` – 网络名称（可以与`sysname`相同）
	- `release` – 底层系统的版本
	- `version` – MicroPython 版本和编译日期
	- `machine` – 底层硬件（例如主板、CPU）的标识符
	'''

def urandom(n: int) -> bytes:
	'''
	返回一个包含`n`个随机字节的 bytes 对象。

	只要有可能，它由硬件随机数生成器生成。
	'''

# Filesystem access
def chdir(path: str):
	'''更改当前目录。'''

def getcwd() -> str:
	'''获取当前目录。'''

@typing.overload
def ilistdir():
	'''
	此函数返回一个迭代器，然后生成与它列出的当前目录中的条目相对应的元组。

	元组的形式为`(name, type, inode[, size])`：

	- `name`是一个字符串（如果`dir`是 bytes 对象，则为 bytes），是条目的名称;

	- `type`是一个整数，用于指定条目的类型，其中 0x4000 表示目录，0x8000 表示常规文件;

	- `inode`是对应于文件的索引节点的整数，对于没有这种概念的文件系统，它可能是 0。

	- 某些平台可能会返回包含条目大小为 4 的元组。

		对于文件条目，`size`是一个整数，表示文件的大小，如果未知，则为 -1。

		对于目录条目，其含义目前尚未定义。
	'''

@typing.overload
def ilistdir(dir: str):
	'''
	此函数返回一个迭代器，然后生成与它列出的目录中的条目相对应的元组。

	它列出了`dir`给出的目录。

	元组的形式为`(name, type, inode[, size])`：

	- `name`是一个字符串（如果`dir`是 bytes 对象，则为 bytes），是条目的名称;

	- `type`是一个整数，用于指定条目的类型，其中 0x4000 表示目录，0x8000 表示常规文件;

	- `inode`是对应于文件节点的整数，对于没有这种概念的文件系统，它可能是 0。

	- 某些平台可能会返回包含条目大小为 4 的元组。

		对于文件条目，`size`是一个整数，表示文件的大小，如果未知，则为 -1。

		对于目录条目，其含义目前尚未定义。
	'''

@typing.overload
def listdir():
	'''列出当前目录。'''

@typing.overload
def listdir(dir: str):
	'''列出给定的目录。'''

def mkdir(path: str):
	'''创建一个新目录。'''

def remove(path: str):
	'''删除文件。'''

def rmdir(path: str):
	'''删除目录。'''

def rename(old_path: str, new_path: str):
	'''重命名文件。'''

def stat(path: str):
	'''获取文件或目录的状态。'''

def statvfs(path: str) -> tuple:
	'''
	获取文件系统的状态。

	按以下顺序返回包含文件系统信息的元组：

	- `f_bsize` – 文件系统块大小
	- `f_frsize` – 片段大小
	- `f_blocks` – 文件系统大小（以`f_frsize`为单位）
	- `f_bfree` – 可用区块数
	- `f_bavail` – 非特权用户的可用块数
	- `f_files` – 节点数
	- `f_ffree` – 可用节点数
	- `f_favail` – 非特权用户的可用节点数量
	- `f_flag` – 挂载标志位
	- `f_namemax` – 最大文件名长度

	与节点相关的参数：`f_files`、`f_ffree`、`f_avail`和`f_flags`可能返回 0，因为它们在特定于端口的实现中可能不可用。
	'''

def sync():
	'''同步所有文件系统。'''

# Terminal redirection and duplication
def dupterm(stream_object, index: int = 0, /):
	'''
	在给定的类似流的对象上复制或切换 MicroPython 终端（REPL）。

	`stream_object`参数必须是原生流对象，或者派生自`io.IOBase`并实现了`readinto()`和`write()`方法。

	流应处于非阻塞模式，如果没有可供读取的数据，则`readinto()`应返回`None`。

	调用此函数后，在此流上重复所有终端输出，并且流上可用的任何输入都将传递到终端输入。

	`index`参数应为非负整数，并指定设置的复制插槽。

	给定端口可以实现多个插槽（插槽 0 将始终可用），在这种情况下，终端输入和输出在设置的所有插槽上复制。

	如果`None`作为`stream_object`传递，则取消在`index`给出的插槽上的复制。

	该函数返回给定插槽中的上一个类似流的对象。
	'''

# Filesystem mounting
# The following functions and classes have been moved to the vfs module.
# They are provided in this module only for backwards compatibility and will be
# removed in version 2 of MicroPython.
def mount(fsobj, mount_point, *, readonly):
	'''请参阅`vfs.mount`。'''

def umount(mount_point):
	'''请参阅`vfs.umount`。'''


class VfsFat(object):
	'''请参阅`vfs.VfsFat`。'''
	def __init__(self, block_dev): ...


class VfsLfs1(object):
	'''请参阅`vfs.VfsLfs1`。'''

	def __init__(self, block_dev, readsize=32, progsize=32, lookahead=32): ...


class VfsLfs2(object):
	'''请参阅`vfs.VfsLfs2`。'''
	def __init__(self, block_dev, readsize=32, progsize=32, lookahead=32, mtime=True): ...


class VfsPosix(object):
	'''请参阅`vfs.VfsPosix`。'''
	def __init__(self, root=None): ...
