from math import *

def solve():
    n=int(input())
    if n%2==1:
        return n//2 
    else:
        op=int(log2(n&-n))+1 
        temp=2**op
        return int(n//temp)

t=int(input())
for loop in range(t):
    print(solve())
