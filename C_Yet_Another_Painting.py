t=int(input())
for i in range(t):
    n=int(input())
    red=[int(char) for char in input().split()]
    m=int(input())
    blue=[int(char) for char in input().split()]
    running=0
    maxRed=0
    maxBlue=0
    for i in range(n):
        running+=red[i]
        maxRed=max(maxRed,running)
    running=0
    for i in range(m):
        running+=blue[i]
        maxBlue=max(maxBlue,running)
    print(maxRed+maxBlue)
