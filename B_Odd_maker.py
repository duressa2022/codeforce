t=int(input())

for i in range(t):
    n,q=input().split()
    n,q=int(n),int(q)
    array=[int(char) for char in input().split()]

    left=[0]*(len(array)+1)
    right=[0]*(len(array)+1)
    for j in range(1,len(array)+1):
        left[j]=left[j-1]+array[j-1]
    array=array[::-1]
    for j in range(1,len(array)+1):
        right[j]=right[j-1]+array[j-1]
    right=right[::-1]
    for j in range(q):
        l,r,k=input().split()
        l,r,k=int(l),int(r),int(k)
        result=left[l-1]+right[r]+(r-l+1)*k
        if result%2==1:
            print("YES")
        else:
            print("NO")

    


