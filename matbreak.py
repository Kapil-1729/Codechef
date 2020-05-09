def fastpower(x,y,p):
    res=1 
    x=x%p 
    if(x==0):
        return 0 
    while(y>0):
        if((y&1)==1):
            res=(res*x)%p 
        y=y>>1 
        x=(x*x)%p 
    return res 

def matrix():
    n,a=map(int,input().split())
    result=0
    power=1
    m=1000000007
    for i in range(n):
        temp=fastpower(a,power,m)
        result=(result+temp)%m
        a=(temp*a)%m
        power+=2
    print(result)

t=int(input())
for loop in range(t):
    matrix()
