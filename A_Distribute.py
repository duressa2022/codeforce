def solver():
    n=int(input())
    array=list(map(int,input().split()))
    temp=[]
    for i,num in enumerate(array):
        temp.append((num,i+1))
    temp.sort()
    left,right=0,n-1
    while left<right:
        x,i=temp[left]
        y,j=temp[right]
        print(i,j)
        left=left+1
        right=right-1
solver()
    
