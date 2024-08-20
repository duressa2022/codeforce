n=int(input())
nums=list(map(int,input().split()))
ans=[]
for i in range(n-1):
    ans.append(nums[i]+nums[i+1])
ans.append(nums[-1])
print(*ans)