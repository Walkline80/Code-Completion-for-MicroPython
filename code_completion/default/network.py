'''
Specific network class implementations

The following concrete classes implement the AbstractNIC interface and provide a way to control networking interfaces of various kinds.

- class WLAN – control built-in WiFi interfaces

[View Doc network](https://docs.micropython.org/en/latest/library/network.html)
[View Doc network.WLAN](https://docs.micropython.org/en/latest/library/network.WLAN.html)
'''
from typing import overload


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
@overload
def country() -> str:
	'''
	Get the two-letter ISO 3166-1 Alpha-2 country code to be used for radio
	compliance.

	This function returns the current country.

	The default code "XX" represents the "worldwide" region.
	'''

@overload
def country(code: str):
	'''
	Set the two-letter ISO 3166-1 Alpha-2 country code to be used for radio
	compliance.

	The country will be set to this `code`.

	The default code "XX" represents the "worldwide" region.
	'''

@overload
def hostname():
	'''
	Get the hostname that will identify this device on the network.

	It will be used by all interfaces.

	This hostname is used for:

	- Sending to the DHCP server in the client request. (If using DHCP)
	- Broadcasting via mDNS. (If enabled)

	This function returns the current hostname.

	The default hostname is typically the name of the board.
	'''

@overload
def hostname(name: str):
	'''
	Set the hostname that will identify this device on the network.

	It will be used by all interfaces.

	This hostname is used for:

	- Sending to the DHCP server in the client request. (If using DHCP)
	- Broadcasting via mDNS. (If enabled)

	The hostname will be set to this `name`.

	A change in hostname is typically only applied during connection.

	For DHCP this is because the hostname is part of the DHCP client request,
	and the implementation of mDNS in most ports only initialises the hostname
	once during connection.

	For this reason, you must set the hostname before activating/connecting your
	network interfaces.

	The length of the hostname is limited to 32 characters.

	MicroPython ports may choose to set a lower limit for memory reasons.

	If the given name does not fit, a `ValueError` is raised.

	The default hostname is typically the name of the board.
	'''

@overload
def phy_mode():
	'''
	Get the PHY mode.

	This function returns the current PHY mode.

	The possible modes are defined as constants:

	- `MODE_11B` – IEEE 802.11b,
	- `MODE_11G` – IEEE 802.11g,
	- `MODE_11N` – IEEE 802.11n.

	Availability: ESP8266.
	'''

