def solver(l,r,x,a,b):
    if a==b:
        return 0
    if abs(a-b)>=x:
        return 1
    
    if abs(a-l)>=x and abs(l-b)>=x:
        return 2
    if abs(a-r)>=x and abs(r-b)>=x:
        return 2
    
    if abs(a-l)>=x and abs(l-r)>=x and abs(r-b)>=x:
        return 3
    if abs(a-r)>=x and abs(r-l)>=x and abs(l-b)>=x:
        return 3
    return -1

for _ in range(int(input())):
    l,r,x=list(map(int,input().split()))
    a,b=list(map(int,input().split()))
    ans=solver(l,r,x,a,b)
    print(ans)