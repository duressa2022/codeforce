t=int(input())
for test in range(t):
    n=int(input())
    array=[int(char) for char in input().split()][::-1]
    stack=[]
    for i,value in enumerate(array):
        if stack and array[stack[-1]]>=value:
            if array[stack[-1]]>0:
                for j in range(stack[-1]+1):
                    if array[j]>0:
                        array[j]-=1
                array[i]+=1
        stack.append(i)
    Flag=True
    for i in range(n-1):
        if array[i]>=array[i+1]:
            Flag=False
            break
    if Flag:
        print("YES")
    else:
        print("NO")