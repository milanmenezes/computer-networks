ip=raw_input("Enter IP\n")
ip=ip.split(".")
flag=True
if len(ip)!=4:
	print "Invalid IP"
else:
	try:
		for i in ip:
			if (not(0 < int(i) and int(i)<= 255)):
				flag=False
		if flag:
			print "Valid IP"
		else:
			print "Invalid IP"
	except:
		print "Invalid IP"


