from collections import defaultdict
n,q=list(map(int,input().split()))
parent={node:node for node in range(1,n+1)}
rank={node:1 for node in range(1,n+1)}
size={node:1 for node in range(1,n+1)}
minValue={node:node for node in range(1,n+1)}
maxValue={node:node for node in range(1,n+1)}
def find(node):
    while node!=parent[node]:
        parent[node]=parent[parent[node]]
        node=parent[node]
    return node
def union(u,v):
    uroot=find(u)
    vroot=find(v)
    if uroot!=vroot:
        urank=rank[uroot]
        vrank=rank[vroot]
        if urank>vrank:
            parent[vroot]=uroot
            size[uroot]+=size[vroot]
            minValue[uroot]=min(minValue[uroot],minValue[vroot])
            maxValue[uroot]=max(maxValue[uroot],maxValue[vroot])
        elif urank<vrank:
            parent[uroot]=vroot
            size[vroot]+=size[uroot]
            minValue[vroot]=min(minValue[uroot],minValue[vroot])
            maxValue[vroot]=max(maxValue[uroot],maxValue[vroot])
        else:
            parent[uroot]=vroot
            size[vroot]+=size[uroot]
            minValue[vroot]=min(minValue[uroot],minValue[vroot])
            maxValue[vroot]=max(maxValue[uroot],maxValue[vroot])
            rank[vroot]+=1
for _ in range(q):
    query=input().split()
    if len(query)==2:
        q,u=query
        u=int(u)
        root=find(u)
        print(minValue[root],maxValue[root],size[root])
    else:
        q,u,v=query
        u,v=int(u),int(v)
        union(u,v)




