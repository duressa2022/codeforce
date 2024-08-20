import heapq
def solver():
    length=int(input())
    array=[]
    for _ in range(length):
        key=input().split()
        if len(key)==2:
            array.append(key)
        else:
            key.append(None)
            array.append(key)
    result=[]
    heap=[]
    for key,value in array:
        if value is not None:
            value=int(value)
        if key=="insert":
            heapq.heappush(heap,value)
            result.append((key,value))
        elif key=="removeMin":
            if heap:
                heapq.heappop(heap)
                result.append((key,None))
            else:
                result.append(("insert",0))
                result.append(("removeMin",None))
        elif key=="getMin":
            while heap and heap[0]<value:
                heapq.heappop(heap)
                result.append(("removeMin",None))
            if not heap or heap[0]>value:
                heapq.heappush(heap,value)
                result.append(("insert",value))
            result.append(("getMin",value))
    print(len(result))
    for i,j in result:
        if j==None:
            print(i)
        else:
            print(i,j)
solver()
