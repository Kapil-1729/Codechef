def solve():
    n,p = map(int,input().split())
    a=[[0 for i in range(n)] for i in range(n)]
    print(1,1,1,n,n)
    total=int(input())
    counter=0
    for i in range(n):
        print(1,i+1,1,i+1,n)
        num=int(input())
        counter+=num
        if num==n:
            for j in range(n):
                a[i][j]=1 
        elif num!=0:
            c=0
            if n%2==1:
                print(1,i+1,n,i+1,n)
                a[i][n-1]=int(input())
            for j in range(0,n,2):
                print(1,i+1,j+1,i+1,j+2)
                num1=int(input())
                c+=num1
                if num1==1:
                    print(1,i+1,j+1,i+1,j+1)
                    a[i][j]=int(input())
                    a[i][j+1]=1-a[i][j]
                elif num1==2:
                    a[i][j]=1 
                    a[i][j+1]=1 
                if c==num:
                    break
        if counter==total:
            break
    print(2)
    for i in range(n):
        print(*a[i])
    x=int(input())
    if x==-1:
        return
t=int(input())
for loop in range(t):
    solve()
