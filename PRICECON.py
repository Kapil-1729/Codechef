def solve():
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    result=0
    for a in arr:
        if a>k:
            result+=(a-k)
    return result
    
t=int(input())
for loop in range(t):
    print(solve())
