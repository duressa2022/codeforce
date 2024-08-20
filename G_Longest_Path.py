from collections import defaultdict,deque
def mainFunction():
    graph=defaultdict(list)
    n,m=list(map(int,input().split()))
    for _ in range(m):
        u,v=list(map(int,input().split()))
        graph[u].append(v)
    def solver(graph,node,n):
        distance={node:0 for node in range(1,n+1)}
        visted=set()
        queue=deque([(node,0)])
        while queue:
            cur,dis=queue.popleft()
            if cur in visted:
                continue
            visted.add(cur)

            for neighbor in graph[cur]:
                if neighbor not in visted:
                    distance[neighbor]=max(distance[neighbor],dis+1)
                    queue.append((neighbor,dis+1))
        return distance
    distances={}
    for node in range(1,n+1):
            distances[node]=solver(graph,node,n)
    ans=0
    for node in range(1,n+1):
         ans=max(ans,max(distances[node].values()))
    print(ans)
mainFunction()


