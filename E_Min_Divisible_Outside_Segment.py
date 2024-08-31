for _ in range(int(input())):
    l,r,d=list(map(int,input().split()))
    if l%d==0 and abs(r-d)!=0:
        print(abs(r-d))

    elif l%d and r-d!=0:
        
    
