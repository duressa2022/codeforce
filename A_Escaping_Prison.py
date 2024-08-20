def solver(array,height):
    runnning=0
    for w,l in array:
        if w>l:
            runnning+=w
        else:
            runnning+=l
    if runnning>=height:
        return True
    else:
        return False
t=int(input())
for i in range(t):
    array=[]
    n,heights=input().split()
    n=int(n)
    heights=int(heights)
    for j in range(n):
        w,l=input().split()
        w,l=int(w),int(l)
        array.append((w,l))
    if solver(array,heights):
        print("YES")
    else:
        print("NO")


