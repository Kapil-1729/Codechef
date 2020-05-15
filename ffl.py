def solve():
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    temp=list(map(int,input().split()))
    min0=101 
    min1=101
    for i in range(n):
        if temp[i]==0:
            min0=min(min0,arr[i])
        else:
            min1=min(min1,arr[i])
    if (s+min0+min1)<=100:
        print("yes")
    else:
        print("no")

t=int(input())
for loop in range(t):
    solve()
