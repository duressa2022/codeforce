import heapq
def solver():
    length=int(input())
    array=list(map(int,input().split()))
    heap=[]
    for i,value in enumerate(array):
        if value!=0:
            heap.append((-value,-1))
    heapq.heapify(heap)
    result=[]
    while len(heap)>=2:
        value1,i=heapq.heappop(heap)
        value2,j=heapq.heappop(heap)
        result.append((i,j))
        value1,value2=-value1,-value2
        if value1-1>0:
            heapq.heappush(heap,(-value1+1,i))
        if value2-1>0:
            heapq.heappush(heap,(-value2+1,j))
    print(len(result))
    for i,j in result:
        print(i,j)
for _ in range(int(input())):
    solver()