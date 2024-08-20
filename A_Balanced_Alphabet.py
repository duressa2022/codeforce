def solver():
    n,k=list(map(int,input().split()))
    x=n//k
    y=n%k
    total=x+y
    index=0
    string=""
    counter=1
    string+=chr(97)*total
    index+=total
    while index<n:
        string+="{}".format(chr(97+counter))*x
        index+=x
        counter+=1
    print(string)
for _ in range(int(input())):
    solver()



