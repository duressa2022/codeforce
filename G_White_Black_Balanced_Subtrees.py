from collections import defaultdict
import sys
sys.setrecursionlimit(8000)
counter=0
def from_graph():
    graph = defaultdict(list)
    length = int(input())
    array = list(map(int, input().split()))
    for node in range(2, length + 1):
        parent = array[node - 2]
        graph[parent].append(node)
    return graph
def dfs(graph,node,color):
    global counter
    tempCounter=1 if color[node-1]=="W" else -1
    for neighbor in graph[node]:
        tempCounter+=dfs(graph,neighbor,color)
    if tempCounter==0:
        counter+=1
    return tempCounter
for _ in range(int(input())):
    graph = from_graph()
    color = input()
    counter=0
    dfs(graph,1,color)
    print(counter)

