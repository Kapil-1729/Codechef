def price():
    p=int(input())
    result=0
    pow=2048
    while(p>0):
        result+=(p//pow)
        p=p%pow
        pow=int(pow/2)
    print(result)

t=int(input())
for loop in range(t):
    price()
