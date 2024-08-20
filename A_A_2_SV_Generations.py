n=int(input())
nums=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        k=abs(nums[i]-nums[j])
        
