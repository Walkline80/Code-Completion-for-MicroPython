'''
堆队列算法

此模块实现相应`CPython`模块的子集，如下所述。

有关详细信息，请参阅原始`CPython`文档：[heapq](https://docs.python.org/3.5/library/heapq.html#module-heapq)。

此模块实现最小堆队列算法。

堆队列本质上是一个列表，其元素的存储方式使列表的第一项始终是最小的。

[查看文档](https://docs.micropython.org/en/latest/library/heapq.html)
'''
# Functions
def heappush(heap, item):
	'''将`item`推到`heap`上。'''

def heappop(heap):
	'''
	从`heap`中弹出第一项并返回它。

	如果`heap`为空，则引发`IndexError`。

	返回的项将是堆中最小的项。
	'''

def heapify(x):
	'''将列表`x`转换为堆。这是就地操作。'''
