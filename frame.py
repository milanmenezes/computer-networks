import random
import operator
class ippac():
        def __init__(self,src,dst,msg):
                self.id=random.randint(1,10000)
		self.src=src
		self.dst=dst
		self.mlen=len(msg)
		self.msg=msg

	def __str__(self):
		return "\nPacket ID: "+str(self.id)+"\nSource: "+self.src+"\nDestination: "+self.dst+"\nMessage Length: "+str(self.mlen)+"\nMessage: "+self.msg+"\n\n\n"

l=[]
while(True):
	x=eval(raw_input("Enter 1 to create a frame\n2 to display\n3 to sort\n4 to exit\n"))
	if(x==1):
		src=raw_input("\n\nEnter Source\n")
		dst=raw_input("Enter Destination\n")
		msg=raw_input("Enter Message\n")
		obj=ippac(src,dst,msg)
		l.append(obj)

	elif(x==2):
		for i in l:
			print i

	elif(x==3):
		l=sorted(l,key=lambda i:i.id)

	else:
		break

		

