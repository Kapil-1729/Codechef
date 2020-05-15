t=int(input())
for loop in range(t):
	n=int(input())
	marks=list(map(int,input().split()))
	if((5 in marks)and(2 not in marks)and(sum(marks)/n>=4.0)):
		print("Yes")
	else:
		print("No")
