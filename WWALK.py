def solve():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sum1=[0]*(n+1)
    sum2=[0]*(n+1)
    sum1[0]=0
    sum2[0]=0
    result=0
    for i in range(n):
        sum1[i+1] = a[i]+sum1[i]
        sum2[i+1] = b[i]+sum2[i]
        if sum1[i+1]==sum2[i+1] and sum1[i]==sum2[i]:
            result+=(sum1[i+1]-sum1[i])
    print(result)

t=int(input())
for loop in range(t):
    solve()
