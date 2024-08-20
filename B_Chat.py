from heapq import *
def solver():
    n,k,q=list(map(int,input().split()))
    test=list(map(int,input().split()))
    heap=[]
    screen=set()
    for _ in range(q):
        id,value=list(map(int,input().split()))
        if id==1:
            if len(heap)<k:
                heappush(heap,(test[value-1],value,id))
                screen.add(value)
            else:
                t,v,i=heappop(heap)
                screen.discard(v)
                if t<test[value-1]:
                    heappush(heap,(test[value-1],value,id))
                    screen.add(value)
                else:
                    heappush(heap,(t,v,i))
                    screen.add(v)
        else:
            if value in screen:
                print("YES")
            else:
                print("NO")
solver()
            
