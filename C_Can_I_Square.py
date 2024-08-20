from math import sqrt
def solver(num):
    return sqrt(num)-int(sqrt(num))==0
for _ in range(int(input())):
    n=input()
    num=sum(map(int,input().split()))
    if solver(num):
        print("YES")
    else:
        print("NO")
    