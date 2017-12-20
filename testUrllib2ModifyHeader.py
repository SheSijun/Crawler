import urllib2
import userAgents
# userAgents is a coustom module with a location in the current directory

class Urllib2ModifyHeader(object):
	# modifying headers using the URLLIB2 module
	def __init__(self):
		# this is PC + IE User-Agent
		PIUA = userAgents.pcUserAgent.get('IE 9.0')
		# this User-Agent is for Mobile + UC
		MUUA = userAgents.mobileUserAgent.get('UC standard')
		# Test Site selected is Youdao translation
		self.url = 'http://fanyi.youdao.com'
		
		self.useUserAgent(PIUA,1)
		self.useUserAgent(MUUA,2)
		
	def useUserAgent(self,userAgent,name):
		request = urllib2.Request(self.url)
		request.add_header(userAgent.split(':')[0],userAgent.split(':')[1])
		response = urllib2.urlopen(request)
		fileName = str(name) + '.html'
		with open(fileName,'a') as fp:
			fp.write("%s\n\n" %userAgent)
			fp.write(response.read())
			
if __name__ == '__main__':
	umh = Urllib2ModifyHeader()
