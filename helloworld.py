import time
import os.path

def warnlongtimenosave() ;
	lastmodified = os.path.getmtime("helloWorld.py")
	elapsed = time.time() - lastmodified
	# print (elapsed)
	if elapsed > 5 :
		print("OLD FILE DID YOU SAVE %s") % time.ctime(lastmodified)
 
 warnlongtimenosave()
 