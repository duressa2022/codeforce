from math import ceil
def solver(n):
    if n==1:
        return 2
    if n==2 or n==3:
        return 1
    return ceil(n/3)
for _ in range(int(input())):
    n=int(input())
    ans=solver(n)
    print(ans)
   

