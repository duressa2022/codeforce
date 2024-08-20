n = int(input())
nums = list(map(int,input().split()))

result = [0]*n

nums.sort()

k = n-1
for i in range(1, n, 2):
    result[i] = nums[k]
    k-= 1

for i in range(0, n, 2):
    result[i] = nums[k]
    k-= 1

print(*result)