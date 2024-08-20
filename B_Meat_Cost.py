array=[]
length=int(input())
for i in range(length):
    amount,cost=input().split()
    amount=int(amount)
    cost=int(cost)
    array.append([amount,cost])
cost=array[0][0]*array[0][1]
minCost=array[0][1]
for i in range(1,length):
    if array[i][1]<minCost:
        minCost=array[i][1]
        cost+=array[i][0]*minCost
    else:
        cost+=array[i][0]*minCost
print(cost)
