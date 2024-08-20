import math
t=int(input())
for i in range(t):
    n,time=input().split()
    n,time=int(n),int(time)
    array1=[int(value) for value in input().split()]
    array2=[int(value) for value in input().split()]
    array=[]
    for i in range(n):
        array.append((array1[i],array2[i]))
    left,right,best=1,max(array1),-1
    while left<=right:
        mid=(left+right)//2
        result=0
        for (key,value) in array:
            result+=math.ceil(key/mid)*value
        if result<=time:
            best=mid
            right=mid-1
        else:
            left=mid+1
    print(best)
    




