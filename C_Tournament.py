import sys, threading
input = lambda: sys.stdin.readline().strip()
from math import floor
t=int(input())
def main():
    def function(nums,k):
        memo={}
        length=len(nums)
        def solver(index,take):
            if (index,take) in memo:
                return memo[(index,take)]
            if index>=length:
                return 0
            
            pick=floor(take*nums[index])-k+solver(index+1,take)
            half=floor(take*nums[index]/2)+solver(index+1,take/2)

            memo[(index,take)]=max(pick,half)
            return memo[(index,take)]
        return solver(0,1)
    for _ in range(t):
        n,k=list(map(int,input().split()))
        nums=list(map(int,input().split()))
        ans=function(nums,k)
        print(ans)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

