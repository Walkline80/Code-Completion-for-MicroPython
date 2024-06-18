'''
Specific network class implementations

The following concrete classes implement the AbstractNIC interface and provide a way to control networking interfaces of various kinds.

- class WLAN – control built-in WiFi interfaces
'''
# Docs:
#	https://docs.micropython.org/en/latest/library/network.html
#	https://docs.micropython.org/en/latest/library/network.WLAN.html

# Constants
STA_IF = ...
AP_IF = ...

MODE_11B = ...
MODE_11G = ...
MODE_11N = ...
MODE_LR = ...

AUTH_OPEN = ...
AUTH_WEP = ...
AUTH_WPA_PSK = ...
AUTH_WPA2_PSK = ...
AUTH_WPA_WPA2_PSK = ...
AUTH_WPA2_ENTERPRISE = ...
AUTH_WPA3_PSK = ...
AUTH_WPA2_WPA3_PSK = ...
AUTH_WAPI_PSK = ...
AUTH_OWE = ...
AUTH_WPA3_ENT_192 = ...
AUTH_MAX = ...

PHY_LAN8710 = ...
PHY_LAN8720 = ...
PHY_IP101 = ...
PHY_RTL8201 = ...
PHY_DP83848 = ...
PHY_KSZ8041 = ...
PHY_KSZ8081 = ...
PHY_KSZ8851SNL = ...
PHY_DM9051 = ...
PHY_W5500 = ...

ETH_INITIALIZED = ...
ETH_STARTED = ...
ETH_STOPPED = ...
ETH_CONNECTED = ...
ETH_DISCONNECTED = ...
ETH_GOT_IP = ...

STAT_IDLE = ...
STAT_CONNECTING = ...
STAT_GOT_IP = ...
STAT_NO_AP_FOUND = ...
STAT_WRONG_PASSWORD = ...
STAT_BEACON_TIMEOUT = ...
STAT_ASSOC_FAIL = ...
STAT_HANDSHAKE_TIMEOUT = ...

# Network functions
def country(code: str | None):
	'''
	Get or set the two-letter ISO 3166-1 Alpha-2 country code to be used for radio compliance.

	If the `code` parameter is provided, the country will be set to this value.

	If the function is called without parameters, it returns the current country.

	The default code "XX" represents the "worldwide" region.
	'''

def hostname(name: str | None):
	'''
	Get or set the hostname that will identify this device on the network. It will be used by all interfaces.

	This hostname is used for:

	- Sending to the DHCP server in the client request. (If using DHCP)
	- Broadcasting via mDNS. (If enabled)

	If the `name` parameter is provided, the hostname will be set to this value.

	If the function is called without parameters, it returns the current hostname.

	A change in hostname is typically only applied during connection.

	For DHCP this is because the hostname is part of the DHCP client request, and the implementation of mDNS in most ports only initialises the hostname once during connection.

	For this reason, you must set the hostname before activating/connecting your network interfaces.

	The length of the hostname is limited to 32 characters.

	MicroPython ports may choose to set a lower limit for memory reasons.

	If the given name does not fit, a `ValueError` is raised.

	The default hostname is typically the name of the board.
	'''

def phy_mode(mode: int | None):
	'''
	Get or set the PHY mode.

	If the `mode` parameter is provided, the PHY mode will be set to this value.

	If the function is called without parameters, it returns the current PHY mode.

	The possible modes are defined as constants:

	- `MODE_11B` – IEEE 802.11b,
	- `MODE_11G` – IEEE 802.11g,
	- `MODE_11N` – IEEE 802.11n.

	Availability: ESP8266.
	'''