@overload
def phy_mode(mode: int):
	'''
	Set the PHY mode.

	The PHY mode will be set to this `mode`.

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
	'''
	enable WiFi power management to balance power savings and WiFi performance
	'''

	PM_POWERSAVE: int = ...
	'''
	enable WiFi power management with additional power savings and reduced WiFi
	performance
	'''

	PM_NONE: int = ...
	'''disable wifi power management'''

	def __init__(self, interface_id: int):
		'''
		Create a WLAN network interface object.

		Supported interfaces are:

		- `network.STA_IF` (station aka client, connects to upstream WiFi access
		points)
		- `network.AP_IF` (access point, allows other WiFi clients to connect).

		Availability of the methods below depends on interface type.

		For example, only STA interface may `WLAN.connect()` to an access point.
		'''

	# Methods
	@overload
	def active(self):
		'''Query current state if no argument is provided.'''

	@overload
	def active(self, is_active: bool):
		'''
		Activate ("up") or deactivate ("down") network interface, if boolean
		argument is passed.

		Most other methods require active interface.
		'''

	def connect(self, ssid: str = None, key: str = None, *, bssid: bytes = None):
		'''
		Connect to the specified wireless network, using the specified key.

		If `bssid` is given then the connection will be restricted to the
		access-point with that MAC address

		the `ssid` must also be specified in this case.
		'''

	def disconnect(self):
		'''Disconnect from the currently connected wireless network.'''

	def scan(self):
		'''
		Scan for the available wireless networks.

		Hidden networks – where the SSID is not broadcast – will also be scanned
		if the WLAN interface allows it.

		Scanning is only possible on STA interface.

		Returns list of tuples with the information about WiFi access points:

			(ssid, bssid, channel, RSSI, security, hidden)

		`bssid` is hardware address of an access point, in binary form, returned
		as bytes object.

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

	@overload
	def status(self) -> int:
		'''
		Returns value describes the network link status.

		The possible statuses are defined as constants:

		- STAT_IDLE – no connection and no activity,
		- STAT_CONNECTING – connecting in progress,
		- STAT_WRONG_PASSWORD – failed due to incorrect password,
		- STAT_NO_AP_FOUND – failed because no access point replied,
		- STAT_CONNECT_FAIL – failed due to other problems,
		- STAT_GOT_IP – connection successful.
		'''

	@overload
	def status(self, param: str) -> int:
		'''
		Return the current status of the wireless connection.

		The possible statuses are defined as constants:

		- STAT_IDLE – no connection and no activity,
		- STAT_CONNECTING – connecting in progress,
		- STAT_WRONG_PASSWORD – failed due to incorrect password,
		- STAT_NO_AP_FOUND – failed because no access point replied,
		- STAT_CONNECT_FAIL – failed due to other problems,
		- STAT_GOT_IP – connection successful.

		Should be a string naming the status parameter to retrieve.

		Supported parameters in WiFI STA mode are: `'rssi'`.
		'''

	def isconnected(self):
		'''
		In case of STA mode, returns True if connected to a WiFi access point
		and has a valid IP address.

		In AP mode returns True when a station is connected.

		Returns False otherwise.
		'''

	@overload
	def ifconfig(self):
		'''
		Get IP-level network interface parameters: IP address, subnet mask,
		gateway and DNS server.

		This method returns a 4-tuple with the above information.
		'''

	@overload
	def ifconfig(self, if_info: tuple):
		'''
		Set IP-level network interface parameters: IP address, subnet mask,
		gateway and DNS server.

		To set the above values, pass a 4-tuple with the required information.

		For example:

			`nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))`
		'''

	@overload
	def ipconfig(self):
		'''
		Get IP-level network interface parameters: IP address, subnet mask,
		gateway and DNS server.

		This method returns a 4-tuple with the above information.
		'''

	@overload
	def ipconfig(self, ip_info: tuple):
		'''
		Set IP-level network interface parameters: IP address, subnet mask,
		gateway and DNS server.

		To set the above values, pass a 4-tuple with the required information.

		For example:

			`nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))`
		'''

	@overload
	def config(self, param: str):
		'''
		Get general network interface parameters.

		These methods allow to work with additional parameters beyond standard IP
		configuration (as dealt with by `WLAN.ifconfig()`).

		These include network-specific and hardware-specific parameters.

		Parameters name should be quoted as a string, and only one parameter can
		be queries at time.

		Following are commonly supported parameters (availability of a specific
		parameter depends on network technology type, driver, and MicroPython port).

		- mac - MAC address (bytes)
		- ssid - WiFi access point name (string)
		- channel - WiFi channel (integer)
		- hidden - Whether SSID is hidden (boolean)
		- security - Security protocol supported (see module constants)
		- key - Access key (string)
		- hostname - The hostname that will be sent to DHCP (STA interfaces) and
		mDNS (if supported, both STA and AP).

			(Deprecated, use `network.hostname()` instead)

		- reconnects - Number of reconnect attempts to make (integer, 0=none,
		-1=unlimited)
		- txpower - Maximum transmit power in dBm (integer or float)
		- pm - WiFi Power Management setting (see module constants)
		'''

	@overload
	def config(self, **params):
		'''
		Set general network interface parameters.

		These methods allow to work with additional parameters beyond standard IP
		configuration (as dealt with by `WLAN.ifconfig()`).

		These include network-specific and hardware-specific parameters.

		Keyword argument syntax should be used, multiple parameters can be set
		at once.

		Following are commonly supported parameters (availability of a specific
		parameter depends on network technology type, driver, and MicroPython port).

		- mac - MAC address (bytes)
		- ssid - WiFi access point name (string)
		- channel - WiFi channel (integer)
		- hidden - Whether SSID is hidden (boolean)
		- security - Security protocol supported (see module constants)
		- key - Access key (string)
		- hostname - The hostname that will be sent to DHCP (STA interfaces) and
		mDNS (if supported, both STA and AP).

			(Deprecated, use `network.hostname()` instead)

		- reconnects - Number of reconnect attempts to make (integer, 0=none,
		-1=unlimited)
		- txpower - Maximum transmit power in dBm (integer or float)
		- pm - WiFi Power Management setting (see module constants)
		'''
