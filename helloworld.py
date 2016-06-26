import time
import os.path

def warnlongtimenosave() :
	lastmodified = os.path.getmtime("helloWorld.py")
	elapsed = time.time() - lastmodified
	# print (elapsed)
	if elapsed > 5 :
		print("OLD FILE DID YOU SAVE %s") % time.ctime(lastmodified)
 
warnlongtimenosave()

def sqrt(a, n) :
	xn = 1.0
	i = 1
	while i <= n :
		xn = (xn + a / xn ) / 2
		print(xn)
		i = i + 1
	return xn

print(sqrt(5,100))
