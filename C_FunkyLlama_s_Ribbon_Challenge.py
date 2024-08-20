from functools import lru_cache
import sys
import threading

def main():
    n,a,b,c = list(map(int,input().split()))

    memo = [-1 for i in range(n + 1)]
    
    def dp(n):
        
        if n < 0:
            return -float('inf')
        if n == 0:
            return 0
        
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = 1 + max(dp(n - a),dp(n - b),dp(n - c))
        
        return memo[n]
    
    print(dp(n))
    
sys.setrecursionlimit( 1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()