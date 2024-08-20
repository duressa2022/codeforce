def solver(n):
    primes=set()
    d=2
    while d**d<=n:
        while n%d==0:
            primes.add(d)
            n=n//d
        d=d+1
    if n>1:
        primes.add(n)
    return primes
for _ in range(int(input())):
    number=int(input())
    primes=solver(number)
    if len(primes)<1:
        print("NO")
    else:
        flag=False
        for num in primes:
            if num!=2 and number%num==0:
                flag=True
                break
        if flag:
            print("YES")
        else:
            print("NO")
        

            