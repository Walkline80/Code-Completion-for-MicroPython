<h1 align="center">Code Completion for MicroPython</h1>

<p align="center"><img src="https://img.shields.io/badge/Licence-MIT-green.svg?style=for-the-badge" /></p>

**Code Completion for MicroPython** 用于为 VSCode 提供 MicroPython 自有类库的代码补全功能。

## 使用方法

使用快捷键 <kbd>F1</kbd> 打开命令面板，输入 `MicroPython`，然后：

* 选择 `Setup Code Completion for MicroPython` 可以启用代码补全功能
* 选择 `Reset Code Completion for MicroPython` 可以复位代码补全功能

## 类库列表

类库列表包含了 MicroPython 官方提供的类库，以及从互联网获取的一些有用的类库。

> MicroPython 官方类库列表获取自固件文件 `MicroPython v1.24.0-preview.23 on 2024-06-05; ESP32C3 module with ESP32C3`

### MicroPython 官方类库

<details>
<summary>已完成的类库</summary>

- [x] binascii
- [x] bluetooth
- [x] btree

- [x] cmath

- [x] esp
- [x] esp32

- [x] gc

- [x] json

- [x] machine
- [x] math
- [x] micropython

- [x] platform

- [x] random

- [x] struct
- [x] sys

- [x] time

</details>

- [ ] _asyncio
- [ ] _boot
- [ ] _espnow
- [ ] _onewire
- [ ] _thread
- [ ] _webrepl

- [ ] aioespnow
- [ ] apa106
- [ ] array
- [ ] asyncio/__init__
- [ ] asyncio/core
- [ ] asyncio/event
- [ ] asyncio/funcs
- [ ] asyncio/lock
- [ ] asyncio/stream

- [ ] builtins

- [ ] collections
- [ ] cryptolib

- [ ] deflate
- [ ] ds18x20
- [ ] dht

- [ ] errno
- [ ] espnow

- [ ] flashbdev
- [ ] framebuf

- [ ] hashlib
- [ ] heapq

- [ ] inisetup
- [ ] io

- [ ] mip/__init__

- [ ] neopixel
- [ ] network
- [ ] ntptime

- [ ] onewire
- [ ] os

- [ ] requests/__init__
- [ ] re

- [ ] select
- [ ] socket
- [ ] ssl

- [ ] tls

- [ ] uasyncio
- [ ] uctypes
- [ ] umqtt/robust
- [ ] umqtt/simple
- [ ] upysh
- [ ] urequests

- [ ] vfs

- [ ] webrepl
- [ ] webrepl_setup
- [ ] websocket

### 其它类库

<details>
<summary>已完成的类库</summary>

- [x] ble_config: [MicroPython BLE 配网](https://gitee.com/walkline/micropython_ble_config)

- [x] dispatcher: [MicroPython Timer Dispatcher](https://gitee.com/walkline/micropython-timer-dispatcher)

- [x] MicroDNSSrv: [MicroDNSSrv](https://github.com/jczic/MicroDNSSrv)
- [x] MicroWebSrv: [MicroWebSrv](https://github.com/jczic/MicroWebSrv)

- [x] qrcode: [MicroPython QRCode CModule](https://gitee.com/walkline/micropython-qrcode-cmodule)

- [x] smartconfig: [esp32/modsmartconfig: Add smartconfig module](https://github.com/micropython/micropython/pull/13658)

</details>

- [ ] fontlib

- [ ] logging

- [ ] MicroWebSrv2

- [ ] st7789

- [ ] uftpd

- [ ] wtools

## 项目主页

* [Code completion for MicroPython](https://gitee.com/walkline/code-completion-for-micropython)

## 合作交流

* 联系邮箱：<walkline@163.com>
* QQ 交流群：
	* 走线物联：[163271910](https://jq.qq.com/?_wv=1027&k=xtPoHgwL)
	* 扇贝物联：[31324057](https://jq.qq.com/?_wv=1027&k=yp4FrpWh)

<p align="center"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_walkline.png" width="300px" alt="走线物联"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_bigiot.png" width="300px" alt="扇贝物联"></p>
