'''
requests

This module provides a lightweight version of the Python requests library.

It includes support for all HTTP verbs, https, json decoding of responses, redirects, basic authentication.

Limitations:

- Certificate validation is not currently supported.

- A dictionary passed as post data will not do automatic JSON or multipart-form encoding of post data (this can be done manually).

- Compressed requests/responses are not currently supported.

- File upload is not supported.

- Chunked encoding in responses is not supported.

[View Doc requests](https://github.com/micropython/micropython-lib/blob/master/python-ecosys/requests/README.md)
[View Doc api](https://requests.readthedocs.io/en/latest/api/)
'''
class Response:
	'''
	The Response object, which contains a server’s response to an HTTP request.
	'''
	def __init__(self, f):
		pass

	def close(self):
		'''
		Releases the connection back to the pool.

		Once this method has been called the underlying raw object must not be accessed again.
		'''

	@property
	def content(self):
		'''Content of the response, in bytes.'''

	@property
	def text(self):
		'''Content of the response, in unicode.'''

	def json(self):
		'''Returns the json-encoded content of a response, if any.'''


def request(method: str, url: str, data=None, json=None, headers=None,
		stream=None, auth=None, timeout=None, parse_headers: bool = True):
	'''
	Constructs and sends a Request.

	Parameters:

	- `method` – method for the new Request object: `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, or `DELETE`.

	- `url` – URL for the new Request object.

	- `data` – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.

	- `json` – (optional) A JSON serializable Python object to send in the body of the Request.

	- `headers` – (optional) Dictionary of HTTP Headers to send with the Request.

	- `stream` – (optional) if False, the response content will be immediately downloaded.

	- `auth` – (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.

	- `timeout` – (optional) How many seconds to wait for the server to send data before giving up, as a float.

	- `parse_headers` – (optional) If True, will parse headers and add them to the response.

	Returns a Response object.
	'''

def head(url: str, **kw):
	'''Sends a HEAD request.'''

def get(url: str, **kw):
	'''Sends a GET request.'''

def post(url: str, **kw):
	'''Sends a POST request.'''

def put(url, **kw):
	'''Sends a PUT request.'''

def patch(url, **kw):
	'''Sends a PATCH request.'''

def delete(url, **kw):
	'''Sends a DELETE request.'''
