t=int(input())
for _ in range(t):
    n=int(input())
    array=[i for i in range(1,n+1)]
    for i in range(n-1):
        array[i],array[i+1]=array[i+1],array[i]
    print(*array)

