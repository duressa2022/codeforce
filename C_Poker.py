from heapq import *
def solver():
    length=int(input())
    array=list(map(int,input().split()))
    heap=[]
    result=0
    for num in array:
        if num>0:
            heappush(heap,-num)
        else:
            if heap:
                result+=-1*heappop(heap)
    return result
for _ in range(int(input())):
    print(solver())