class WLAN(object):
	'''
	control built-in WiFi interfaces

	This class provides a driver for WiFi network processors.
	'''
	# Constants
	IF_STA = ...
	IF_AP = ...
	SEC_OPEN = ...
	SEC_WEP = ...
	SEC_WPA = ...
	SEC_WPA2 = ...
	SEC_WPA_WPA2 = ...
	SEC_WPA2_ENT = ...
	SEC_WPA3 = ...
	SEC_WPA2_WPA3 = ...
	SEC_WAPI = ...
	SEC_OWE = ...

	'''
	Allowed values for the `WLAN.config(pm=...)` network interface parameter:

	- PM_PERFORMANCE: enable WiFi power management to balance power savings and WiFi performance
	- PM_POWERSAVE: enable WiFi power management with additional power savings and reduced WiFi performance
	- PM_NONE: disable wifi power management
	'''
	PM_PERFORMANCE = ...
	PM_POWERSAVE = ...
	PM_NONE = ...

	def __init__(self, interface_id: int):
		'''
		Create a WLAN network interface object.

		Supported interfaces are:

		- `network.STA_IF` (station aka client, connects to upstream WiFi access points)
		- `network.AP_IF` (access point, allows other WiFi clients to connect).

		Availability of the methods below depends on interface type.

		For example, only STA interface may `WLAN.connect()` to an access point.
		'''

	# Methods
	def active(self, is_active: bool | None):
		'''
		Activate ("up") or deactivate ("down") network interface, if boolean argument is passed.

		Otherwise, query current state if no argument is provided.

		Most other methods require active interface.
		'''

	def connect(self, ssid: str = None, key: str = None, *, bssid: bytes = None):
		'''
		Connect to the specified wireless network, using the specified key.

		If `bssid` is given then the connection will be restricted to the access-point with that MAC address

		the `ssid` must also be specified in this case.
		'''

	def disconnect(self):
		'''Disconnect from the currently connected wireless network.'''

	def scan(self):
		'''
		Scan for the available wireless networks.

		Hidden networks – where the SSID is not broadcast – will also be scanned if the WLAN interface allows it.

		Scanning is only possible on STA interface.

		Returns list of tuples with the information about WiFi access points:

			(ssid, bssid, channel, RSSI, security, hidden)

		`bssid` is hardware address of an access point, in binary form, returned as bytes object.

		You can use `binascii.hexlify()` to convert it to ASCII form.

		There are five values for `security`:

		- 0 – open
		- 1 – WEP
		- 2 – WPA-PSK
		- 3 – WPA2-PSK
		- 4 – WPA/WPA2-PSK

		and two for `hidden`:

		- 0 – visible
		- 1 – hidden
		'''

	def status(self, param: str | None) -> int:
		'''
		Return the current status of the wireless connection.

		When called with no argument the return value describes the network link status.

		The possible statuses are defined as constants:

		- STAT_IDLE – no connection and no activity,
		- STAT_CONNECTING – connecting in progress,
		- STAT_WRONG_PASSWORD – failed due to incorrect password,
		- STAT_NO_AP_FOUND – failed because no access point replied,
		- STAT_CONNECT_FAIL – failed due to other problems,
		- STAT_GOT_IP – connection successful.

		When called with one argument param should be a string naming the status parameter to retrieve.

		Supported parameters in WiFI STA mode are: `'rssi'`.
		'''

	def isconnected(self):
		'''
		In case of STA mode, returns True if connected to a WiFi access point and has a valid IP address.

		In AP mode returns True when a station is connected.

		Returns False otherwise.
		'''

	def ifconfig(if_info: tuple | None):
		'''
		Get/set IP-level network interface parameters: IP address, subnet mask, gateway and DNS server.

		When called with no arguments, this method returns a 4-tuple with the above information.

		To set the above values, pass a 4-tuple with the required information.

		For example:

			nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
		'''

	def ipconfig(ip_info: tuple | None):
		'''
		Get/set IP-level network interface parameters: IP address, subnet mask, gateway and DNS server.

		When called with no arguments, this method returns a 4-tuple with the above information.

		To set the above values, pass a 4-tuple with the required information.

		For example:

			nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
		'''

	def config(param: str):
		'''
		config(param=value, ...)

		Get or set general network interface parameters.

		These methods allow to work with additional parameters beyond standard IP configuration (as dealt with by `WLAN.ifconfig()`).

		These include network-specific and hardware-specific parameters.

		For setting parameters, keyword argument syntax should be used, multiple parameters can be set at once.

		For querying, parameters name should be quoted as a string, and only one parameter can be queries at time.

		Following are commonly supported parameters (availability of a specific parameter depends on network technology type, driver, and MicroPython port).

		- mac - MAC address (bytes)
		- ssid - WiFi access point name (string)
		- channel - WiFi channel (integer)
		- hidden - Whether SSID is hidden (boolean)
		- security - Security protocol supported (see module constants)
		- key - Access key (string)
		- hostname - The hostname that will be sent to DHCP (STA interfaces) and mDNS (if supported, both STA and AP).

			(Deprecated, use `network.hostname()` instead)

		- reconnects - Number of reconnect attempts to make (integer, 0=none, -1=unlimited)
		- txpower - Maximum transmit power in dBm (integer or float)
		- pm - WiFi Power Management setting (see module constants)
		'''
