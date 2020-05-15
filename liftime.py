def lift():
    n,q=map(int,input().split())
    current=0
    result=0
    for i in range(q):
        fi,fd=map(int,input().split())
        result+=abs(current-fi)
        result+=abs(fi-fd)
        current=fd
    print(result)

t=int(input())
for loop in range(t):
    lift()
