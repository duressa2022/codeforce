for _ in range(int(input())):
    n=int(input())
    alice=1
    bob=0
    a=1
    b=0
    s=1
    flag=True
    while s<=n:
        if flag:
            if a+1+s>n:
                b+=(n-s)
            else:
                b+=(a+1)
            
            if a+2+s>n:
                b+=(n-s)
            else:
                b+=(a+2)
            flag=True
            bob+=b
            s+=bob
        else:
            if b+1+s>n:
                a+=(n-s)
            else:
                a+=(b+1)

            if b+2+s>n:
                a+=(n-s)
            else:
                a+=(b+2)
            alice+=a
            flag=False
            s+=alice
    print(alice,bob)




      



