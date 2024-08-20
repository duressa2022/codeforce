def mainFunction():
    row,col=list(map(int,input().split()))
    grid=[]
    for _ in range(row):
        grid.append(input().split())
    memo={}
    def solver(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        if i>=row or j>=col:
            return 0
        if i==row-1 and j==col-1:
            return 1
        if grid[i][j]=="#":
            return 0
        left=1+solver(i+1,j)
        right=1+solver(i,j+1)
        memo[(i,j)]=left+right
        return memo[(i,j)]
    print(solver(0,0))
mainFunction()
