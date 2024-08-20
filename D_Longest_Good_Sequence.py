from math import gcd
import sys, threading
input = lambda: sys.stdin.readline().strip()
def main():
    def good(x,y):
        if x<y and gcd(x,y)>1:
            return True
        return False
    n=int(input())
    nums=list(map(int,input().split()))
    memo={}
    def solver(i):
        if i in memo:
            return memo[i]
        if i>=n:
            return 0
        ans=0
        for j in range(i+1,n):
            if good(nums[i],nums[j]):
                ans=max(ans,1+solver(j))
        memo[i]=ans
        return memo[i]
    ans=0
    for i in range(n):
        ans=max(ans,1+solver(i))
        memo[i]=ans
    print(ans)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
