from collections import defaultdict
t=int(input())
for i in range(t):
    length=int(input())
    numbers=map(int,input().split())
    counter=defaultdict(int)
    appearance=defaultdict(int)
    for number in numbers:
        counter[number]+=1
        current=counter[number]
        appearance[current]+=current
    maxValue=max(appearance.values())
    print(length-maxValue)
