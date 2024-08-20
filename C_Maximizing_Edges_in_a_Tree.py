from collections import defaultdict
def solver(graph):
    def helper(graph,node):
        visted=set()
        set1=set()
        set2=set()
        stack=[(node,True)]
        while stack:
            cur,color=stack.pop()
            visted.add(cur)
            if color==True:
                set1.add(cur)
            else:
                set2.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visted:
                    stack.append((neighbor,not color))
        return [set1,set2]
    return helper(graph,1)
n=int(input())
array=[]
for _ in range(n-1):
    array.append(list(map(int,input().split())))
graph=defaultdict(list)
for u,v in array:
    graph[u].append(v)
    graph[v].append(u)
result=solver(graph)
print(len(result[0])*len(result[1])-(n-1))


  


