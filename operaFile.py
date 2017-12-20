import os

def operaFile():
	# Create a file
	print(u'Create a file named test.txt and write Hello in it')
	print("First,make sure test.txt doesn't exit.")
	os.system('rm test.txt')
	os.system('ls -l test.txt')
	print('Now to create the file and write the content.\n')
	
	fp = open('test.txt','w')
	fp.write('Hello William,')
	fp.close()
	print("Don't forget to close the file with closing.")
	print("Let's see if test.txt eists, and the content.")
	os.system('ls -l test.txt')
	os.system('cat test.txt')
	print('\n')
	
	print("How to avoid the problem of open file failure?")
	print("Use with As to")
	with open('test.txt','r') as fp:
		st = fp.read()
	print("test.txt content is %s" %st)
	
if __name__ == '__main__':
	operaFile()
