from collections import Counter
t=int(input())
for test in range(t):
    n=int(input())
    result=[]
    for i in range(n):
        array=[char for char in input()]
        array=set(array)
        ans=len(array)
        result.append(ans)
    result.sort()
    flag=True
    for i in range(n-1):
        if result[i]!=result[i+1]:
            flag=False
            break
    if flag:
        print("YES")
    else:
        print("NO")



