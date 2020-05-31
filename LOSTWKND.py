def solve():
    arr=list(map(int,input().split()))
    temp=sum(arr)-arr[-1]
    temp=temp*arr[-1]
    if temp<=120:
        print("No")
    else:
        print("Yes")

t=int(input())
for loop in range(t):
    solve()
