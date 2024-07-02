'''
网络配置

该模块提供网络驱动程序和路由配置。

要使用该模块，必须安装具有网络功能的 MicroPython 变体/构建。

本模块提供特定硬件的网络驱动程序，用于配置硬件网络接口。

配置好的接口所提供的网络服务可通过 `socket` 模块使用。

[查看文档](https://docs.micropython.org/en/latest/library/network.html)
'''
import typing


# Constants
STA_IF: int = ...
AP_IF: int = ...

MODE_11B: int = ...
MODE_11G: int = ...
MODE_11N: int = ...
MODE_LR: int = ...

AUTH_OPEN: int = ...
AUTH_WEP: int = ...
AUTH_WPA_PSK: int = ...
AUTH_WPA2_PSK: int = ...
AUTH_WPA_WPA2_PSK: int = ...
AUTH_WPA2_ENTERPRISE: int = ...
AUTH_WPA3_PSK: int = ...
AUTH_WPA2_WPA3_PSK: int = ...
AUTH_WAPI_PSK: int = ...
AUTH_OWE: int = ...
AUTH_WPA3_ENT_192: int = ...
AUTH_MAX: int = ...

PHY_LAN8710: int = ...
PHY_LAN8720: int = ...
PHY_IP101: int = ...
PHY_RTL8201: int = ...
PHY_DP83848: int = ...
PHY_KSZ8041: int = ...
PHY_KSZ8081: int = ...
PHY_KSZ8851SNL: int = ...
PHY_DM9051: int = ...
PHY_W5500: int = ...

ETH_INITIALIZED: int = ...
ETH_STARTED: int = ...
ETH_STOPPED: int = ...
ETH_CONNECTED: int = ...
ETH_DISCONNECTED: int = ...
ETH_GOT_IP: int = ...

STAT_IDLE: int = ...
STAT_CONNECTING: int = ...
STAT_GOT_IP: int = ...
STAT_NO_AP_FOUND: int = ...
STAT_WRONG_PASSWORD: int = ...
STAT_BEACON_TIMEOUT: int = ...
STAT_ASSOC_FAIL: int = ...
STAT_HANDSHAKE_TIMEOUT: int = ...

# Network functions
@typing.overload
def country() -> str:
	'''
	获取用于无线电合规性的双字母 ISO 3166-1 Alpha-2 国家代码。

	此函数返回当前国家/地区。

	默认代码“XX”代表“全球”地区。
	'''

@typing.overload
def country(code: str):
	'''
	设置用于无线电合规的双字母 ISO 3166-1 Alpha-2 国家代码。

	国家将被设置为该`code`。

	默认代码“XX”代表“全球”地区。
	'''

@typing.overload
def hostname() -> str:
	'''
	获取在网络上标识此设备的主机名，所有接口都将使用该主机名。

	该主机名用于：

	- 在客户端请求中发送给 DHCP 服务器。(如果使用 DHCP）

	- 通过 mDNS 广播。(如果启用）

	此函数返回当前主机名。

	默认主机名通常是开发版名称。
	'''

@typing.overload
def hostname(name: str):
	'''
	设置在网络上标识此设备的主机名。

	所有接口都将使用该主机名。

	该主机名用于：

	- 在客户端请求中发送给 DHCP 服务器。(如果使用 DHCP）

	- 通过 mDNS 广播。(如果启用）

	主机名将设置为该`name`。

	主机名的更改通常只在连接过程中进行。

	对于 DHCP 而言，这是因为主机名是 DHCP 客户端请求的一部分，而大多数端口的
	mDNS 只在连接时初始化一次主机名。

	因此，必须在激活/连接网络接口前设置主机名。

	主机名的长度限制为 32 个字符。

	`MicroPython 端口`可能会出于内存原因设置更低的限制。

	如果给定的主机名不合适，系统将提示`ValueError`。

	默认主机名通常是开发板的名称。
	'''

@typing.overload
def phy_mode() -> int:
	'''
	获取 PHY 模式，该函数返回当前的 PHY 模式。

	可能的模式被定义为常量：

	- `MODE_11B` - IEEE 802.11b
	- `MODE_11G` - IEEE 802.11g
	- `MODE_11N` - IEEE 802.11n

	可用性： ESP8266。
	'''

