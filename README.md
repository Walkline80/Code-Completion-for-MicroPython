<h1 align="center">Code Completion for MicroPython</h1>

<p align="center"><img src="https://img.shields.io/badge/Licence-MIT-green.svg?style=for-the-badge&&logo=gitee" /></p>

**Code Completion for MicroPython** 扩展程序用于为 VSCode 提供 MicroPython 类库代码补全功能。

## 使用方法

使用快捷键 <kbd>F1</kbd> 打开命令面板，输入 `MicroPython`，然后：

* 选择 `MicroPython: 启用代码补全功能` 启用扩展
* 选择 `MicroPython: 禁用代码补全功能` 禁用扩展
* 选择 `MicroPython: 多语言文档支持` 启用/禁用多语言内容提示

## 类库列表

类库列表包含了 MicroPython 官方提供的类库，以及从互联网获取的一些有用的类库。

> MicroPython 官方类库列表获取自固件文件 `MicroPython v1.24.0-preview.23 on 2024-06-05; ESP32C3 module with ESP32C3`

### MicroPython 官方类库

<details>
<summary>已完成的类库</summary>

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
<summary>未完成的类库</summary>

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

<details>
<summary>未完成的类库</summary>

- [ ] MicroWebSrv2

- [ ] st7789

- [ ] wtools

</details>


### 多语言文档支持

计划对已完成的类库文件中的说明内容进行本地化翻译。

<details>
<summary>已完成的类库</summary>

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
<summary>未完成的类库</summary>

- [ ] asyncio

- [ ] ssl

- [ ] uasyncio


- [ ] MicroDNSSrv: [MicroDNSSrv](https://github.com/jczic/MicroDNSSrv)
- [ ] MicroWebSrv: [MicroWebSrv](https://github.com/jczic/MicroWebSrv)

</details>

## 项目主页

* [Gitee: Code completion for MicroPython](https://gitee.com/walkline/code-completion-for-micropython)

## 合作交流

* 联系邮箱：<walkline@163.com>
* QQ 交流群：
	* 走线物联：[163271910](https://jq.qq.com/?_wv=1027&k=xtPoHgwL)
	* 扇贝物联：[31324057](https://jq.qq.com/?_wv=1027&k=yp4FrpWh)

<p align="center"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_walkline.png" width="300px" alt="走线物联"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_bigiot.png" width="300px" alt="扇贝物联"></p>
