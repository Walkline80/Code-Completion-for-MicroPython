# Code Completion for MicroPython Change Log

## [Unreleased]


## [Version 0.1.3]: 2024-07-06

### Updated

将说明文档多语言跳转指向 Github。


## [Version 0.1.3]: 2024-07-06

### Updated

更新演示动画内容。


## [Version 0.1.2]: 2024-07-06

### Fixed

修复说明文档语言版本冲突问题。


## [Version 0.1.1]: 2024-07-06

### Added

增加英文说明文档。

### Updated

更新扩展英文显示内容。

### Fixed

修复中文翻译中的 [输入错误](https://gitee.com/walkline/code-completion-for-micropython/issues/IAB0IR)。


## [Version 0.1.0]: 2024-07-05

### Updated

给类库文件中的常量增加数据类型。

翻译类库文件：

* array

* binascii
* bluetooth
* btree

* cmath
* collections
* cryptolib

* deflate
* dht
* ds18x20

* esp
* esp32
* errno

* framebuf

* gc

* hashlib
* heapq

* json

* machine
* math
* micropython
* mip

* neopixel
* network
* ntptime

* onewire
* os

* platform

* random
* re
* requests

* select
* socket
* struct
* sys

* time

* uctypes
* umqtt/robust
* umqtt/simple


* ble_config
* dispatcher
* qrcode
* smartconfig


## [Version 0.0.12]: 2024-06-23

### Added

增加代码补全文件多语言文档支持，并计划开始翻译中文文档。


## [Version 0.0.11]: 2024-06-23

### Added

* 增加多语言支持
* 增加自动更新插件设置功能，用于在扩展自动更新后刷新插件设置


## [Version 0.0.10]: 2024-06-23

### Updated

调整注释内容格式。


## [Version 0.0.9]: 2024-06-21

### Updated

为类库文件中的常量增加注释。


## [Version 0.0.8]: 2024-06-20

### Added

增加代码补全类库文件：

* array.py
* collections.py
* deflate.py
* dht.py
* ds18x20.py
* errno.py
* ssl.py
* uctypes.py
* umqtt/robust.py
* umqtt/simple.py

### Updated

优化调整代码补全类库文件内容格式。


## [Version 0.0.7]: 2024-06-19

### Fixed

优化 `update_configuration()` 函数执行顺序，并增加错误捕捉。


## [Version 0.0.6]: 2024-06-19

### Added

增加代码补全类库文件：

* asyncio.py

* re.py

* select.py
* socket.py

* uasyncio.py

### Updated

各类库文件增加参考文档链接。


## [Version 0.0.5]: 2024-06-19

### Added

增加代码补全类库文件：

* cryptolib.py

* framebuf.py

* hashlib
* heapq.py

* mip.py

* neopixel.py
* network.py: 包含 WLAN 类模块
* ntptime.py

* onewire.py
* os.py

* requests.py

### Updated

修改命令面板中显示命令的标题，使其具有分组效果。


## [Version 0.0.4]: 2024-06-17

### Added

增加 `Reset Code Completion for MicroPython` 命令，用于清除之前的设置。


## [Version 0.0.3]: 2024-06-17

### Added

增加代码补全类库文件：

* ble_config.py

* cmath.py

* dispatcher.py

* gc.py

* json.py

* machine.py
* math.py
* microDNSSrv.py
* microWebSrv.py

* platform.py

* qrcode.py

* random.py

* smartconfig.py
* struct.py
* sys.py

* time.py


## [Version 0.0.2]: 2024-06-16

### Added

增加代码补全类库文件：

* binascii.py
* bluetooth.py
* btree.py

* esp.py
* esp32.py

* micropython.py


## [Version 0.0.1]: 2024-06-16

### Added

初始化项目：

* 增加 .gitignore 文件
* 增加 vscode extension 脚手架文件
* 增加 操作流程 文档

### Removed

删除无用文件。


[unreleased]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.1.4...HEAD
[Version 0.1.4]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.1.3...v0.1.4
[Version 0.1.3]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.1.2...v0.1.3
[Version 0.1.2]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.1.1...v0.1.2
[Version 0.1.1]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.1.0...v0.1.1
[Version 0.1.0]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.12...v0.1.0
[Version 0.0.12]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.11...v0.0.12
[Version 0.0.11]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.10...v0.0.11
[Version 0.0.10]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.9...v0.0.10
[Version 0.0.9]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.8...v0.0.9
[Version 0.0.8]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.7...v0.0.8
[Version 0.0.7]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.6...v0.0.7
[Version 0.0.6]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.5...v0.0.6
[Version 0.0.5]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.4...v0.0.5
[Version 0.0.4]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.3...v0.0.4
[Version 0.0.3]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.2...v0.0.3
[Version 0.0.2]: https://gitee.com/walkline/code-completion-for-micropython/compare/v0.0.1...v0.0.2
[Version 0.0.1]: https://gitee.com/walkline/code-completion-for-micropython/releases/tag/v0.0.1