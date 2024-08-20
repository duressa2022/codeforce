from collections import deque
length=int(input())
a,b=list(map(int,input().split()))
a=a-1
b=b-1
c,d=list(map(int,input().split()))
c=c-1
d=d-1
graph=[]
for _ in range(length):
    row=[char for char in input()]
    graph.append(row)
def solver():
    def inbound(row,col):
        return 0<=row<length and 0<=col<length
    dir=[(1,1),(1,-1),(-1,1),(-1,-1)]
    visted=set((a,b))
    if a==c and b==d:
        return 0
    queue=deque()
    for dx,dy in dir:
        x=a+dx
        y=b+dy
        if inbound(x,y) and graph[x][y]==".":
            queue.append((x,y,1,abs(dx+dy)))
    
    while queue:
        curx,cury,move,value=queue.popleft()
        if curx==c and cury==d:
            return move
        visted.add((curx,cury))
        for dx,dy in dir:
            x=curx+dx
            y=cury+dy
            if inbound(x,y) and (x,y) not in visted and graph[x][y]==".":
                if value==abs(dx+dy):
                    queue.append((x,y,move,value))
                else:
                    queue.append((x,y,move+1,abs(dx+dy)))
    return -1
print(solver())




