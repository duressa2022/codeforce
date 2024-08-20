from heapq import *
from collections import defaultdict
def solver():
    n,m=list(map(int,input().split()))
    graph=defaultdict(list)
    indegree=[0 for i in range(n)]
    for i in range(m):
        u,v=list(map(int,input().split()))
        graph[u].append(v)
        indegree[v-1]+=1
    queue=[]
    for node in range(1,n+1):
        if indegree[node-1]==0:
            queue.append(node)
    result=[]
    while queue:
        cur=heappop(queue)
        result.append(cur)

        for neighbor in graph[cur]:
            indegree[neighbor-1]-=1
            if indegree[neighbor-1]==0:
                heappush(queue,neighbor)
    if len(result)!=n:
        print(-1)
        return 
    print(*result)
solver()

            
