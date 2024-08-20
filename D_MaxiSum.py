n,q=input().split()
n,q=int(n),int(q)
array=[int(num) for num in input().split()]
tempArray=[0]*(n+1)
for i in range(q):
    [left,right]=input().split()
    left,right=int(left),int(right)
    tempArray[left-1]+=1
    tempArray[right]-=1
running=0
for i in range(len(tempArray)):
    running+=tempArray[i]
    tempArray[i]=running
tempArray.sort(reverse=True)
array.sort(reverse=True)
result=0
for i in range(n):
    result+=tempArray[i]*array[i]
print(result)

