n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
original = [[1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            for k in range(n):
                original[k][j] = 0
            for t in range(m):
                original[i][t] = 0

newMatrix = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        newMatrix[i][j] |= int(any(original[i] + [original[k][j] for k in range(n)]))
if newMatrix == matrix:
    print('YES')
    for i in range(n):
        print(*original[i])
else:
    print('NO')