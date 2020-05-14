t=int(input())

for loop in range(t):
	
	nop=0
	n=int(input())
	w=list(map(int,input().split()))
	w.sort()
	
	if(len(w)==2):
		nop=w[1]-w[0]
	else:
		for i in range(1,n):
			nop+=w[i]-w[0]
	
	print(nop)
