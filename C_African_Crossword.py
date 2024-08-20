from collections import defaultdict
rows,cols=map(int,input().split())
rowElements=[defaultdict(int) for i in range(rows)]
colElements=[defaultdict(int) for i in range(cols)]
matrix=[]
for i in range(rows):
    matrix.append(list(input()))
for i in range(rows):
    for j in range(cols):
        rowElements[i][matrix[i][j]]+=1
        colElements[i][matrix[j][i]]+=1
result=[]
for i in range(rows):
    for j in range(cols):
        if rowElements[i][matrix[i][j]]==1 and colElements[j][matrix[i][j]]==1:
            result.append(matrix[i][j])
print("".join(result))


    


