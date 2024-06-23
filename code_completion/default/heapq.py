'''
heap queue algorithm

This module implements a subset of the corresponding CPython module, as described
below.

For more information, refer to the original CPython documentation: heapq.

This module implements the min heap queue algorithm.

A heap queue is essentially a list that has its elements stored in such a way
that the first item of the list is always the smallest.

[View Doc](https://docs.micropython.org/en/latest/library/heapq.html)
'''
# Functions
def heappush(heap, item):
	'''Push the `item` onto the `heap`.'''

def heappop(heap):
	'''
	Pop the first item from the `heap`, and return it.

	Raise `IndexError` if `heap` is empty.

	The returned item will be the smallest item in the heap.
	'''

def heapify(x):
	'''
	Convert the list `x` into a heap.

	This is an in-place operation.
	'''
