for _ in range(int(input())):
    n=int(input())
    string=input()
    ans=[]
    bs=[]
    for char in string:
        if char!="b":
            ans.append(char)
        else:
            bs.append(char)
    ans=bs+ans
    print("".join(ans))