from collections import defaultdict,deque

def ssolver():
    n,m=list(map(int,input().split()))
    def formGraph():
        graph=defaultdict(list)
        for _ in range(m):
            u,v=list(map(int,input().split()))
            graph[u].append(v)
            graph[v].append(u)
        return graph
    result=[]
    def solver1(graph,start):
        visted=set()
        queue=deque([start])
        visted=set()
        while queue:
            cur=queue.popleft()
            visted.add(cur)
            counter=0
            for neighbor in graph[cur]:
                if neighbor not in visted:
                    queue.append(neighbor)
                counter+=1
            length=len(queue)
            result.append(counter)
            
    graph=formGraph()
    solver1(graph,1)
    maxValue=max(result)
    minValue=min(result)
    result=set(result)
    
    if maxValue==2 and minValue==1 and len(result)==2:
        print("bus topology")
    elif maxValue==2 and len(result)==1:
        print("ring topology")
    elif maxValue==m and minValue==1 and len(result)==2:
        print("star topology")
    else:
        print("unknown topology")
ssolver()

