length=int(input())
array=list(map(int,input().split()))
maxValue=max(array)
result=set()
for num in array:
    while num>0 and (num%2==0 or num%3==0):
        if num%2==0:
            num=num/2
        elif num%3==0:
            num=num/3
    result.add(num)

if len(result)==1:
    print("Yes")
else:
    print("No")

