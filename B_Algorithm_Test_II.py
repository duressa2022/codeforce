def insertAfter(nums,x,y):
    index=-1
    flag=False
    for i in range(len(nums)-1,-1,-1):
        if nums[i]==y:
            flag=True
            index=i
            break
    if not flag:
        nums.append(x)
    else:
        nums.insert(x,index+1)
def removeX(nums,x):
    index=-1
    flag=False
    for i in range(len(nums)-1,-1,-1):
        if nums[i]==x:
            index=i
            flag=True
            break
    if flag:
        nums.remove(x,index)
nums=[]
ops=[]
for _ in range(int(input())):
    ops.append(input())
for op in ops:
    if op[0]=="i":
        _,x,y=op.split()
        insertAfter(nums,int(x),int(y))
    if op[0]=="r":
        _,x=op.split()
        removeX(nums,int(x))
print(*nums)
