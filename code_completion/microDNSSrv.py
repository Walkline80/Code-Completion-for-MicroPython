'''
MicroDNSSrv is a micro DNS server for MicroPython to simply respond to A queries (principally used on ESP32 and Pycom modules)

Simple but effective :

- Use it to embed a fast DNS server in yours modules
- Simply responds to A queries (only)
- Use a list of multiple domains
- Include wildcards in the scheme of names
- Use it to make a captive portal simply
'''
# Docs: https://github.com/jczic/MicroDNSSrv


class MicroDNSSrv :
	def Create(self, domainsList) :
		'''
		Speed Creation

		- domainsList
		
		eg. domainsList = {
				"test.com"   : "1.1.1.1",
				"*test2.com" : "2.2.2.2",
				"*google*"   : "192.168.4.1",
				"*.toto.com" : "192.168.4.1",
				"www.site.*" : "192.168.4.1" }
		'''

	def __init__(self) :
		'''Initialize class'''

	def Start(self) :
		'''Start dns server'''

	def Stop(self) :
		'''Stop dns server'''

	def IsStarted(self) :
		'''Dns server start status'''

	def SetDomainsList(self, domainsList) :
		'''Set domains list'''
