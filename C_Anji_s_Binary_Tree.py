from collections import defaultdict
def formGraph():
    graph=defaultdict(list)
    leaf=set()
    length=int(input())
    Dir=input()
    for node in range(1,length+1):
        left,right=list(map(int,input().split()))
        if left and right:
            if Dir[node-1]=="L":
                graph[node].append((left,0))
                graph[node].append((right,1))
            elif Dir[node-1]=="R":
                graph[node].append((right,0))
                graph[node].append((left,1))
            else:
                graph[node].append((right,1))
                graph[node].append((left,1))
        elif left and not right:
            if Dir[node-1]=="L":
                graph[node].append((left,0))
            elif Dir[node-1]=="R":
                graph[node].append((left,1))
            else:
                graph[node].append((left,1))
        elif not left and right:
            if Dir[node-1]=="R":
                graph[node].append((right,0))
            elif Dir[node-1]=="L":
                graph[node].append((right,1))
            else:
                graph[node].append((right,1))
        else:
            leaf.add(node)
    return graph,leaf
def solver():
    graph,leaf=formGraph()
    stack=[(1,0)]
    length=float("inf")
    while stack:
        cur,weight=stack.pop()
        if cur in leaf:
            length=min(length,weight)
        
        for neighbor,other in graph[cur]:
            stack.append((neighbor,weight+other))
    print(length)
for _ in range(int(input())):
    solver()


















        
        