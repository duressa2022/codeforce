from collections  import Counter
for _ in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split()))
    counter=Counter(nums)
    ans=-1
    cur=float("inf")
    for index,num in enumerate(nums):
        if counter[num]==1:
            if cur>num:
                cur=num
                ans=index
    print(ans) if ans==-1 else print(ans+1)

