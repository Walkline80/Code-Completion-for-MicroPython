<h1 align="center">Code Completion for MicroPython</h1>

<p align="center"><img src="https://img.shields.io/badge/Licence-MIT-green.svg?style=for-the-badge&&logo=gitee" /></p>

[使用说明（简体中文）](README.md)

**Code Completion for MicroPython** Extension to provide MicroPython library code completion for VSCode.

![demo](https://raw.githubusercontent.com/Walkline80/Code-Completion-for-MicroPython/master/images/demo.gif)

## How to use

Use the shortcut <kbd>F1</kbd> to open the command panel, type `MicroPython`, and:

* Select `MicroPython: Enable Code Completion` to enable the extension.
* Select `MicroPython: Disable Code Completion` to disable extensions.
* Select `MicroPython: Multi-Language Documentation Support` to enable/disable multi-language content hinting

	> Currently only English and Simplified Chinese are supported.

## Libraries List

The list of libraries contains the official MicroPython libraries, as well as some useful libraries obtained from the Internet.

### MicroPython Official Libraries

> MicroPython official libraries list from firmware file `MicroPython v1.24.0-preview.23 on 2024-06-05; ESP32C3 module with ESP32C3`

<details>
<summary>Completed libraries</summary>

- [x] array
- [x] asyncio

- [x] binascii
- [x] bluetooth
- [x] btree

- [x] cmath
- [x] collections
- [x] cryptolib

- [x] deflate
- [x] dht
- [x] ds18x20

- [x] errno
- [x] esp
- [x] esp32

- [x] framebuf

- [x] gc

- [x] hashlib
- [x] heapq

- [x] json

- [x] machine
- [x] math
- [x] micropython
- [x] mip

- [x] neopixel
- [x] network
- [x] ntptime

- [x] platform

- [x] onewire
- [x] os

- [x] random
- [x] re
- [x] requests

- [x] select
- [x] socket
- [x] ssl
- [x] struct
- [x] sys

- [x] time

- [x] uasyncio
- [x] uctypes
- [x] umqtt/robust
- [x] umqtt/simple

</details>

<details>
<summary>Unfinished libraries</summary>

- [ ] _thread

- [ ] aioespnow
- [ ] apa106

- [ ] espnow

- [ ] io

- [ ] tls

- [ ] vfs

- [ ] webrepl
- [ ] webrepl_setup
- [ ] websocket

</details>

### Other Libraries

<details>
<summary>Completed libraries</summary>

- [x] ble_config: [MicroPython BLE 配网](https://gitee.com/walkline/micropython_ble_config)

- [x] dispatcher: [MicroPython Timer Dispatcher](https://gitee.com/walkline/micropython-timer-dispatcher)

- [x] MicroDNSSrv: [MicroDNSSrv](https://github.com/jczic/MicroDNSSrv)
- [x] MicroWebSrv: [MicroWebSrv](https://github.com/jczic/MicroWebSrv)

- [x] qrcode: [MicroPython QRCode CModule](https://gitee.com/walkline/micropython-qrcode-cmodule)

- [x] smartconfig: [esp32/modsmartconfig: Add smartconfig module](https://github.com/micropython/micropython/pull/13658)

</details>

<details>
<summary>Unfinished libraries</summary>

- [ ] MicroWebSrv2

- [ ] st7789

- [ ] wtools

</details>


### Multi-Language Documentation Support

<details>
<summary>Completed libraries</summary>

- [x] array

- [x] binascii
- [x] bluetooth
- [x] btree

- [x] cmath
- [x] collections
- [x] cryptolib

- [x] deflate
- [x] dht
- [x] ds18x20

- [x] esp
- [x] esp32
- [x] errno

- [x] framebuf

- [x] gc

- [x] hashlib
- [x] heapq

- [x] json

- [x] machine
- [x] math
- [x] micropython
- [x] mip

- [x] neopixel
- [x] network
- [x] ntptime

- [x] onewire
- [x] os

- [x] platform

- [x] random
- [x] re
- [x] requests

- [x] select
- [x] socket
- [x] struct
- [x] sys

- [x] time

- [x] uctypes
- [x] umqtt/robust
- [x] umqtt/simple


- [x] ble_config: [MicroPython BLE 配网](https://gitee.com/walkline/micropython_ble_config)

- [x] dispatcher: [MicroPython Timer Dispatcher](https://gitee.com/walkline/micropython-timer-dispatcher)

- [x] qrcode: [MicroPython QRCode CModule](https://gitee.com/walkline/micropython-qrcode-cmodule)

- [x] smartconfig: [esp32/modsmartconfig: Add smartconfig module](https://github.com/micropython/micropython/pull/13658)

</details>

<details>
<summary>Unfinished libraries</summary>

- [ ] asyncio

- [ ] ssl

- [ ] uasyncio


- [ ] MicroDNSSrv: [MicroDNSSrv](https://github.com/jczic/MicroDNSSrv)
- [ ] MicroWebSrv: [MicroWebSrv](https://github.com/jczic/MicroWebSrv)

</details>

## Project Home

* [Gitee: Code completion for MicroPython](https://gitee.com/walkline/code-completion-for-micropython)

## Communication

* Contact Email: <walkline@163.com>
