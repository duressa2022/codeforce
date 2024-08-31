from collections import Counter
n=int(input())
nums=list(map(int,input().split()))
counter=Counter(nums)
def func(n):
    if n==0 or n==1:
        return 1
    else:
        return n*func(n-1)
ans=func(len(counter))
print(ans)