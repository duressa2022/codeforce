def sieve(n):
    number=[True for i in range(n+1)]
    number[0]=number[1]=False
    i=2
    while i*i<=n:
        if number[i]:
            j=i*i
            while j*j<=n:
                number[j]=False
                j=j+1
        i=i+1
    return number
print(sieve(5))






