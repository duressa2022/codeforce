def solver(n):
    result=set()
    d=2
    while d*d<=n:
        while n%d==0:
            result.add(d)
            n=n//d
        d=d+1
    if n>1:
        result.add(n)
    return len(result)
number=int(input())
counter=0
for i in range(1,number+1):
    if solver(i)==2:
        counter+=1
print(counter)


