'''
MicroWebSrv is a micro HTTP Web server that supports WebSockets, html/python
language templating and routing handlers, for MicroPython

(principally used on ESP32 and Pycom modules. Now supports all variants of Pyboard
D-series from the makers of Micropython)

Very easy to integrate and very light with 3 files only:

- 'microWebSrv.py' - The Web server
- 'microWebSocket.py' - The optional support of WebSockets
- 'microWebTemplate.py' - The optional templating language for .pyhtml rendered pages

[View Doc](https://github.com/jczic/MicroWebSrv)
'''
class MicroWebSrvRoute:
	def __init__(self, route, method, func, routeArgNames, routeRegex):
		'''Initialize class'''


class MicroWebSrv:
	@classmethod
	def route(cls, url, method='GET'):
		'''Adds a route handler function to the routing list'''

	@staticmethod
	def HTMLEscape(s):
		'''HTML Escape'''

	def __init__(self, routeHandlers = [], port = 80, bindIP = '0.0.0.0',
		webPath = "/flash/www"):
		'''Initialize class'''

	def Start(self, threaded: bool = False):
		'''Start'''

	def Stop(self):
		'''Stop'''

	def IsStarted(self):
		'''IsStarted'''

	def SetNotFoundPageUrl(self, url: str = None):
		'''SetNotFoundPageUrl'''

	def GetMimeTypeFromFilename(self, filename: str):
		'''GetMimeTypeFromFilename'''
	
	def GetRouteHandler(self, resUrl, method):
		'''GetRouteHandler'''


	class _client:
		def __init__(self, microWebSrv, socket, addr):
			'''Initialize class'''

		def GetServer(self):
			'''GetServer'''

		def GetAddr(self):
			'''GetAddr'''

		def GetIPAddr(self):
			'''GetIPAddr'''

		def GetPort(self):
			'''GetPort'''

		def GetRequestMethod(self):
			'''GetRequestMethod'''

		def GetRequestTotalPath(self):
			'''GetRequestTotalPath'''

		def GetRequestPath(self):
			'''GetRequestPath'''

		def GetRequestQueryString(self):
			'''GetRequestQueryString'''

		def GetRequestQueryParams(self):
			'''GetRequestQueryParams'''

		def GetRequestHeaders(self):
			'''GetRequestHeaders'''

		def GetRequestContentType(self):
			'''GetRequestContentType'''

		def GetRequestContentLength(self):
			'''GetRequestContentLength'''

		def ReadRequestContent(self, size=None):
			'''ReadRequestContent'''

		def ReadRequestPostedFormData(self):
			'''ReadRequestPostedFormData'''

		def ReadRequestContentAsJSON(self):
			'''ReadRequestContentAsJSON'''


	class _response:
		def __init__(self, client):
			'''Initialize class'''

		def WriteSwitchProto(self, upgrade, headers=None):
			'''WriteSwitchProto'''

		def WriteResponse(self, code, headers, contentType, contentCharset, content):
			'''WriteResponse'''

		def WriteResponsePyHTMLFile(self, filepath, headers=None, vars=None):
			'''WriteResponsePyHTMLFile'''

		def WriteResponseFile(self, filepath, contentType=None, headers=None):
			'''WriteResponseFile'''

		def WriteResponseFileAttachment(self, filepath, attachmentName, headers=None):
			'''WriteResponseFileAttachment'''

		def WriteResponseOk(self, headers=None, contentType=None, contentCharset=None, content=None):
			'''WriteResponseOk'''

		def WriteResponseJSONOk(self, obj=None, headers=None):
			'''WriteResponseJSONOk'''

		def WriteResponseRedirect(self, location):
			'''WriteResponseRedirect'''

		def WriteResponseError(self, code):
			'''WriteResponseError'''

		def WriteResponseJSONError(self, code, obj=None):
			'''WriteResponseJSONError'''

		def WriteResponseNotModified(self):
			'''WriteResponseNotModified'''

		def WriteResponseBadRequest(self):
			'''WriteResponseBadRequest'''

		def WriteResponseForbidden(self):
			'''WriteResponseForbidden'''

		def WriteResponseNotFound(self):
			'''WriteResponseNotFound'''

		def WriteResponseMethodNotAllowed(self):
			'''WriteResponseMethodNotAllowed'''

		def WriteResponseInternalServerError(self):
			'''WriteResponseInternalServerError'''

		def WriteResponseNotImplemented(self):
			'''WriteResponseNotImplemented'''

		def FlashMessage(self, messageText, messageStyle=''):
			'''FlashMessage'''
