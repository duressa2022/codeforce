"""t=int(input())
for i in range(t):
    n=int(input())
    string=input()
    string=[i for i in string]
    i=0
    j=1
    while len(string)>2 and j<len(string):
        if string[i]!=string[j]:
            string.remove(string[i])
            string.remove(string[i])
            i=0
            j=1
        else:
            i=i+1
            j=j+1
    if len(string)==2:
        if string[0]!=string[1]:
            print(0)
    else:
        print(len(string))"""
t=int(input())
for i in range(t):
    n=int(input())
    string=input()
    map={}
    for j in string:
        if j not in  map:
            map[j]=1
        else:
            map[j]+=1
    mostCommonValue=-float("inf")
    mostCommonChar=""
    for val in map:
        if map[val]>mostCommonValue:
            mostCommonValue=map[val]
            mostCommonChar=val
    notMostCommon=0
    for val in map:
        if val!=mostCommonChar:
            notMostCommon+=map[val]
    result=mostCommonValue-notMostCommon
    if result>0:
        print(result)
    else:
        if n%2==1:
            print(1)
        else:
            print(0)


