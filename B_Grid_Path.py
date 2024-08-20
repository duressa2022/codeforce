import sys, threading
input = lambda: sys.stdin.readline().strip()
def main():
    def solver():
        n,m,k=list(map(int,input().split()))
        memo={}
        def minSolver(row,col,k):
            if (row,col) in memo:
                return memo[(row,col)]
            if row>=n or col>=m:
                return False
            if row==n-1 and col==m-1:
                if k==0:
                    return True 
                else:
                    return False
            memo[(row,col)]=minSolver(row+1,col,k-col-1) or minSolver(row,col+1,k-row-1)
            return memo[(row,col)]
        if minSolver(0,0,k)==True:
            print("YES")
        else:
            print("NO")

    for _ in range(int(input())):
        solver()
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
