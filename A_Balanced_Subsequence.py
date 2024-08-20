from collections import Counter
n,k=list(map(int,input().split()))
counter=Counter(input())
min_=min(counter.values())
if k!=len(counter):
    print(0)
else:
    print(min_*k)
