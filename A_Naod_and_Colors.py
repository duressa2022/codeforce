from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    counter=Counter(a)
    ans=1
    for key in counter:
        ans=max(ans,counter[key])
    print(ans)