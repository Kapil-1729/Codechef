def sticks():
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    i=0
    counter=0
    result=1
    while(i<n-1):
        if counter == 2:
            break
        if arr[i]==arr[i+1]:
            result*=arr[i]
            counter+=1 
            i+=2
        else:
            i+=1 
    if counter<2:
        return (-1)
    return(result)
    
    
t=int(input())
for loop in range(t):
    print(sticks())
