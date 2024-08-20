def mainFunction():
    n,k=list(map(int,input().split()))
    heights=list(map(int,input().split()))
    def solver(i):
        if i>=n:
            return 0
        ans=0
        for j in range(1,k+1):
            if i+j<n:

        return ans
    print(solver(0))
mainFunction()