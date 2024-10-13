def min_packages(n, k):
    min_ = n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i <= k:
                min_ = min(min_, n // i)
            if n // i <= k:
                min_ = min(min_, i)
    
    return min_

import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
results = []
for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    index += 2
    results.append(min_packages(n, k))
for result in results:
    print(result)
