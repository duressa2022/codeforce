from collections import defaultdict,deque
def bulidGraph():
    graph=defaultdict(list)
    length=int(input())
    for _ in range(length-1):
        u,v,cost=list(map(int,input().split()))
        graph[u].append((v,cost))
        graph[v].append((u,cost))
    return graph
def solver():
    graph=bulidGraph()
    queue=deque([(0,0)])
    maxresult=-float("inf")
    visted=set()
    while queue:
        node,cur=queue.popleft()
        maxresult=max(cur,maxresult)

        for neighbor,weight in graph[node]:
            if (node,neighbor) not in visted or (neighbor,node) not in visted:
                queue.append((neighbor,weight+cur))
                visted.add((node,neighbor))
                visted.add((neighbor,node))
    return maxresult
print(solver())
        
