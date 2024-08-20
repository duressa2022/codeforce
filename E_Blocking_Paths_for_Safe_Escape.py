from collections import defaultdict
def formGraph():
    graph=[]
    n,m=list(map(int,input().split()))
    for _ in range(n):
        graph.append([char for char in input()])
    return (n,m,graph)
def solver():
    DIR=[(1,0),(-1,0),(0,1),(0,-1)]
    n,m,graph=formGraph()
    def inbound(row,col,visted,graph):
        return (0<=row<n and 0<=col<m) and (row,col) not in visted and graph[row][col]!="#"
    good,bad,empty=[],[],[]
    for i in range(n):
        for j in range(m):
            if graph[i][j]=="G":
                good.append((i,j))
            elif graph[i][j]=="B":
                bad.append((i,j))
            elif graph[i][j]==".":
                empty.append((i,j))
    for row,col in empty:
        for dx,dy in DIR:
            x=row+dx
            y=col+dy
            if 0<=x<n and 0<=y<m and graph[x][y]=="B":
                graph[row][col]="#"
                break
    stack=[(n-1,m-1)]
    visted=set()
    while stack:
        row,col=stack.pop()
        if (not (0<=row<n and 0<=col<m)) or (row,col) in visted or graph[row][col]=="#":
            continue
        visted.add((row,col))
        for dx,dy in DIR:
            x=row+dx
            y=col+dy
            stack.append((x,y))
    ans="Yes"
    for node in good:
        if node not in visted:
            ans="No"
            break
    for node in bad:
        if node in visted:
            ans="No"
            break
    print(ans)
for _ in range(int(input())):
    solver()
        