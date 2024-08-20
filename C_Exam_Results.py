from collections import Counter

n = int(input())
scores =  list(map(int, input().split()))
n = len(scores)
dp = [[0] * (n - 1)] * (n - 1)
for i in range(1, n):
    for j in range(1, n):
        if scores[i] > scores[j]:
            dp[i][j] = max(dp[i - 1][k - 1] + 1, where k is the index of the paper with score ai+1 > ai)


print(max(dp[n - 1]))