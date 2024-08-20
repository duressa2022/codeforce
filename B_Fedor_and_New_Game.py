def solver(nums,compare,key):
    result=0
    for num in nums:
        diff=num^compare
        counter=0
        while diff>0:
            if (diff&1)==1:
                counter+=1
            diff>>=1
        if counter<=key:
            result+=1
    return result
n,m,key=list(map(int,input().split()))
array=[]
for _ in range(m):
    array.append(int(input()))
compare=int(input())
print(solver(array,compare,key))
        
        

