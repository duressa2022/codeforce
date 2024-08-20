for _ in range(int(input())):
    length=int(input())
    nums=sorted(list(map(int,input().split())))
    bob=0
    alice=0
    player=True
    while nums:
        cur=nums.pop()
        if player==True:
            if cur%2==0:
                alice+=cur
            player=False
        else:
            if cur%2==1:
                bob+=cur
            player=True
    if alice>bob:
        print("Alice")
    elif alice<bob:
        print("Bob")
    else:
        print("Tie")

