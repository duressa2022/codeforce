
for _ in range(int(input())):
    length=int(input())
    nums = list(map(int, input().split()))
    result="YES"
    leftMin = nums[0]
    for i in range(1,length-1):
        if leftMin<nums[i]>nums[i+1]:
            result="NO"
            break
        leftMin=min(leftMin,nums[i])
    print(result)