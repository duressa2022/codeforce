
n,m=list(map(int,input().split()))
def formGraph():
    array=[]
    for _ in range(n):
        array.append([int(value) for value in input()])
    return array
def check(array):
    for row in array:
        if len(set(row))!=1:
            return False
    return True
def inbound(row,col):
    return 0<=row<n and 0<=col<m
def ssolver():
    visted=set()
    def solver(array,row,col):
        stack=[(row,col)]
        while stack:
            row,col=stack.pop()
            visted.add((row,col))
            x=row+1
            y=col
            if inbound(x,y) and (x,y) not in visted:
                if array[row][col]==array[x][y]:
                    return False
                stack.append((x,y))
        return True
    array=formGraph()
    if not check(array):
        return False
    
    for i in range(n):
        for j in range(m):
            if (i,j) not in visted:
                if not solver(array,i,j):
                    return False
    return True
if ssolver():
    print("YES")
else:
    print("NO")




