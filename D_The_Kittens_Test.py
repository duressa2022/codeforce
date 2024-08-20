from collections import defaultdict,deque
length=int(input())
parent={node:node for node in range(1,length+1)}
size={node:1 for node in range(1,length+1)}
merged={node:[node] for node in range(length+1)}
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union( x, y):
    rooty = find(y)
    rootx = find(x)
    if size[rootx] > size[rooty]:
        parent[rooty] = rootx
        size[rootx] += size[rooty]
        merged[rootx].extend(merged[rooty])
    else:
        parent[rootx] = rooty
        size[rooty] += size[rootx]
        merged[rooty].extend(merged[rootx])
for _ in range(length-1):
    u,v=list(map(int,input().split()))
    union(u,v)
print(*merged[find(1)])

