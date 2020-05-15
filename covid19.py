def solve():
    
    n=int(input())
    arr=list(map(int,input().split()))
    minimum=n
    maximum=0
    d={}
    for k in arr:
        d[k]=[]
    
    for i in range(n):
        
        if i == 0:
            for j in range(i,n-1):
                temp=abs(arr[j]-arr[j+1])
                if temp<=2:
                    d[arr[i]].append(arr[j+1])
                else:
                    break
        
        elif i==n-1:
            for j in range(i,0,-1):
                temp=abs(arr[j]-arr[j-1])
                if temp<=2:
                    d[arr[i]].append(arr[j-1])
                else:
                    break
        
        else:
            for j in range(i,0,-1):
                temp=abs(arr[j]-arr[j-1])
                if temp<=2:
                    d[arr[i]].append(arr[j-1])
                else:
                    break
                     
        
            for j in range(i,n-1):
                temp=abs(arr[j+1]-arr[j])
                if temp<=2:
                    d[arr[i]].append(arr[j+1])
                else:
                    break
    
    for k in d:
        maximum=max(maximum,len(d[k]))
        minimum=min(minimum,len(d[k]))
    
    print(minimum+1,maximum+1)
        
    
t=int(input())
for loop in range(t):
    solve()
