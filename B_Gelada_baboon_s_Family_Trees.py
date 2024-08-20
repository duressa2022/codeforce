from collections import defaultdict,deque
length=int(input())
parent={node:node for node in range(1,length+1)}
size={node:1 for node in range(1,length+1)}
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
    else:
        parent[rootx] = rooty
        size[rooty] += size[rootx]
def solver():
    array=list(map(int,input().split()))
    counter=0
    for i in range(length):
        if find(i+1)==find(array[i]):
            counter+=1
        else:
            union(i+1,array[i])
    return counter
print(solver())