n,k=list(map(int,input().split()))
array=list(map(int,input().split()))
ans=0
for num in array:
    counter=0
    for char in str(num):
        if char=="4" or char=="7":
            counter+=1
    if counter<=k:
        ans+=1
print(ans)
