n=int(input())
left,right,best=1,10**18,-1
candies=n
half=(n/4)*(n+1)
while left<right:
    mid=(left+right)//2

    calculated=0
    while candies:
        if candies>mid:
            calculated+=min(candies, mid)
            candies=candies-mid
        if candies:
            ten=candies//10
            candies=candies-ten

    
    if calculated>=half:
        best=mid
        right=mid-1
    else:
        left=mid+1
print(best)

