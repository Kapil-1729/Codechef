def stones():
    n1,n2,m=map(int,input().split())
    print(max(n1+n2-m*(m+1),abs(n1-n2)))

t=int(input())
for loop in range(t):
    stones()
