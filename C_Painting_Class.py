from collections import defaultdict,deque
def buildGraph():
    graph=defaultdict(list)
    length=int(input())
    array=list(map(int,input().split()))
    for node in range(2,length+1):
        graph[array[node-2]].append(node)
    return graph
def solver():
    graph=buildGraph()
    color=list(map(int,input().split()))
    queue=deque([(1,0)])
    counter=0
    while queue:
        node,cur=queue.popleft()
        if color[node-1]!=cur:
            counter+=1
        for neighbor in graph[node]:
            queue.append((neighbor,color[node-1]))
    return counter
print(solver())

