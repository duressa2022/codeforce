def solver():
    n,k=list(map(int,input().split()))
    string=input()
    word=input()
    compare=0
    for char in word:
        compare+=ord(char)
    _sum=0
    for i in range(k):
        _sum+=ord(string[i])
    left=0
    for right in range(k,n):
        if _sum==compare:
            return True
        _sum=_sum-ord(string[left])+ord(string[right])
        left=left+1
    return _sum==compare
for _ in range(int(input())):
    if solver():
        print("YES")
    else:
        print("NO")

    


