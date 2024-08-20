from collections import defaultdict
def solverFunction():
    graph=defaultdict(list)
    n=int(input())
    if n%2==1:return -1
    for _ in range(n-1):
        u,v=list(map(int,input().split()))
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    visted=[-1 for _ in range(n)]
    lowest=[-1 for _ in range(n)]
    parent=[-1 for _ in range(n)]
    edgelist=[]
    timer=0
    def dfSolver(node):
        nonlocal timer
        visted[node]=timer
        lowest[node]=timer
        timer+=1
        for neighbor in graph[node]:
            if lowest[neighbor]==-1:
                parent[neighbor]=node
                dfSolver(neighbor)
                lowest[node]=min(lowest[node],lowest[neighbor])
                if lowest[neighbor]>lowest[node]:
                    edgelist.append((node,neighbor))
            else:
                if neighbor!=parent[node]:
                    lowest[node]=min(lowest[node],visted[neighbor])
        return None
    dfSolver(0)
    dirtyEdges=len(edgelist)
    return dirtyEdges-n//2
print(solverFunction())

