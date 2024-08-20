def solver():
    a,b,c=map(int,input().split())
    if c==0:return 0
    if a==0:return b
    if c-a==0:return -1
    counter=0
    while a!=0 and b!=0:
        counter+=a
        a,b,c=sorted([a,b-a,c-a])
        if a==0:
            counter+=b
            return counter
    return counter
for _ in range(int(input())):
    print(solver())

