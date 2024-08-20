from math import gcd
def solver():
    n,k=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    for i in range(n):
        nums[i]-=k
    greater_zero=0
    lessthan_zero=0
    equal_zero=0
    for num in nums:
        if num>0:
            greater_zero+=1
        elif num<0:
            lessthan_zero+=1
        else:
            equal_zero+=1
    if greater_zero==n:
        g=nums[0]
        for num in nums[1:]:
            g=gcd(g,num)
        ans=0
        for num in nums:
            ans+=num//g-1
        print(ans)
        return 
    elif lessthan_zero==n:
        g=abs(nums[0])
        for num in nums[1:]:
            g=gcd(g,abs(num))
        ans=0
        for num in nums:
            ans+=abs(num)//g-1
        print(ans)
        return 
    elif equal_zero==n:
        print(0)
        return 
    else:
        print(-1)
for _ in range(int(input())):
    solver()