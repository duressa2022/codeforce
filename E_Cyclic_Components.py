from collections import defaultdict
def formGraph():
    n,m=list(map(int,input().split()))
    graph=defaultdict(list)
    for _ in range(m):
        u,v=list(map(int,input().split()))
        graph[u].append(v)
        graph[v].append(u)
    return graph
def solver():
    graph=formGraph()
    visted=set()
    def helper(graph,node):
        stack=[node]
        degree=set()
        visted.add(node)
        while stack:
            cur=stack.pop()
            counter=0
            for neighbor in graph[cur]:
                if neighbor not in visted:
                    stack.append(neighbor)
                    visted.add(neighbor)
                counter+=1
            degree.add(counter)
        return True if len(degree)==1 and 2 in degree else False
    result=0
    for node in graph:
        if node in visted:
            continue
        if helper(graph,node):
            result+=1
    return result
print(solver())

                    




