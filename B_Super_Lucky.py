number=(input())
result=[]
counter4=len(number)//2
counter5=counter4
for num in number:
    if int(num)<=4:
        if counter4>0:
            result.append("4")
            counter4-=1
        else:
            result.append("7")
            counter5-=1
    else:
        if counter5>0:
            result.append("7")
            counter5-=1
        else:
            result.append("4")
            counter4-=1
flag=False
for num in number:
    if int(num)>7:
        flag=True
if flag:
    result=["4"]+result+["7"]
    result.sort()
if len(number)%2==1:
    length=len(number)+1
    half=length//2
    result=["4" for i in range(half)]+["7" for i in range(half)]
print("".join(result))
