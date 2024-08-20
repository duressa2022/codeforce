from collections import deque, defaultdict
def ordering(graph, indegree):
    queue = deque()
    for node in range(n):
        if not indegree[node]:
            queue.append(node)
    order = []
    while queue:
        cur = queue.popleft()
        order.append(cur)

        for neighbor in graph[cur]:
            indegree[neighbor] -= 1

            if not indegree[neighbor]:
                queue.append(neighbor)
    return order
def helperFunction():
    n, m = map(int, input().split())
    directed = []
    undirected = []
    for i in range(m):
        direction, x, y = map(int, input().split())
        x -= 1 
        if direction:
            directed.append((x, y))

        else:
            undirected.append((x, y))
    return (n,directed,undirected)
    
for _ in range(int(input())):
    n,directed,undirected=helperFunction()
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for u, v in directed:
        graph[u].append(v)
        indegree[v] += 1
    
    order= ordering(graph, indegree)
    if len(order) < n:
        print("NO")
    
    else:
        current = {node: index for index, node in enumerate(order)}
        print('YES')
        for u, v in undirected:
            if current[u] < current[v]:
                print(u+ 1, v + 1)
                
            else:
                print(v + 1, u + 1)

        for u, v in directed:
            print(u + 1, v + 1)