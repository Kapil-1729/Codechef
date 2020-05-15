from sys import stdin, stdout
def isolation():
    n,q=map(int,stdin.readline().split())
    s=input()
    d={}
    for k in s:
        if k in d:
            d[k]+=1 
                
        else:
            d[k]=1
            
    for i in range(q):
        c=int(stdin.readline())
        result=0
        for k in d:
            if d[k]>c:
                result+=(d[k]-c)
                
        stdout.write(str(result)+'\n')
                
t=int(stdin.readline())
for loop in range(t):
    isolation()
