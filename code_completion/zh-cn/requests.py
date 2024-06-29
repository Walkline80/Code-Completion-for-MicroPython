'''
requests 库

这个模块提供了一个轻量级的 Python requests 库。

它包括对所有 HTTP 操作、https、json 响应解码、重定向、基本身份验证的支持。

局限性：

- 当前不支持证书验证。

- 作为 POST 数据传递的字典不会自动进行 JSON 或 multipart-form 格式的编码
（可以手动完成）。

- 目前不支持压缩请求/响应。

- 不支持文件上传。

- 不支持响应中的分块编码。

[查看 requests 源码](https://github.com/micropython/micropython-lib/blob/master/python-ecosys/requests/requests/__init__.py)
[查看 API 文档](https://requests.readthedocs.io/en/latest/api/)
'''
class Response:
	'''Response 对象，其中包含服务器对 HTTP 请求的响应。'''
	def __init__(self, f): ...

	def close(self):
		'''
		释放连接回资源池。

		一旦调用了这个方法，底层的原始对象就不应再被访问。
		'''

	@property
	def content(self) -> bytes:
		'''响应的内容（字节）。'''

	@property
	def text(self) -> str:
		'''响应的内容（Unicode）。'''

	def json(self) -> dict:
		'''返回响应的 json 编码内容（如果有）。'''


def request(method: str, url: str, data=None, json: dict = None, headers: dict = None,
		stream: bool = None, auth: tuple = None, timeout: float=None,
		parse_headers: bool = True) -> Response:
	'''
	构造并发送请求。

	参数：

	- `method` – 新请求对象的方法：`GET`、`HEAD`、`POST`、`PUT`、`PATCH`或`DELETE`。

	- `url` – 新请求对象的 URL 地址。

	- `data` –（可选）要发送到请求体中的字典、元组列表、字节或类似文件的对象。

	- `json` – （可选）要发送到请求体中的可序列化的 Python 对象。

	- `headers` –（可选）要与请求一起发送的 HTTP 头的字典。

	- `stream` –（可选）如果为 `False`，则立即下载响应内容。

	- `auth` –（可选）启用基本/摘要/自定义 HTTP 身份验证的 Auth 元组。

	- `timeout` –（可选）等待服务器发送数据的秒数，以浮点数表示。

	- `parse_headers` –（可选）如果为 `True`，将解析头并将其添加到响应中。

	返回一个`Response`对象。
	'''

def head(url: str, **kw) -> Response:

	'''发送`HEAD`请求。'''

def get(url: str, **kw) -> Response:
	'''发送`GET`请求。'''

def post(url: str, **kw) -> Response:
	'''发送`POST`请求。'''

def put(url, **kw) -> Response:
	'''发送`PUT`请求。'''

def patch(url, **kw) -> Response:
	'''发送`PATCH`请求。'''

def delete(url, **kw) -> Response:
	'''发送`DELETE`请求。'''
