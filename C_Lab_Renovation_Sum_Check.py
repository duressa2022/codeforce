n=int(input())
m=[]
def solver():
    for _ in range(n):
        m.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            if m[i][j]==1:
                continue
            else:
                row=[]
                for index in range(n):
                    if (i,index)==(i,j):
                        continue
                    row.append(m[i][index])
                col=[]
                for index in range(n):
                    if (index,j)==(i,j):
                        continue
                    col.append(m[index][j])
                cur=m[i][j]
                flag=False
                for val1 in row:
                    for val2 in col:
                        if val1+val2==cur:
                            flag=True
                            break
                if not flag:
                    return False
    return True
ans=solver()
if ans:
    print("Yes")
else:
    print("No")
                            

    
