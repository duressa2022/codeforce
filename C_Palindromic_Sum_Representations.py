
import sys, threading
input = lambda: sys.stdin.readline().strip()
def main():
    def ispali(n):
        return str(n)==str(n)[::-1]
    mod=10**9+7
    def solver():
        n=int(input())
        memo={}
        def minSolver(current,prev,count):
            if current==0:
                return 1
            if (current,prev,count) in memo:
                return memo[(current,prev,count)]
            ans=0

            for i in range(1,current+1):
                if ispali(i) and current-i>=0:
                    if i!=prev or count<1:
                        ans=(ans+minSolver(current-i,i,count+1))%mod
            memo[(current,prev,count)]=ans
            return memo[(current,prev,count)]
        return minSolver(n,0,0)
    for _ in range(int(input())):
        print(solver())
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