@typing.overload
def phy_mode(mode: int):
	'''
	设置 PHY 模式，PHY 模式将设置为`mode`。

	可能的模式被定义为常量：

	- `MODE_11B` - IEEE 802.11b
	- `MODE_11G` - IEEE 802.11g
	- `MODE_11N` - IEEE 802.11n

	可用性： ESP8266。
	'''


class WLAN(object):
	'''
	控制内置 WiFi 接口

	该类为 WiFi 网络处理器提供驱动程序。

	[查看文档](https://docs.micropython.org/en/latest/library/network.WLAN.html)
	'''
	# Constants
	IF_STA: int = ...
	IF_AP: int = ...
	SEC_OPEN: int = ...
	SEC_WEP: int = ...
	SEC_WPA: int = ...
	SEC_WPA2: int = ...
	SEC_WPA_WPA2: int = ...
	SEC_WPA2_ENT: int = ...
	SEC_WPA3: int = ...
	SEC_WPA2_WPA3: int = ...
	SEC_WAPI: int = ...
	SEC_OWE: int = ...

	PM_PERFORMANCE: int = ...
	'''启用 WiFi 电源管理，在省电和 WiFi 性能之间取得平衡'''

	PM_POWERSAVE: int = ...
	'''启用 WiFi 电源管理，可节省更多电力并降低 WiFi 性能'''

	PM_NONE: int = ...
	'''禁用 WIFI 电源管理'''

	def __init__(self, interface_id: int):
		'''
		创建 WLAN 网络接口对象。

		支持的接口有：

		- `network.STA_IF`（站点，又称客户端，连接上游 WiFi 接入点 点）。
		- `network.AP_IF`（接入点，允许其它 WiFi 客户端连接）。

		以下方法的可用性取决于接口类型。

		例如，只有 STA 接口可以`WLAN.connect()`连接到接入点。
		'''

	# Methods
	@typing.overload
	def active(self) -> bool:
		'''查询当前状态。'''

	@typing.overload
	def active(self, is_active: bool):
		'''
		激活（"up"）或停用（"down"）网络接口。

		大多数其他方法需要激活接口。
		'''

	def connect(self, ssid: str = None, key: str = None, *, bssid: bytes = None):
		'''
		使用指定的密钥连接到指定的无线网络。

		如果给出了`bssid`，则连接将仅限于具有该 MAC 地址的接入点
		（在这种情况下必须指定`ssid`）。
		'''

	def disconnect(self):
		'''断开当前连接的无线网络。'''

	def scan(self):
		'''
		扫描可用的无线网络。

		如果 WLAN 接口允许，还将扫描隐藏的网络（SSID 没有广播）。

		扫描只能在 STA 接口上进行。

		返回包含 WiFi 接入点信息的元组列表：

			`(ssid, bssid, channel, RSSI, security, hidden)`

		`bssid`是接入点的二进制硬件地址，以字节对象形式返回。

		可以使用`binascii.hexlify()`将其转换为 ASCII 格式。

		`security`有五个值：

		- 0 - 开放
		- 1 - WEP
		- 2 - WPA-PSK
		- 3 - WPA2-PSK
		- 4 - WPA/WPA2-PSP

		和两个`hidden`选项：

		- 0 - 可见
		- 1 - 隐藏
		'''

	@typing.overload
	def status(self) -> int:
		'''
		返回值描述网络链接状态。

		可能的状态被定义为常量：

		- `STAT_IDLE` - 无连接、无活动
		- `STAT_CONNECTING` - 正在连接
		- `STAT_WRONG_PASSWORD` - 因密码错误而连接失败
		- `STAT_NO_AP_FOUND` - 因没有接入点回复而失败
		- `STAT_CONNECT_FAIL` - 因其他问题而失败
		- `STAT_GOT_IP` - 连接成功
		'''

	@typing.overload
	def status(self, param: str) -> int:
		'''
		返回无线连接的当前状态。

		可能的状态定义为常量：

		- `STAT_IDLE` - 无连接、无活动、
		- `STAT_CONNECTING` - 正在连接、
		- `STAT_WRONG_PASSWORD` - 因密码错误而连接失败、
		- `STAT_NO_AP_FOUND` - 因没有接入点回复而失败、
		- `STAT_CONNECT_FAIL` - 因其他问题而失败、
		- `STAT_GOT_IP` - 连接成功。

		应使用字符串命名要检索的状态参数。

		WiFI STA 模式下支持的参数有`rssi`。
		'''

	def isconnected(self) -> bool:
		'''
		在 STA 模式下，如果连接到 WiFi 接入点并具有有效 IP 地址，则返回`True`。

		在 AP 模式下，如果连接了一个站点，则返回`True`。

		其它情况下返回`False`。
		'''

	@typing.overload
	def ifconfig(self) -> tuple:
		'''
		获取 IP 级网络接口参数：IP 地址、子网掩码、网关和 DNS 服务器。

		该方法返回包含上述信息的 4 元组。
		'''

	@typing.overload
	def ifconfig(self, if_info: tuple):
		'''
		设置 IP 级网络接口参数：IP 地址、子网掩码、网关和 DNS 服务器。

		要设置上述值，请传递包含所需信息的 4 元组。

		例如::

		    nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
		'''

	@typing.overload
	def ipconfig(self) -> tuple:
		'''
		获取 IP 级网络接口参数：IP 地址、子网掩码、网关和 DNS 服务器。

		该方法返回包含上述信息的 4 元组。
		'''

	@typing.overload
	def ipconfig(self, ip_info: tuple):
		'''
		设置 IP 级网络接口参数：IP 地址、子网掩码、网关和 DNS 服务器。

		要设置上述值，请传递包含所需信息的 4 元组。

		例如::

		    nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
		'''

	@typing.overload
	def config(self, param: str) -> typing.Any:
		'''
		获取一般网络接口参数。

		这些方法允许处理标准 IP 配置（由`WLAN.ifconfig()`处理）之外的其他参数。

		这些参数包括网络特定参数和硬件特定参数。

		参数名应以字符串形式加引号，每次只能查询一个参数。

		以下是通常支持的参数（特定参数的可用性取决于网络技术类型、驱动程序和`MicroPython 端口`）。

		- `mac` - MAC 地址（字节）
		- `ssid` - WiFi 接入点名称（字符串）
		- `channel` - WiFi 频道（整数）
		- `hidden` - SSID 是否隐藏（布尔值）
		- `security` - 支持的安全协议（参见模块常量）
		- `key` - 访问密钥（字符串）
		- `hostname` - 发送给 DHCP（STA 接口）和 mDNS（如果支持，STA 和 AP）的主机名。

			(已过时，请使用`network.hostname()`代替）。

		- `reconnects` - 尝试重新连接的次数（整数，0=无，-1=无限制）
		- `txpower` - 以 dBm 为单位的最大发射功率（整数或浮点数）
		- `pm` - WiFi 电源管理设置（参见模块常量）
		'''

	@typing.overload
	def config(self, **params):
		'''
		设置一般网络接口参数。

		这些方法允许处理标准 IP 配置（由`WLAN.ifconfig()`处理）之外的其他参数。

		这些参数包括网络特定参数和硬件特定参数。

		应使用关键字参数语法，可同时设置多个参数。

		以下是通常支持的参数（特定参数的可用性取决于网络技术类型、驱动程序和`MicroPython 端口`）。

		- `mac` - MAC 地址（字节）
		- `ssid` - WiFi 接入点名称（字符串）
		- `channel` - WiFi 频道（整数）
		- `hidden` - SSID 是否隐藏（布尔值）
		- `security` - 支持的安全协议（参见模块常量）
		- `key` - 访问密钥（字符串）
		- `hostname` - 发送给 DHCP（STA 接口）和 mDNS（如果支持，STA 和 AP）的主机名。

			(已过时，请使用`network.hostname()`代替）。

		- `reconnects` - 尝试重新连接的次数（整数，0=无，-1=无限制）
		- `txpower` - 以 dBm 为单位的最大发射功率（整数或浮点数）
		- `pm` - WiFi 电源管理设置（参见模块常量）
		'''
