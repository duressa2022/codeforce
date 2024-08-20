for _ in range(int(input())):
    n=int(input())
    string=input()
    counter=0
    for char in reversed(string):
        if char==")":
            counter+=1
        else:
            break
    if n-counter<counter:
        print("Yes")
    else:
        print("No")
