import sys, threading
input = lambda: sys.stdin.readline().strip()
def main():
    def solver(n):
        if n in memo:
            return memo[n]
        if n==0:
            return 0
        if n<0:
            return float("inf")
        
        one=1+solver(n-1)
        three=solver(n-3)
        five=solver(n-5)
        memo[n]=min(one,three,five)
        return memo[n]
    for _ in range(int(input())):
        n=int(input())
        memo={}
        ans=solver(n)
        print(ans)
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
