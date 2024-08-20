from collections import Counter
for _ in range(int(input())):
    string,word=input().split()
    counter=Counter(string)
    set_=set(word)

    for char in reversed(string):
        if char not in set_:
            counter[char]=0
        else:
            if counter[char]==1:
                continue
            else:
                if counter[char]==2:
                    

