t=int(input())
for i in range(t):
    n=int(input())
    array=[int(char) for char in input().split()]
    hash_set=set(array)
    counter_temp=[0]*(n+1)
    for i in range(1,n):
        counter_temp[i]=counter_temp[i-1]+array[i]
    

