from collections import deque
n,m=list(map(int,input().split()))
nums=list(map(int,input().split()))
queue=deque([])
for index,num in enumerate(nums):
    queue.append((index,num))
while len(queue)>1:
    index,cur=queue.popleft()
    if cur>m:
        queue.append((index,cur-m))
    else:
        continue
index,_=queue.pop()
print(index+1)
    


