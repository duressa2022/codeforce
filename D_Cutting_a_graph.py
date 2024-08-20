n,m,q=list(map(int,input().split()))
parent={node:node for node in range(1,n+1)}
size={node:1 for node in range(1,n+1)}
def find(node):
    while node!=parent[node]:
        parent[node]=parent[parent[node]]
        node=parent[node]
    return node
def union(u,v):
    uroot=find(u)
    vroot=find(v)
    if uroot!=vroot:
        usize=size[uroot]
        vsize=size[vroot]
        if usize>vsize:
            parent[vroot]=uroot
            size[usize]+=vsize
        else:
            parent[uroot]=vroot
            size[vsize]+=usize
edgelist=[]
for _ in range(m):
    edgelist.append(tuple(map(int,input().split())))
request=[]
for _ in range(q):
    request.append(input().split())
results=[]
for query,u,v in reversed(request):
    u,v=int(u),int(v)
    if query=="ask":
        if find(u)==find(v):
            results.append("YES")
        else:
            results.append("NO")
    else:
        union(u,v)
for result in reversed(results):
    print(result)
