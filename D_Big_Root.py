from collections import defaultdict
import sys, threading
input = lambda: sys.stdin.readline().strip()
from math import floor
def main():
    graph=defaultdict(list)
    values=[]
    memo={}
    def solver(node):
        if node in memo:
            return memo[node]
        if len(graph[node])==0:
            return values[node]
        ans=0
        for neighbor in graph[node]:
            if values[node]-values[neighbor]>=0:
                ans=max(ans,solver(neighbor))
        memo[node]=ans+values[node]
        return memo[node]
    for _ in range(int(input())):
        n=int(input())
        parent=list(map(int,input().split()))
        values=list(map(int,input().split()))
        graph=defaultdict(list)
        for index in range(1,len(parent)):
            graph[parent[index-1]]=index
        ans=solver(1)
        print(ans)
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
