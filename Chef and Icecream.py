def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    five=0
    ten=0
    fifteen=0
    for a in arr:
        if a==5:
            five+=1 
        elif a==10:
            if five>0:
                five-=1 
                ten+=1 
            else:
                return "NO"
        elif a==15:
            if ten>0:
                ten-=1 
                fifteen+=1 
            elif five>=2:
                five-=2
                fifteen+=1 
            else:
                return "NO"
    return "YES"
    
t=int(input())
for loop in range(t):
    print(solve())
