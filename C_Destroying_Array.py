n = int(input())
a = list(map(int,input().split()))
rem = list(map(int,input().split()))
parent = {i+1:(i+1,a[i]) for i in range(n)}
# print(parent)
build = [-1 for i in range(n)]

ans = []

for i in range(n,-1,-1):
    build[rem[-1]] = 
