def solve():
    n=int(input())
    mat = [[0 for i in range(n)] for i in range(n)]
    i=0
    j=0
    k=1 
    temp=n 
    m=n
    while i<n or j<m:
        
        if i<n:
            for p in range(j,m):
                mat[i][p]=k 
                k+=1 
            i+=1 
        
        if j<m:
            for p in range(i,n):
                mat[p][m-1]=k 
                k+=1 
            m-=1 
            
        if i<n:
            for p in range(m-1,j-1,-1):
                mat[n-1][p]=k 
                k+=1 
            n-=1 
        
        if j<m:
            for p in range(n-1,i-1,-1):
                mat[p][j]=k 
                k+=1 
            j+=1 
    for i in range(temp):
        print(*mat[i])

t=int(input())
for loop in range(t):
    solve()
