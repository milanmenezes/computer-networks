import copy
ip=raw_input("Enter IP\n")
n=0
classfull=True
if "/" in ip:
	classfull=False
	ip=ip.split("/")
	n=eval(ip[1])
	ip=ip[0]

ip=ip.split(".")
flag=True

if len(ip)!=4:
	flag=False
	print "Invalid IP"
else:
	try:
		for i in ip:
			if (not(0 <= int(i) and int(i)<= 255)):
				flag=False
		if flag:
			print "Valid IP"
		else:
			print "Invalid IP"
	except:
		flag=False
		print "Invalid IP"

if flag:
	if (ip[0]=='0' and ip[1]=='0' and ip[2]=='0' and ip[3]=='0' and classfull):
		print "Special Address: This Address"

	elif(ip[0]=='127'and classfull):
		print "Special Address: Loop Back Address"

	# checking private address
	elif(ip[0]=='10' and classfull):
		print "Class A: Private Address"

	elif(ip[0]=="172" and (16<=eval(ip[1])<=31) and classfull):
		print "Class B: Private Address"

	elif(ip[0]=='192' and ip[1]=='168' and classfull):
		print "Class A: Private Address"

	else:
		if classfull:
			print "Classfull address"
			if eval(ip[3])<126:
				print "Class A"
			elif eval(ip[3])<191:
				print "Class B"
			elif eval(ip[3])<223:
				print "Class C"
		else:
			print "Classless address"
			mask=""
			l=[]
			for i in range(n):
				mask=mask+"1"
			for i in range(32-n):
				mask=mask+"0"
			print "Subnet mask is: ",
			for i in range(0,32,8):
				 l.append(str(eval("0b"+mask[i:i+8])))
			print ".".join(l)

			netid=[]
			for i in range(4):
				netid.append(str(eval(l[i]) & eval(ip[i])))
			print "NetId: ",".".join(netid)
			bid=[]
			for i in range(4):
				bid.append(str(((~eval(l[i])) | eval(ip[i])) & 0xff))
			#anded with 0xff to convert from signed negative value to unsigned

			print "BroadcastId: ",".".join(bid)

			range1=copy.copy(netid)
			range2=copy.copy(bid)
			
			#first address
			if(netid[3]=='255'):
				if(netid[2]=='255'):
					if(netid=='255'):
						range1[0]=str(eval(range1[0])+1)
					else:
						range1[1]=str(eval(range1[1])+1)
				else:
					range1[2]=str(eval(range1[2])+1)
			else:
				range1[3]=str(eval(range1[3])+1)

			#last address
			if(bid[3]=='0'):
				if(bid[2]=='0'):
					if(bid=='0'):
						range2[0]=str(eval(range2[0])-1)
					else:
						range2[1]=str(eval(range2[1])-1)
				else:
					range2[2]=str(eval(range2[2])-1)
			else:
				range2[3]=str(eval(range2[3])-1)

			print "Range:",".".join(range1),"to",".".join(range2)
