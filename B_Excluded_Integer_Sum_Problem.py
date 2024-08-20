
def solver(n,k,x):
    if x!=1:
        print("YES")
        print(n)
        print(*[1 for _ in range(n)])
    elif k==1:
        print("NO")
    elif k==2 and n%2==1:
        print("NO")
    else:
        ans=[2 if n%2==0 else 3]
        for _ in range(n//2):
            ans.append(2)
        print("YES")
        print(len(ans))
        print(*ans)
for _ in range(int(input())):
    n,k,x=list(map(int,input().split()))
    solver(n,k,x)
        
        
