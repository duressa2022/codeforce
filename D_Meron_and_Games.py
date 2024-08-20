from collections import Counter
import sys
sys.setrecursionlimit(1000)
def solver():
    length=int(input())
    array=list(map(int,input().split()))
    counter=Counter(array)
    temp_array=[key for key in counter]
    temp_array.sort()
    length=len(temp_array)
    memo={}
    def minSolver(i):
        if i in memo:
            return memo[i]
        if i>=length:
            return 0
        if i<length-1 and temp_array[i]+1==temp_array[i+1]:
            take=temp_array[i]*counter[temp_array[i]]+minSolver(i+2)
        else:
            take=temp_array[i]*counter[temp_array[i]]+minSolver(i+1)
        dont=minSolver(i+1)
        memo[i]=max(take,dont)
        return memo[i]
    print(minSolver(0))

solver()
