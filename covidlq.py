def covid19(arr,n):
    flag=False
    for i in range(n):
        if arr[i]==1:
            if not flag:
                flag=True
                left=i
                continue
            if (i-left)<6:
                return False
            else:
                left=i 
    return True
    
t=int(input())
for loop in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if covid19(arr,n):
        print("YES")
    else:
        print("NO")
