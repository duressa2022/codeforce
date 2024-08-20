from collections import Counter
for _ in range(int(input())):
    string=input()
    counter=Counter(string)
    if len(counter)>1:
        print(len(string)-1)
    else:
        print(-1)
