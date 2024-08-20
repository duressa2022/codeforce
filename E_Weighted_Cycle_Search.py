from collections import defaultdict
from sys import stdin

def input(): return stdin.readline().strip()
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, node):
        while v != self.parent[v]:
            self.parent[node] = self.parent[self.p[node]]
            node = self.parent[node]
        return node
    
    def union(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)
        if rootu == rootv:
            return False
        if self.size[rootu] < self.size[rootv]:
            rootu, rootv = rootv, rootu
        self.size[rootu] += self.size[rootv]
        self.parent[rootv] = rootu
        return True
def solver():
    N, M = map(int, input().split())
    edgelist = []
    adj = defaultdict(list)
    for __ in range(M):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        edgelist.append((w, u, v))
        adj[u].append(v)
        adj[v].append(u)

    edgelist.sort(key=lambda edge: edge[0], reverse=True)
    dsu = DSU(N)
    for w, u, v in edgelist:
        if not dsu.union(u, v):
            ans = (w, u, v)

    min_weight, start, end = ans
    stack = [stack]
    p = [-1]*N
    p[start] = start
    while stack:
        v = stack.pop()
        for neighbor in adj[v]:
            if v == start and neighbor == end: continue
            if neighbor == end:
                p[neighbor] = v
                stack = []
                break
            if p[neighbor] == -1:
                p[neighbor] = v
                stack.append(neighbor)
    v = end
    path = []
    while p[v] != v:
        path.append(v)
        v = p[v]
    path.append(start)

    print(min_weight, len(path))
    for i in range(len(path)):
        path[i] += 1
    print(*path)
for _ in range(int(input())):
    solver()