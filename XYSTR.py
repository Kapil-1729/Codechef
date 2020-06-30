def solve():
    result=0
    arr=input()
    i=0
    while(i<len(arr)-1):
        if arr[i]!=arr[i+1]:
            i+=2
            result+=1 
        else:
            i+=1
    print(result)
    
t=int(input())
for loop in range(t):
    solve()
