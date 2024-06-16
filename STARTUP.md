<h1 align="center">操作流程</h1>

## 安装 Visual Studio Code Extension Manager

```bash
npm install -g vsce
```

> Node.js at least 18.x.x.

## 安装项目依赖

进入项目目录执行如下命令，或者直接直接使用<kbd>F5</kbd>运行插件。

```bash
npm install
```

## 打包插件文件

进入项目目录执行如下命令，会生成一个`.vsix`文件，即打包好的插件文件。

```bash
vsce package
```

## 上传插件

访问 [Manage Publishers & Extensions](https://marketplace.visualstudio.com/manage) 页面，注册`Publisher ID`并上传`.vsix`文件即可。

## 合作交流

* 联系邮箱：<walkline@163.com>
* QQ 交流群：
	* 走线物联：[163271910](https://jq.qq.com/?_wv=1027&k=xtPoHgwL)
	* 扇贝物联：[31324057](https://jq.qq.com/?_wv=1027&k=yp4FrpWh)

<p align="center"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_walkline.png" width="300px" alt="走线物联"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_bigiot.png" width="300px" alt="扇贝物联"></p>
