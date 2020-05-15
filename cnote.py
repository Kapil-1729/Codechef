# X page long poetry
# Y pages left in notebook
# Total pages required = X-Y
# Balance = K rubles
# P>=X-Y and K>=C

t=int(input())

for loop in range(t):

    x,y,k,n=map(int,input().split())
    flag=0

    for i in range(n):

        p,c=map(int,input().split())

        if((p>=x-y)and(k>=c)):
            flag+=1

    if (flag==0):
        print("UnluckyChef\n")
    else:
        print("LuckyChef\n")
