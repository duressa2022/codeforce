from collections import deque,defaultdict
def bfs(graph,start,end):
    path={node:node for node in graph}
    path[start]=None
    queue=deque([start])
    visted=set()
    while queue:
        cur=queue.popleft()
        visted.add(cur)
        if cur==end:
            result=[]
            while cur!=None:
                result.append(cur)
                cur=path[cur]
            return result[::-1]
        for neighbor in graph[cur]:
            if neighbor not in visted:
                path[neighbor]=cur
                queue.append(neighbor)
    return []

v,e=list(map(int,input().split()))
start,end=list(map(int,input().split()))
edgelist=[]
for i in range(v):
    edgelist.append(list(map(int,input().split())))
graph=defaultdict(list)
for u,v in edgelist:
    graph[u].append(v)
    graph[v].append(u)
print(bfs(graph,start,end))


        
