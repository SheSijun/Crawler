import urllib2

def clear():
	# This function is used to clear the screen
	print("More content,show 3 seconds to page")
	time.sleep(3)
	OS = platform.system()
	if (OS == 'Windows'):
		os.system('cls')
	else:
		os.system('clear')
		
def linkBaidu():
	url = 'http://www.baidu.com'
	try:
		response = urllib2.urlopen(url,timeout=3)
	except urllib2.URLError:
		print("Network address Error")
		exit()
	with open('./baidu.txt','w') as fp:
		fp.write(response.read())
	print("Get URL Information,response.geturl() \n: %s" %response.geturl())
	print("Get return code,response.getcode() \n: %s" %response.getcode())
	print("Get return information,response.info() \n: %s" %response.info())
	print("The content of the Web page has been stored in the baidu.txt of the current directory,please view it yourself")
	
if __name__ == '__main__':
	linkBaidu()
	
