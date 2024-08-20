from collections import Counter
string=input()
counter=Counter(string)
n=int(input())
if n>len(string):
    print("impossible")
else:
    if len(counter)>=n:
        print(0)
    else:
        print(n-len(counter))
