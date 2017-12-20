import logging
import getpass
import sys

class MyLog(object):
	# This class is used to create a log 
	def __init__(self):
		user = getpass.getuser()
		self.logger = logging.getLogger(user)
		self.logger.setLevel(logging.DEBUG)
		# Log file name
		logFile = './' + sys.argv[0][0:-3] + '.log'
		formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')
		
		# Logs are displayed to the screen and exported to the log file
		logHand = logging.FileHandler(logFile)
		logHand.setFormatter(formatter)
		logHand.setLevel(logging.ERROR)
		
		logHandSt = logging.StreamHandler()
		logHandSt.setFormatter(formatter)
		
		self.logger.addHandler(logHand)
		self.logger.addHandler(logHandSt)
		
		
	# The 5 levels of the log correspond to the following 5 functions
	def debug(self,msg):
		self.logger.debug(msg)
		
	def info(self,msg):
		self.logger.info(msg)
		
	def warn(self,msg):
		self.logger.warn(msg)
		
	def error(self,msg):
		self.logger.error(msg)
		
	def critical(self,msg):
		self.logger.critical(msg)
		
if __name__ == '__main__':
	mylog = MyLog()
	mylog.debug("I'm debug")
	mylog.info("I'm info")
	mylog.warn("I'm warn")
	mylog.error("I'm error")
	mylog.critical("I'm critical")
		
