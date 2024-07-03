'''
简单 BTree 数据库

`btree`模块使用外部存储（磁盘文件或一般情况下的随机访问流）实现了一个简单的键值数据库。

键在数据库中排序存储，除了按键的值高效检索外，数据库还支持高效的有序范围扫描（检索指定范围内的键和值）。

在应用程序接口方面，BTree 数据库的工作方式与标准`dict`类型的工作方式尽可能接近，一个显著的区别是键和值都必须是类字节对象
（因此，如果要存储其他类型的对象，需要先将其序列化为`str`或`bytes`或其他支持缓冲协议的类型）。

该模块基于著名的 BerkelyDB 库 1.xx 版本。

[查看文档](https://docs.micropython.org/en/latest/library/btree.html)
'''
# Constants
INCL: int = ...
'''`keys()`、`values()`、`items()`方法的标志，用于指定扫描应包括末端键。'''
DESC: int = ...
'''`keys()`、`values()`、`items()`方法的标志，用于指定扫描应按键的递减方向进行。'''

# Functions
def open(stream, *, flags: int = 0, pagesize: int = 0, cachesize: int = 0, minkeypage: int = 0):
	'''
	从随机访问的`stream`（类似于打开的文件）中打开数据库。

	所有其他参数都是可选的关键字参数，允许调整数据库操作的高级参数（大多数用户不需要它们）：

	- `flags` - 当前未使用。

	- `pagesize` - BTree 中节点使用的页面大小。

		可接受的范围是 512-65536。

		如果为 0，将使用特定于端口的默认值，并根据端口的内存使用情况和/或性能进行优化。

	- `cachesize` - 推荐的内存缓存大小（以字节为单位）。

		对于有足够内存的开发板，使用较大的值可能会提高性能。

		缓存策略如下：整个缓存不会一次性分配；相反，访问数据库中的新页面将为其分配一个内存缓冲区，直到达到`cachesize`指定的值。

		然后，这些缓冲区将使用 LRU（最近最少使用）策略进行管理。

		如果需要，还可以分配更多缓冲区（例如，如果数据库包含较大的键和/或值）。

		分配的缓冲区不会被回收。

	- `minkeypage` - 每页存储的最小键数。默认值 0 相当于 2。

	返回一个 BTree 对象，该对象实现了字典协议（一组方法）和一些附加方法。
	'''

# Methods
def close():
	'''
	关闭数据库。

	处理结束时必须关闭数据库，因为缓存中可能仍有一些未写入的数据。

	请注意，这并不会关闭数据库打开时使用的底层数据流，它应该单独关闭（这也是确保数据从缓冲区刷新到底层存储的必要条件）。
	'''

def flush():
	'''将缓存中的任何数据刷新到底层数据流中。'''

def __getitem__(key):
	'''标准字典方法。'''

def get(key, default=None, /):
	'''标准字典方法。'''

def __setitem__(key, val):
	'''标准字典方法。'''

def __delitem__(key):
	'''标准字典方法。'''

def __contains__(key):
	'''标准字典方法。'''

def __iter__():
	'''BTree 对象可以直接遍历（类似于字典），以便按顺序访问所有键。'''

def keys(start_key=None, end_key=None, flags=None):
	'''
	该方法与标准字典方法类似，但也可以使用可选参数遍历键的子范围，而不是整个数据库。

	请注意，`start_key`和`end_key`参数代表键。

	例如，`values()`方法将遍历所给键范围对应的值。

	`start_key`的值为`None`表示“从第一个键开始”，没有`end_key`或其值为`None`表示
	“直到数据库结束”。

	默认情况下，范围包含`start_key`但不包含`end_key`，可以通过给`flags`传递`btree.INCL`常量以便在迭代中包含`end_key`。

	通过给`flags`传入`btree.DESC`常量，可以按键的递减方向迭代。

	这些标志值可以被`or`连接在一起使用。
	'''

def values(start_key=None, end_key=None, flags=None):
	'''
	该方法与标准字典方法类似，但也可以使用可选参数遍历键的子范围，而不是整个数据库。

	请注意，`start_key`和`end_key`参数代表键。

	例如，`values()`方法将遍历所给键范围对应的值。

	`start_key`的值为`None`表示“从第一个键开始”，没有`end_key`或其值为`None`表示
	“直到数据库结束”。

	默认情况下，范围包含`start_key`但不包含`end_key`，可以通过给`flags`传递`btree.INCL`常量以便在迭代中包含`end_key`。

	通过给`flags`传入`btree.DESC`常量，可以按键的递减方向迭代。

	这些标志值可以被`or`连接在一起使用。
	'''

def items(start_key=None, end_key=None, flags=None):
	'''
	该方法与标准字典方法类似，但也可以使用可选参数遍历键的子范围，而不是整个数据库。

	请注意，`start_key`和`end_key`参数代表键。

	例如，`values()`方法将遍历所给键范围对应的值。

	`start_key`的值为`None`表示“从第一个键开始”，没有`end_key`或其值为`None`表示
	“直到数据库结束”。

	默认情况下，范围包含`start_key`但不包含`end_key`，可以通过给`flags`传递`btree.INCL`常量以便在迭代中包含`end_key`。

	通过给`flags`传入`btree.DESC`常量，可以按键的递减方向迭代。

	这些标志值可以被`or`连接在一起使用。
	'''
