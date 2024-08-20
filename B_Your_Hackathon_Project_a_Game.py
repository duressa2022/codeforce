import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
heights = list(map(int, data[2:n+2]))
quests = [(int(data[2+n+i*2])-1, int(data[3+n+i*2])-1) for i in range(m)]
left = [0] * n
right = [0] * n

for i in range(1, n):
    if heights[i-1] > heights[i]:
        left[i] = left[i-1] + (heights[i-1] - heights[i])
    else:
        left[i] = left[i-1]

for i in range(n-2, -1, -1):
    if heights[i+1] > heights[i]:
        right[i] = right[i+1] + (heights[i+1] - heights[i])
    else:
        right[i] = right[i+1]
results = []
for s, t in quests:
    if s < t:
        results.append(left[t] - left[s])
    else:
        results.append(right[t] - right[s])

print("\n".join(map(str, results)))
