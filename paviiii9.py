l,m11=map(int,input().split())
c11=0
for i in range(l,m11+1):
	for j in range(2,i):
		if i%j==0:
			break
	else:
	    c11=c11+1
print(c11)
#i
