'''
This module provides an interface to a Bluetooth controller on a board.

Currently this supports Bluetooth Low Energy (BLE) in Central, Peripheral, Broadcaster, and Observer roles, as well as GATT Server and Client and L2CAP connection-oriented-channels.

A device may operate in multiple roles concurrently.

Pairing (and bonding) is supported on some ports.

This API is intended to match the low-level Bluetooth protocol and provide building-blocks for higher-level abstractions such as specific device types.
'''
# Docs: https://docs.micropython.org/en/latest/library/bluetooth.html


# class BLE
class BLE(object):
	'''Returns the singleton BLE object.'''
	# Configuration
	def active(self, active: bool | None, /):
		'''
		Optionally changes the active state of the BLE radio, and returns the current state.

		The radio must be made active before using any other methods on this class.
		'''

	def config(self, param: str, /):
		'''
		config(self, *, param, ...)

		Get or set configuration values of the BLE interface.

		To get a value the parameter name should be quoted as a string, and just one parameter is queried at a time.

		To set values use the keyword syntax, and one or more parameter can be set at a time.

		Currently supported values are:

		- 'mac': The current address in use, depending on the current address mode. This returns a tuple of (addr_type, addr).

			This may only be queried while the interface is currently active.

		- 'addr_mode': Sets the address mode. Values can be:

			- 0x00 - PUBLIC - Use the controller’s public address.
			- 0x01 - RANDOM - Use a generated static address.
			- 0x02 - RPA - Use resolvable private addresses.
			- 0x03 - NRPA - Use non-resolvable private addresses.

			By default the interface mode will use a PUBLIC address if available, otherwise it will use a RANDOM address.

		- 'gap_name': Get/set the GAP device name used by service 0x1800, characteristic 0x2a00.

			This can be set at any time and changed multiple times.

		- 'rxbuf': Get/set the size in bytes of the internal buffer used to store incoming events.

			This buffer is global to the entire BLE driver and so handles incoming data for all events, including all characteristics.

			Increasing this allows better handling of bursty incoming data (for example scan results) and the ability to receive larger characteristic values.

		- 'mtu': Get/set the MTU that will be used during a ATT MTU exchange.

			The resulting MTU will be the minimum of this and the remote device’s MTU.

			ATT MTU exchange will not happen automatically (unless the remote device initiates it), and must be manually initiated with gattc_exchange_mtu.

			Use the `_IRQ_MTU_EXCHANGED` event to discover the MTU for a given connection.

		- 'bond': Sets whether bonding will be enabled during pairing.

			When enabled, pairing requests will set the "bond" flag and the keys will be stored by both devices.

		- 'mitm': Sets whether MITM-protection is required for pairing.

		- 'io': Sets the I/O capabilities of this device. Available options are:

			- _IO CAPABILITY DISPLAY ONLY = const(0)
			- _IO_CAPABILITY_DISPLAY_YESNO = const(1)
			- _IO_CAPABILITY_KEYBOARD_ONLY = const(2)
			- _IO_CAPABILITY_NO_INPUT_OUTPUT = const(3)
			- _IO_CAPABILITY_KEYBOARD_DISPLAY = const(4)

		'le_secure': Sets whether "LE Secure" pairing is required.

			Default is false (i.e. allow "Legacy Pairing").
		'''

	# Event Handling
	def irq(self, handler: function, /):
		'''
		Registers a callback for events from the BLE stack.

		The `handler` takes two arguments:

		- event (which will be one of the codes below)

		- data (which is an event-specific tuple of values).
		'''

	# Broadcaster Role (Advertiser)
	def gap_advertise(self, interval_us: int, adv_data=None, *, resp_data=None, connectable: bool = True):
		'''
		Starts advertising at the specified interval (in microseconds).

		This interval will be rounded down to the nearest 625us.

		To stop advertising, set `interval_us` to None.

		`adv_data` and `resp_data` can be any type that implements the buffer protocol (e.g. bytes, bytearray, str).

		`adv_data` is included in all broadcasts, and `resp_data` is send in reply to an active scan.

		Note:

			if `adv_data` (or `resp_data`) is None, then the data passed to the previous call to gap_advertise will be reused.

			This allows a broadcaster to resume advertising with just gap_advertise(interval_us).

			To clear the advertising payload pass an empty bytes, i.e. b''.
		'''

	# Observer Role (Scanner)
	def gap_scan(self, duration_ms: int, interval_us: int = 1280000, window_us: int = 11250, active: bool = False, /):
		'''
		Run a scan operation lasting for the specified duration (in milliseconds).

		To scan indefinitely, set `duration_ms` to 0.

		To stop scanning, set `duration_ms` to None.

		Use `interval_us` and `window_us` to optionally configure the duty cycle.

		The scanner will run for `window_us` microseconds every `interval_us` microseconds for a total of `duration_ms` milliseconds.

		The default interval and window are 1.28 seconds and 11.25 milliseconds respectively (background scanning).

		For each scan result the `_IRQ_SCAN_RESULT` event will be raised, with event data (addr_type, addr, adv_type, rssi, adv_data).

		- addr_type values indicate public or random addresses:

			- 0x00 - PUBLIC
			- 0x01 - RANDOM (either static, RPA, or NRPA, the type is encoded in the address itself)

		- adv_type values correspond to the Bluetooth Specification:

			- 0x00 - ADV_IND - connectable and scannable undirected advertising
			- 0x01 - ADV_DIRECT_IND - connectable directed advertising
			- 0x02 - ADV_SCAN_IND - scannable undirected advertising
			- 0x03 - ADV_NONCONN_IND - non-connectable undirected advertising
			- 0x04 - SCAN_RSP - scan response

		`active` can be set True if you want to receive scan responses in the results.

		When scanning is stopped (either due to the duration finishing or when explicitly stopped), the `_IRQ_SCAN_DONE` event will be raised.
		'''

	# Central Role
	def gap_connect(self, addr_type: int, addr, scan_duration_ms: int = 2000,
			min_conn_interval_us: int | None = None, max_conn_interval_us: int | None = None, /):
		'''
		Connect to a peripheral.

		To cancel an outstanding connection attempt early, call gap_connect(None).

		On success, the `_IRQ_PERIPHERAL_CONNECT` event will be raised.

		If cancelling a connection attempt, the `_IRQ_PERIPHERAL_DISCONNECT` event will be raised.

		The device will wait up to `scan_duration_ms` to receive an advertising payload from the device.

		The connection interval can be configured in microseconds using either or both of `min_conn_interval_us` and `max_conn_interval_us`.

		Otherwise a default interval will be chosen, typically between 30000 and 50000 microseconds.

		A shorter interval will increase throughput, at the expense of power usage.
		'''

	# Central & Peripheral Roles
	def gap_disconnect(self, conn_handle: int, /):
		'''
		Disconnect the specified connection handle.

		This can either be a central that has connected to this device (if acting as a peripheral) or a peripheral that was previously connected to by this device (if acting as a central).

		On success, the `_IRQ_PERIPHERAL_DISCONNECT` or `_IRQ_CENTRAL_DISCONNECT` event will be raised.

		Returns False if the connection handle wasn’t connected, and True otherwise.
		'''

	# GATT Server
	def gatts_register_services(self, services_definition, /):
		'''
		Configures the server with the specified services, replacing any existing services.

		`services_definition` is a list of services, where each service is a two-element tuple containing a UUID and a list of characteristics.

		Each characteristic is a two-or-three-element tuple containing a UUID, a flags value, and optionally a list of descriptors.

		Each descriptor is a two-element tuple containing a UUID and a flags value.

		The flags are a bitwise-OR combination of the flags defined below.

		These set both the behaviour of the characteristic (or descriptor) as well as the security and privacy requirements.

		The return value is a list (one element per service) of tuples (each element is a value handle).

		Characteristics and descriptor handles are flattened into the same tuple, in the order that they are defined.
		'''

	def gatts_read(self, value_handle: int, /):
		'''
		Reads the local value for this handle (which has either been written by gatts_write or by a remote client).
		'''

	def gatts_write(self, value_handle: int, data, send_update: bool = False, /):
		'''
		Writes the local value for this handle, which can be read by a client.

		If `send_update` is True, then any subscribed clients will be notified

		(or indicated, depending on what they’re subscribed to and which operations the characteristic supports) about this write.
		'''

	def gatts_notify(self, conn_handle: int, value_handle: int, data=None, /):
		'''
		Sends a notification request to a connected client.

		If `data` is None (the default), then the current local value (as set with gatts_write) will be sent.

		Otherwise, if `data` is not None, then that value is sent to the client as part of the notification. The local value will not be modified.

		Note:

			The notification will be sent regardless of the subscription status of the client to this characteristic.
		'''

	def gatts_indicate(self, conn_handle: int, value_handle: int, data=None, /):
		'''
		Sends a indication request to a connected client.

		If `data` is None (the default), then the current local value (as set with gatts_write) will be sent.

		Otherwise, if `data` is not None, then that value is sent to the client as part of the indication. The local value will not be modified.

		On acknowledgment (or failure, e.g. timeout), the `_IRQ_GATTS_INDICATE_DONE` event will be raised.

		Note:

			The indication will be sent regardless of the subscription status of the client to this characteristic.
		'''

	def gatts_set_buffer(self, value_handle: int, len: int, append: bool = False, /):
		'''
		Sets the internal buffer size for a value in bytes.

		This will limit the largest possible write that can be received.

		The default is 20.

		Setting `append` to True will make all remote writes append to, rather than replace, the current value.
		'''

	# GATT Client
	def gattc_discover_services(self, conn_handle: int, uuid=None, /):
		'''
		Query a connected server for its services.

		Optionally specify a service `uuid` to query for that service only.

		For each service discovered, the `_IRQ_GATTC_SERVICE_RESULT` event will be raised, followed by `_IRQ_GATTC_SERVICE_DONE` on completion.
		'''

	def gattc_discover_characteristics(self, conn_handle: int, start_handle: int, end_handle: int, uuid=None, /):
		'''
		Query a connected server for characteristics in the specified range.

		Optionally specify a characteristic `uuid` to query for that characteristic only.

		You can use `start_handle`=1, `end_handle`=0xffff to search for a characteristic in any service.

		For each characteristic discovered, the `_IRQ_GATTC_CHARACTERISTIC_RESULT` event will be raised, followed by `_IRQ_GATTC_CHARACTERISTIC_DONE` on completion.
		'''

	def gattc_discover_descriptors(self, conn_handle: int, start_handle: int, end_handle: int, /):
		'''
		Query a connected server for descriptors in the specified range.

		For each descriptor discovered, the `_IRQ_GATTC_DESCRIPTOR_RESULT` event will be raised, followed by `_IRQ_GATTC_DESCRIPTOR_DONE` on completion.
		'''

	def gattc_read(self, conn_handle: int, value_handle: int, /):
		'''
		Issue a remote read to a connected server for the specified characteristic or descriptor handle.

		When a value is available, the `_IRQ_GATTC_READ_RESULT` event will be raised.

		Additionally, the `_IRQ_GATTC_READ_DONE` will be raised.
		'''

	def gattc_write(self, conn_handle: int, value_handle: int, data, mode: int = 0, /):
		'''
		Issue a remote write to a connected server for the specified characteristic or descriptor handle.

		The argument `mode` specifies the write behaviour, with the currently supported values being:

		- mode=0 (default) is a write-without-response: the write will be sent to the remote server but no confirmation will be returned, and no event will be raised.
		- mode=1 is a write-with-response: the remote server is requested to send a response/acknowledgement that it received the data.

		If a response is received from the remote server the `_IRQ_GATTC_WRITE_DONE` event will be raised.
		'''

	def gattc_exchange_mtu(self, conn_handle: int, /):
		'''
		Initiate MTU exchange with a connected server, using the preferred MTU set using BLE.config(mtu=value).

		The `_IRQ_MTU_EXCHANGED` event will be raised when MTU exchange completes.

		Note:

			MTU exchange is typically initiated by the central.

			When using the BlueKitchen stack in the central role, it does not support a remote peripheral initiating the MTU exchange.

			NimBLE works for both roles.
		'''

	# L2CAP connection-oriented-channels
	def l2cap_listen(self, psm, mtu, /):
		'''
		Start listening for incoming L2CAP channel requests on the specified `psm` with the local MTU set to `mtu`.

		When a remote device initiates a connection, the `_IRQ_L2CAP_ACCEPT` event will be raised, which gives the listening server a chance to reject the incoming connection (by returning a non-zero integer).

		Once the connection is accepted, the `_IRQ_L2CAP_CONNECT` event will be raised, allowing the server to obtain the channel id (CID) and the local and remote MTU.

		Note:

			It is not currently possible to stop listening.
		'''

	def l2cap_connect(self, conn_handle: int, psm, mtu, /):
		'''
		Connect to a listening peer on the specified `psm` with local MTU set to `mtu`.

		On successful connection, the the `_IRQ_L2CAP_CONNECT` event will be raised, allowing the client to obtain the CID and the local and remote (peer) MTU.

		An unsuccessful connection will raise the `_IRQ_L2CAP_DISCONNECT` event with a non-zero status.
		'''

	def l2cap_disconnect(self, conn_handle: int, cid, /):
		'''
		Disconnect an active L2CAP channel with the specified `conn_handle` and `cid`.
		'''

	def l2cap_send(self, conn_handle: int, cid, buf, /):
		'''
		Send the specified `buf` (which must support the buffer protocol) on the L2CAP channel identified by `conn_handle` and `cid`.

		The specified buffer cannot be larger than the remote (peer) MTU, and no more than twice the size of the local MTU.

		This will return False if the channel is now "stalled", which means that l2cap_send must not be called again until the `_IRQ_L2CAP_SEND_READY` event is received (which will happen when the remote device grants more credits, typically after it has received and processed the data).
		'''

	def l2cap_recvinto(self, conn_handle: int, cid, buf, /):
		'''
		Receive data from the specified `conn_handle` and `cid` into the provided `buf` (which must support the buffer protocol, e.g. bytearray or memoryview).

		Returns the number of bytes read from the channel.

		If `buf` is None, then returns the number of bytes available.

		Note:

			After receiving the `_IRQ_L2CAP_RECV` event, the application should continue calling l2cap_recvinto until no more bytes are available in the receive buffer (typically up to the size of the remote (peer) MTU).

		Until the receive buffer is empty, the remote device will not be granted more channel credits and will be unable to send any more data.
		'''

	# Pairing and bonding
	def gap_pair(self, conn_handle: int, /):
		'''
		Initiate pairing with the remote device.

		Before calling this, ensure that the `io`, `mitm`, `le_secure`, and `bond` configuration options are set (via config).

		On successful pairing, the `_IRQ_ENCRYPTION_UPDATE` event will be raised.
		'''

	def gap_passkey(self, conn_handle: int, action: int, passkey, /):
		'''
		Respond to a `_IRQ_PASSKEY_ACTION` event for the specified `conn_handle` and `action`.

		The `passkey` is a numeric value and will depend on on the `action` (which will depend on what I/O capability has been set):

		When the `action` is `_PASSKEY_ACTION_INPUT`, then the application should prompt the user to enter the `passkey` that is shown on the remote device.

		When the `action` is `_PASSKEY_ACTION_DISPLAY`, then the application should generate a random 6-digit `passkey` and show it to the user.

		When the `action` is `_PASSKEY_ACTION_NUMERIC_COMPARISON`, then the application should show the passkey that was provided in the `_IRQ_PASSKEY_ACTION` event and then respond with either 0 (cancel pairing), or 1 (accept pairing).
		'''


# class UUID
class UUID(object):
	'''
	Creates a UUID instance with the specified `value`.

	The `value` can be either:

	- A 16-bit integer. e.g. 0x2908.
	- A 128-bit UUID string. e.g. '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'.
	'''
	def __init__(self, value, /):
		pass


# Constants
FLAG_READ = ...
FLAG_WRITE = ...
FLAG_NOTIFY = ...
FLAG_INDICATE = ...
FLAG_WRITE_NO_RESPONSE = ...