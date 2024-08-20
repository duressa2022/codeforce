def solver(n,k):
    left,right,best,k=1,n,0,4*60-k
    while left<=right:
        mid=(left+right)//2
        current=0
        for index in range(1,mid+1):
            current+=5*index
        if current<=k:
            best=mid
            left=mid+1
        else:
            right=mid-1
    return best
n,k=list(map(int,input().split()))
print(solver(n,k))

