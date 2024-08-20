def mainFunction():
    length=int(input())
    heights=list(map(int,input().split()))
    def solver(i):
        if i>=length:
            return 0
        take=0
        dont=0
        if i+1<length:
            take=abs(heights[i]-heights[i+1])+solver(i+1)
        if i+2<length:
            dont=abs(heights[i]-heights[i+2])+solver(i+2)
        return min(take,dont)
    print(solver(0))
mainFunction()
