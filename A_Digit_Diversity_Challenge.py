from collections import Counter
l,k=map(int,input().split())
number=[]
result=-1
for i in range(l,k+1):
    number.append((i,Counter(str(i))))
for i in range(len(number)):
    flag=True
    value,temp=number[i]
    for key in temp:
        if temp[key]>1:
            flag=False
            break
        else:
            flag=True
    if flag==True:
        result=value
        break
print(result)
