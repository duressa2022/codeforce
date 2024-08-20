t=int(input())
for i in range(t):
    n,x=input().split()
    n=int(n)
    x=int(x)    
    array=[int(char) for char in input().split()]
    array.sort()
    array1=array[:n]
    array2=array[n:]
    flag=False
    for i in range(n):
        if array2[i]-array1[i]<x:
            flag=True
    if flag:
        print("NO")
    else:
        print("YES")
