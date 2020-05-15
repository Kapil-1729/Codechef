t=int(input())
for loop in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    r1=abs(sum(arr[k:])-sum(arr[:k]))
    r2=abs(sum(arr[n-k:])-sum(arr[:n-k]))
    result=max(r1,r2)
    print(str(result))
