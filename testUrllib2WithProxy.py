import urllib2
import sys
import re

def testArgument():
	# Testing the input parameters requires only on parameter
	if len(sys.argv) !=2:
		print("Just one argument is enough")
		tipUse()
		exit()
	else:
		TP = TestProxy(sys.argv[1])
	
def tipUse():
	# Show Tips
	print("The program can only enter one parameter,which must be an available proxy")
	print("usage: python testUrllib2WithProxy.py http://1.2.3.4:5")
	print("usage: python testUrllib2WithProxy.py https://1.2.3.4:5")
	
class TestProxy(object):
	# The function of this class is to test whether the proxy is valid
	
	def __init__(self,proxy):
		self.proxy = proxy
		self.checkProxyFormat(self.proxy)
		self.url = 'http://www.baidu.com'
		self.timeout = 5
		self.flagWord = 'BAIDU'
		# find this keyword in the data returned by the web page
		self.useProxy(self.proxy)
		
	def checkProxyFormat(self,proxy):
		try:
			proxyMatch = re.compile('http[s]?://[\d]{1,3}\.[\d\{1,3}\.[\d]{1,3}\.[\d]{1,3}:[\d]{1,5}$')
			re.search(proxyMatch,proxy).group()
		except AttributeError:
			tipUse()
			exit()
		flag = 1
		proxy = proxy.replace('//','')
		try:
			protocol = proxy.split(':')[0]
			ip = proxy.split(':')[1]
			port = proxy.split(':')[2]
		except IndexError:
			print("subscript out of bounds")
			tipUse()
			exit()
			
		flag = flag and len(proxy.split(':')) == 3 and len(ip.split('.')) == 4
		flag = ip.split('.')[0] in map(str,xrange(1,256)) and flag
		flag = ip.split('.')[1] in map(str,xrange(256)) and flag
		flag = ip.split('.')[2] in map(str,xrange(256)) and flag
		flag = ip.split('.')[3] in map(str,xrange(1,255)) and flag
		flag = protocol in [u'http',u'https'] and flag
		flag = port in map(str,range(1,65535)) and flag
		# This is the format of the proxy check
		
		if flag:
			print("The HTTP proxy server entered conforms to the standard")
		else:
			tipUse()
			exit()
			
	
	def useProxy(self,proxy):
		# Use the agent to visit Baidu,and find keywords
		protocol = proxy.split('//')[0].replace(':','')
		ip = proxy.split('//')[1]
		opener = urllib2.build_opener(urllib2.ProxyHandler({protocol:ip}))
		urllib2.install_opener(opener)
		try:
			response = urllib2.urlopen(self.url,timeout=self.timeout)
		except:
			print("connection error,exiting program")
			exit()
		str = response.read()
		if re.search(self.flagWord,str):
			print("A feature word has been obtained that the agent is available")
		else:
			print("The agent is not available")
			
if __name__ == '__main__':
	testArgument()
		
