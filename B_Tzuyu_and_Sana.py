def solver(a,b):
    index=x=0
    while a or b:
        if (a&1) and (b&1):
            x+=(1<<index)
        a>>=1
        b>>=1
        index+=1
    return x
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    x=solver(a,b)
    print((a^x)+(b^x))