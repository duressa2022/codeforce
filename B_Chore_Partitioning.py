n,a,b,=list(map(int,input().split()))
nums=list(map(int,input().split()))
nums.sort()
ans=nums[-a]-nums[-a-1]
print(ans)