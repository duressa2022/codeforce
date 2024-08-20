n,s=list(map(int,input().split()))
import sys, threading
sys.setrecursionlimit(1000)

def solver(n,s):
    if n==1 and s==0:
        return (0,0)
    if s==0:
        return (-1,-1)
    
    max_digits=[0 for i in range(n)]
    for i in range(n):
        current=min(9,s)
        max_digits[i]+=current
        s=s-current
    if s:
        return (-1,-1)
    min_digits=max_digits[::-1]

    for i in range(n):
        if min_digits[i]!=0:
            min_digits[i]-=1
            min_digits[0]+=1
            break
    maxResult="".join([str(num) for num in max_digits])
    minResult="".join([str(num) for num in min_digits])
    return (int(minResult),int(maxResult))
min,max=solver(n,s)
print(min,max)
    

        

