for _ in range(int(input())):
    n=int(input())
    counter=0
    while n>1:
        if n%2==0:
            counter+=1
            n=n//2
        elif n%3==0:
            counter+=1
            n=2*(n//3)
        elif n%5==0:
            counter+=1
            n=4*(n//5)
        else:
            counter=-1
            break
    print(counter)

