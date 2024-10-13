def solver(nums,l,r,k):
    valid=[cost for cost in nums if l<=cost<=r]
    valid.sort()

    counter=0
    current=0
    for cost in valid:
        if current+cost<=k:
            current=current+cost
            counter=counter+1
        else:
            break
    return counter

for _ in range(int(input())):
    _,l,r,k=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    ans=solver(nums,l,r,k)
    print(ans)
