n = int(raw_input("Enter the cost of the matrix\n"))
m = []

for i in range(n):
	l=[eval(i) for i in raw_input().split()]
	m.append(l)

d = m[0]

for i in range (1,n):
	c = m[i]
	for j in range(n):
		if i == j:
			continue
		if d[j] > d[i] + c[j]:
			d[j] = d[i]+c[j]


print "Shortest distance vector = ", d


