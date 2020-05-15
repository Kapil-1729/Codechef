def chopstick():
    l=[]
    n,d=map(int,input().split())
    for j in range(n):
       l.append(int(input()))
    l.sort()
    i=0
    result=0
    while(i<n):
        if i==n-1:
            i+=1 
            continue
        if (l[i+1]-l[i])<=d:
            result+=1 
            i+=2
        else:
            i+=1
    print(result)

chopstick()
