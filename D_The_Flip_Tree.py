from collections import defaultdict,deque
m=int(input())
def formGraph():
    graph=defaultdict(list)
    for _ in range(m-1):
        u,v=list(map(int,input().split()))
        graph[v].append(u)
        graph[u].append(v)
    return graph
graph=formGraph()
def solver(graph):
    incorrect=list(map(int,input().split()))
    correct=list(map(int,input().split()))
    result=[]
    stack=[(1,1,0,0,0)]
    while stack:
        node,par,oddCount,evenCount,level=stack.pop()
        if level%2==0:
            if evenCount%2==0:
                if correct[node-1]!=incorrect[node-1]:
                    result.append(node)
                    evenCount=1-oddCount
            else:
                if 1-incorrect[node-1]!=correct[node-1]:
                    result.append(node)
                    evenCount=1-evenCount
        else:
            if oddCount%2==0:
                if correct[node-1]!=incorrect[node-1]:
                    result.append(node)
                    oddCount=1-oddCount
            else:
                if 1-incorrect[node-1]!=correct[node]:
                    result.append(node)
                    oddCount=1-oddCount
        for neighbor in graph[node]:
            if neighbor!=par:
                stack.append((neighbor,node,oddCount,evenCount,level+1))
    return result


result=solver(graph)
print(len(result))
for node in result:
    print(node)

