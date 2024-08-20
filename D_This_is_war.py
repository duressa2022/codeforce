from collections import Counter
for _ in range(int(input())):
    n=int(input())
    nums=list(reversed(sorted([(num,index+1) for index,num in enumerate(list(map(int,input().split())))])))
    tokens=[]
    for key,value in nums:
        tokens.append(key)
    counter=Counter(tokens)
    left,right=0,1
    res=[]
    best=0
    while right<n:
        if nums[left][0]>nums[right][0]:
            res.append(nums[left][1])
            best=nums[left][0]
            left=left+1
            right=right+1
        else:
            if nums[left][0]*counter[nums[left][0]]>=best:
                res.append(nums[left][1])
                best=nums[left][0]*counter[nums[left][0]]
            left=left+1
            right=right+1
    if nums[-1][0]*counter[nums[-1][0]]>=best:
        res.append(nums[-1][1])
    res.sort()
    print(len(res))
    print(*res)



