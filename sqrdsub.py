def sqsub():
    n=int(input())
    arr=list(map(int,input().split()))
    counter=0
    sums=0
    nums=[]
    for element in arr:
        if element%4==0:
            nums.append(2)
        elif element%4==2:
            nums.append(1)
        else:
            nums.append(0)
    d={}
    d[0]=1 
    for num in nums:
        sums+=num 
        if sums-1 in d:
            counter+=(d[sums-1])
        if sums in d:
            d[sums]+=1 
        else:
            d[sums]=1 
    print ((n*(n+1)//2)-counter)

t=int(input())
for loop in range(t):
    sqsub()
