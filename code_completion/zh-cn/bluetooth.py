'''
该模块为开发板上的蓝牙控制器提供接口。

目前，它支持蓝牙低功耗（BLE）的中央、外设、广播和观察者等角色，以及 GATT
服务器和客户端以及面向连接的 L2CAP 通道。

一个设备可同时扮演多个角色。

某些端口支持配对和绑定。

该 API 旨在与底层蓝牙协议相匹配，并为更高层次的抽象（如特定设备类型）提供基石。

[查看文档](https://docs.micropython.org/en/latest/library/bluetooth.html)
'''
import typing


# Constants
FLAG_READ: int = ...
FLAG_WRITE: int = ...
FLAG_NOTIFY: int = ...
FLAG_INDICATE: int = ...
FLAG_WRITE_NO_RESPONSE: int = ...


class UUID(object):
	def __init__(self, value: int | str, /):
		'''
		用指定的`value`创建 UUID 实例。

		`value`可以是：

		- 16 位整数，如`0x2908`。
		- 128 位 UUID 字符串，如`'6E400001-B5A3-F393-E0A9-E50E24DCCA9E'`。
		'''


class BLE(object):
	'''返回 BLE 对象的单例。'''
	# Configuration
	@typing.overload
	def active(self) -> bool:
		'''
		返回 BLE 无线电设备当前的激活状态。

		在使用该类的其他方法之前，必须先使无线电处于激活状态。
		'''

	@typing.overload
	def active(self, active: bool, /) -> bool:
		'''
		更改 BLE 无线电设备的激活状态，并返回当前状态。

		在使用该类的其他方法之前，必须先使无线电处于激活状态。
		'''

	@typing.overload
	def config(self, param: str, /):
		'''
		获取 BLE 接口的配置值。

		要获取参数值，参数名应以字符串形式引述，每次只能查询一个参数。

		目前支持的参数值有：

		- `mac`：当前使用的地址，取决于当前的地址模式。

			返回一个元组`(addr_type, addr)`。

			只能在接口当前处于活动状态时查询。

		- `addr_mode`：获取地址模式。值可以是：

			- `0x00 - PUBLIC` - 使用控制器的公共地址
			- `0x01 - RANDOM` - 使用生成的静态地址
			- `0x02 - RPA` - 使用可解析的私有地址
			- `0x03 - NRPA` - 使用不可解析的专用地址

			默认情况下，如果可以的话接口模式将使用 PUBLIC 地址，否则将使用 RANDOM 地址。

		- `gap_name`：获取服务`0x1800`，特征`0x2a00`使用的 GAP 设备名称。

		- `rxbuf`：获取用于存储传入事件的内部缓冲区的大小（以字节为单位）。

			该缓冲区是整个 BLE 驱动程序的全局缓冲区，因此可以处理所有事件（包括所有`特征`）的传入数据。

		- `mtu`：获取 ATT MTU 交换时使用的 MTU。

			获得的 MTU 是该 MTU 和远程设备 MTU 的最小值。

			使用`_IRQ_MTU_EXCHANGED`事件发现给定连接的 MTU。
		'''

	@typing.overload
	def config(self, **params):
		'''
		设置 BLE 接口的配置值。

		要设置参数值，请使用关键字语法，一次可设置一个或多个参数。

		目前支持的参数值有：

		- `addr_mode`：设置地址模式。值可以是：

			- `0x00 - PUBLIC` - 使用控制器的公共地址
			- `0x01 - RANDOM` - 使用生成的静态地址
			- `0x02 - RPA` - 使用可解析的私有地址
			- `0x03 - NRPA` - 使用不可解析的专用地址

			默认情况下，如果可以的话接口模式将使用 PUBLIC 地址，否则将使用 RANDOM 地址。

		- `gap_name`：获取服务`0x1800`，特征`0x2a00`使用的 GAP 设备名称。

			可随时设置并多次更改。

		- `rxbuf`：设置用于存储传入事件的内部缓冲区的大小（以字节为单位）。

			该缓冲区是整个 BLE 驱动程序的全局缓冲区，因此可以处理所有事件（包括所有`特征`）的传入数据。

			增大缓冲区大小可以更好地处理突发传入数据（例如扫描结果），并能接收更大的`特征`值。

		- `mtu`：设置 ATT MTU 交换时使用的 MTU。

			ATT MTU 不会自动进行交换（除非远程设备启动），必须使用`gattc_exchange_mtu()`手动启动。

			使用`_IRQ_MTU_EXCHANGED`事件可发现给定连接的 MTU。

		- `bond`：设置配对时是否启用绑定。

			启用后，配对请求将设置“绑定标志，并且密钥将被两个设备存储。

		- `mitm`：设置配对是否需要 MITM 保护。

		- `io`：设置设备的输入输出功能。可用选项有::

		    _IO CAPABILITY DISPLAY ONLY = const(0)
		    _IO_CAPABILITY_DISPLAY_YESNO = const(1)
		    _IO_CAPABILITY_KEYBOARD_ONLY = const(2)
		    _IO_CAPABILITY_NO_INPUT_OUTPUT = const(3)
		    _IO_CAPABILITY_KEYBOARD_DISPLAY = const(4)

		- `le_secure`：设置是否需要`LE Secure`配对。

			默认为`False`（即允许“传统配对”）。
		'''

	# Event Handling
	def irq(self, handler: function, /):
		'''
		为来自 BLE 堆栈的事件注册回调函数。

		`handler`函数需要两个参数，`event`和`data`（这是一个特定于事件的数值元组）。

		详见 [说明文档](https://docs.micropython.org/en/latest/library/bluetooth.html#bluetooth.BLE.irq)。
		'''

	# Broadcaster Role (Advertiser)
	def gap_advertise(self, interval_us: int, adv_data=None, *, resp_data=None,
		connectable: bool = True):
		'''
		以指定的时间间隔（微秒）开始广播。

		该间隔将向下舍入到最接近的 625 微秒。

		要停止广播，请将`interval_us`设为`None`。

		`adv_data`和`resp_data`可以是任何实现缓冲协议的类型（如`bytes`、`bytearray`、`str`）。

		`adv_data`包含在所有广播中，而`resp_data`则在主动扫描的回复中发送。

		注意：

			如果`adv_data`（或`resp_data`）为`None`，则会重复使用上次调用`gap_advertise`时传递的数据。

			这样，广播者只需使用`gap_advertise(interval_us)`，就能继续广播。

			要清除广播有效载荷，请输入一个空字节，即`b''`。
		'''

	# Observer Role (Scanner)
	def gap_scan(self, duration_ms: int, interval_us: int = 1280000,
		window_us: int = 11250, active: bool = False, /):
		'''
		运行扫描操作，持续指定的时间（以毫秒为单位）。

		要无限期扫描，请将`duration_ms`设置为`0`。

		要停止扫描，请将`duration_ms`设置为`None`。

		使用`interval_us`和`window_us`可选择配置占空比。

		扫描将每隔`interval_us`微秒运行`window_us`微秒，总共运行`duration_ms`毫秒。

		默认时间间隔和窗口分别为 1.28 秒和 11.25 毫秒（后台扫描）。

		每次扫描结果都会引发`_IRQ_SCAN_RESULT`事件，事件数据为::

		    (addr_type, addr, adv_type, rssi, adv_data)

		- `addr_type`值表示公共地址或随机地址：

			- `0x00 - PUBLIC`
			- `0x01 - RANDOM`（静态、RPA 或 NRPA，类型在地址本身中编码）

		- `adv_type`值与蓝牙规范相对应：

			- `0x00 - ADV_IND` - 可连接和可扫描的非定向广告
			- `0x01 - ADV_DIRECT_IND` - 可连接的定向广告
			- `0x02 - ADV_SCAN_IND` - 可扫描的非定向广告
			- `0x03 - ADV_NONCONN_IND` - 不可连接的非定向广告
			- `0x04 - SCAN_RSP` - 扫描响应

		如果希望在结果中接收扫描响应，可将`active`设置为`True`。

		扫描停止时（由于持续时间结束或显式停止），将引发`_IRQ_SCAN_DONE`事件。
		'''

	# Central Role
	def gap_connect(self, addr_type: int, addr: bytes, scan_duration_ms: int = 2000,
		min_conn_interval_us: int | None = None, max_conn_interval_us: int | None = None, /):
		'''
		连接外设。

		要提前取消未完成的连接尝试，请调用`gap_connect(None)`。

		成功后将引发`_IRQ_PERIPHERAL_CONNECT`事件。

		如果取消连接尝试，则会引发`_IRQ_PERIPHERAL_DISCONNECT`事件。

		设备将最多等待`scan_duration_ms`毫秒接收来自设备的广播有效载荷。

		可以使用`min_conn_interval_us`和`max_conn_interval_us`配置连接间隔（以微秒为单位）。

		否则将选择默认的时间间隔，通常在 30000 至 50000 微秒之间。

		较短的时间间隔会提高吞吐量，但会增加功耗。
		'''

	# Central & Peripheral Roles
	def gap_disconnect(self, conn_handle: int, /):
		'''
		断开指定的连接句柄。

		该句柄可以是已连接到该设备的中心设备（如果作为外设），也可以是之前连接到该设备的外设（如果作为中心设备）。

		成功后将触发`_IRQ_PERIPHERAL_DISCONNECT`或`_IRQ_CENTRAL_DISCONNECT`事件。

		如果连接句柄未连接，则返回`False`，否则返回`True`。
		'''

	# GATT Server
	def gatts_register_services(self, services_definition: tuple, /) -> tuple:
		'''
		用指定的`服务`配置服务器，替换任何现有`服务`。

		`services_definition`是一个`服务`列表，其中每个`服务`都是一个包含 UUID 和`特征`列表的双元素元组。

		每个`特征`都是一个包含 UUID、`标志`值和可选的`描述符`列表的二或三元素元组。

		每个`描述符`都是包含一个 UUID 和一个`标志`值的双元素元组。

		`标志`是标志常量的位或组合。

		这些`标志`设定了`特征`（或`描述符`）的行为以及安全和隐私要求。

		返回值是一个包含列表（每个`服务`一个元素）的元组（每个元素是一个值句柄）。

		`特征`和`描述符`句柄会按照定义的顺序平铺到同一个元组中。
		'''

	def gatts_read(self, value_handle: int, /):
		'''读取此句柄的本地值（该值由`gatts_write`或远程客户端写入）。'''

	def gatts_write(self, value_handle: int, data, send_update: bool = False, /):
		'''
		写入此句柄的本地值，客户端可以读取此值。

		如果`send_update`为`True`，则任何已订阅的客户端都会收到关于此次写入的通知
		（或指示，取决于他们订阅的内容和`特征`支持的操作）。
		'''

	def gatts_notify(self, conn_handle: int, value_handle: int, data: bytes = None, /):
		'''
		向已连接的客户端发送通知请求。

		如果`data`为`None`（默认值），则会发送当前的本地值（通过`gatts_write`设置）。

		否则，如果`data`不是`None`，那么该值将作为通知的一部分发送给客户端。

		本地值不会被修改。

		注意：

			无论客户端对该`特征`的订阅状态如何，都将发送通知。
		'''

	def gatts_indicate(self, conn_handle: int, value_handle: int, data: bytes = None, /):
		'''
		向已连接的客户端发送指示请求。

		如果`data`为`None`（默认值），则会发送当前的本地值（通过`gatts_write`设置）。

		否则，如果`data`不是`None`，那么该值将作为指示的一部分发送给客户端。

		本地值不会被修改。

		确认（或失败，例如超时）时，将触发`_IRQ_GATTS_INDICATE_DONE`事件。

		注意：

			无论客户端对该`特征`的订阅状态如何，都将发送指示。
		'''

	def gatts_set_buffer(self, value_handle: int, len: int, append: bool = False, /):
		'''
		设置值的内部缓冲区大小（以字节为单位）。

		这将限制可接收的最大写入量，默认值为 20。

		将`append`设置为`True`，所有远程写入都将追加到当前值，而不是替换当前值。
		'''

	# GATT Client
	def gattc_discover_services(self, conn_handle: int, uuid: UUID = None, /):
		'''
		查询已连接服务器的`服务`。

		可选择指定一个服务`uuid`，以便只查询该`服务`。

		对于发现的每个`服务`，都会引发`_IRQ_GATTC_SERVICE_RESULT`事件，并在完成后引发`_IRQ_GATTC_SERVICE_DONE`事件。
		'''

	def gattc_discover_characteristics(self, conn_handle: int, start_handle: int,
		end_handle: int, uuid: UUID = None, /):
		'''
		查询指定范围内已连接服务器的`特征`。

		可选择指定一个特征`uuid`，以便只查询该`特征`。

		可以使用`start_handle=1`，`end_handle=0xffff`搜索任何`服务`中的`特征`。

		每发现一个`特征`，就会引发`_IRQ_GATTC_CHARACTERISTIC_RESULT`事件，完成后会引发`_IRQ_GATTC_CHARACTERISTIC_DONE`事件。
		'''

	def gattc_discover_descriptors(self, conn_handle: int, start_handle: int,
		end_handle: int, /):
		'''
		在指定范围内查询已连接服务器的`描述符`。

		每发现一个`描述符`，就会触发`_IRQ_GATTC_DESCRIPTOR_RESULT`事件，完成后触发`_IRQ_GATTC_DESCRIPTOR_DONE`事件。
		'''

	def gattc_read(self, conn_handle: int, value_handle: int, /):
		'''
		针对指定的`特征`或`描述符`句柄，向已连接的服务器发出远程读取命令。

		当值可用时，将触发`_IRQ_GATTC_READ_RESULT`事件。

		此外，还将引发`_IRQ_GATTC_READ_DONE`事件。
		'''

	def gattc_write(self, conn_handle: int, value_handle: int, data: bytes, mode: int = 0, /):
		'''
		针对指定的`特征`或`描述符`句柄向已连接的服务器发出远程写入命令。

		参数`mode`指定写入行为，目前支持的值有：

		- `mode=0`（默认）是无响应写入

			将向远程服务器发送写入信息，但不会返回确认信息，也不会引发任何事件。

		- `mode=1`为带响应写入

			要求远程服务器发送收到数据的响应/确认。

		如果收到了远程服务器的响应，就会触发`_IRQ_GATTC_WRITE_DONE`事件。
		'''

	def gattc_exchange_mtu(self, conn_handle: int, /):
		'''
		使用`BLE.config(mtu=value)`设置首选 MTU，与已连接的服务器启动 MTU 交换。

		MTU 交换完成后，`_IRQ_MTU_EXCHANGED`事件将被触发。

		注意：

			MTU 交换通常由中心设备启动。

			在中心设备中使用 BlueKitchen 堆栈时，它不支持由远程外设启动 MTU 交换。

			NimBLE 同时适用于这两种角色。
		'''

	# L2CAP connection-oriented-channels
	def l2cap_listen(self, psm, mtu: int, /):
		'''
		开始在指定的`psm`上监听传入的 L2CAP 信道请求，并将本地 MTU 设为`mtu`。

		当远程设备发起连接时，`_IRQ_L2CAP_ACCEPT`事件将被触发，这将给监听服务器一个拒绝传入连接的机会（通过返回一个非零整数）。

		一旦连接被接受，就会触发`_IRQ_L2CAP_CONNECT`事件，使服务器能够获取通道 ID（CID）以及本地和远程 MTU。

		注意：

			目前无法停止监听。
		'''

	def l2cap_connect(self, conn_handle: int, psm, mtu: int, /):
		'''
		连接到指定`psm`上的监听节点设备，并将本地 MTU 设为`mtu`。

		连接成功后，将触发`_IRQ_L2CAP_CONNECT`事件，允许客户端获取 CID 以及本地和远程（节点）MTU。

		连接不成功时，将引发状态非零的`_IRQ_L2CAP_DISCONNECT`事件。
		'''

	def l2cap_disconnect(self, conn_handle: int, cid: int, /):
		'''使用指定的`conn_handle`和`cid`断开活动的 L2CAP 信道。'''

	def l2cap_send(self, conn_handle: int, cid: int, buf, /) -> bool:
		'''
		在由`conn_handle`和`cid`标识出的 L2CAP 信道上发送指定的`buf`（必须支持缓冲协议）。

		指定的缓冲区不能大于远程（节点）MTU，也不能超过本地 MTU 的两倍。

		如果通道现在处于“停滞”状态，则返回`False`，这意味着在收到`_IRQ_L2CAP_SEND_READY`事件
		（通常是在远程设备接收并处理完数据后授予更多信用点时）之前，不得再次调用`l2cap_send`。
		'''

	def l2cap_recvinto(self, conn_handle: int, cid: int, buf, /) -> int:
		'''
		从指定的`conn_handle`和`cid`接收数据到提供的`buf`中（必须支持缓冲协议，如`bytearray`或`memoryview`）。

		返回从通道读取的字节数。

		如果`buf`为`None`，则返回可用字节数。

		注意：

			接收到`_IRQ_L2CAP_RECV`事件后，应用程序应继续调用`l2cap_recvinto`，直到接收缓冲区中没有可用字节
			（通常达到远程（节点）MTU 的大小）。

		在接收缓冲区清空之前，远程设备不会获得更多信道点数，也无法发送更多数据。
		'''

	# Pairing and bonding
	def gap_pair(self, conn_handle: int, /):
		'''
		启动与远程设备的配对。

		调用前，请确保已通过`config`设置了`io`、`mitm`、`le_secure`和`bond`配置选项。

		配对成功后，将触发`_IRQ_ENCRYPTION_UPDATE`事件。
		'''

	def gap_passkey(self, conn_handle: int, action: int, passkey: int, /):
		'''
		响应指定的`conn_handle`和`action`的`_IRQ_PASSKEY_ACTION`事件。

		`passkey`是一个数值，取决于`action`（取决于已设置的 I/O 功能）：

		- 当`action`为`_PASSKEY_ACTION_INPUT`时，应用程序应提示用户输入远程设备上显示的`passkey`。

		- 当`action`为`_PASSKEY_ACTION_DISPLAY`时，应用程序将随机生成一个 6 位数的密码并显示给用户。

		- 当`action`为`_PASSKEY_ACTION_NUMERIC_COMPARISON`时，应用程序应显示在`_IRQ_PASSKEY_ACTION`
		事件中提供的密码，然后以`0`（取消配对）或`1`（接受配对）作为响应。
		'''
