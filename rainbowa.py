t=int(input());

for loop in range(t):

    n=int(input())
    a=list(map(int,input().split()))

    mid=(n-1)//2

    i=1
    j=n-2
    flag=True

    if((a[0]!=1)or(a[n-1]!=1)or(a[mid]!=7)):
        flag=False

    for k in range(n):
        if((a[k]>7)or(a[k]<=0)):
            flag=False

    if flag==False:
        print("no")
        continue

    else:
        while(i<=j):

            if(a[i]!=a[j]):
                flag=False
                break

            if (((a[i]-a[i-1])!=0)and(a[i]-a[i-1])!=1):
                flag=False
                break

            i+=1
            j-=1

        if flag:
            print("yes")
        else:
            print("no")
