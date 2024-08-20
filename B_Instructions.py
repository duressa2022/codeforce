
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def minSolver(i):
        if i in memo:
            return memo[i]
        if i>=length:
            return 0
        current=array[i]+minSolver(i+array[i])
        memo[i]=current
        return memo[i]
    for _ in range(int(input())):
        length=int(input())
        array=list(map(int,input().split()))
        memo={}
        result=0
        for i in range(length):
            result=max(result,minSolver(i))
        print(result)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
