from sys import stdin, stdout 
def unit_gcd(n):
    l=[]
    if n<=3:
        l.append([i for i in range(1,n+1)])
        return l
        
    if n<=5:
        l.append([i for i in range(1,4)])
        l.append([i for i in range(4,n+1)])
        return l

    if n%2 == 0:
        for i in range(1,n+1,2):
            l.append([i,i+1])
        return l

    l.append([i for i in range(1,4)])
    l.append([i for i in range(4,6)])
    for i in range(6,n+1,2):
        l.append([i,i+1])
    return l

t=int(input())
for loop in range(t):
    n=int(input())
    x=unit_gcd(n)
    print(len(x))
    for element in x:
        stdout.write(str(len(element))+" "+" ".join(map(str,element))+'\n')
