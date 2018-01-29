import copy
x=[eval(i) for i in raw_input("Enter the bits\n")]
y=[1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1]
l1=copy.copy(x)
for i in range(33):
	l1.append(0)

def crc32(l1,y):
	for i in range(len(l1)-32):
		if(l1[i]==1):
			for j in range(len(y)):
				l1[i+j]=(l1[i+j]+y[j])%2
	return x[-32:]

rem=crc32(l1,y)
enc=copy.copy(x)
enc.extend(rem)
rem=[str(i) for i in rem]
enc=[str(i) for i in enc]
print "Reminder: ","".join(rem)
print "Encoded message: ","".join(enc)

