from collections import deque,defaultdict
def solver():
    n,m=list(map(int,input().split()))
    a,b=list(map(int,input().split()))
    graph=defaultdict(list)
    for _ in range(m):
        u,v=list(map(int,input().split()))
        graph[u].append(v)
        graph[v].append(u)

    path={node:None for node in range(1,n+1)}
    queue=deque([(a,0)])
    visted=set()
    while queue:
        cur,distance=queue.popleft()
        if cur==b:
            paths=[]
            while path[cur]:
                paths.append(cur)
                cur=path[cur]
            paths.append(cur)
            return distance,reversed(paths)
        visted.add(cur)
        for neighbor in graph[cur]:
            if neighbor not in visted:
                queue.append((neighbor,distance+1))
                path[neighbor]=cur
    return -1,[]
ans=solver()
print(ans[0])
print(*ans[1])




