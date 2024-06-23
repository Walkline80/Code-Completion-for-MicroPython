'''
配合小程序使用的 BLE 配网客户端

[View Doc](https://gitee.com/walkline/micropython_ble_config)
'''
class BLEConfig(object):
	'''BLEConfig 客户端'''
	def __init__(self, rx_received_cb: function = None):
		'''初始化 BLEConfig 客户端'''

	def success(self) -> bool:
		'''获取配网完成状态'''
