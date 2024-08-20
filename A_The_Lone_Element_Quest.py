from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    list_number=input().split()
    map_number=Counter(list_number)
    for i in range(n):
        if map_number[list_number[i]]==1:
            print(i+1)
