def carsell(arr,n):
    count0=0 
    profit=0 
    arr.sort(reverse=True)
    for i in range(n):
        if (arr[i]-i)<=0:
            break
        profit+=(arr[i]-i)
    print(profit%1000000007)
    
t=int(input())
for loop in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    carsell(arr,n)
