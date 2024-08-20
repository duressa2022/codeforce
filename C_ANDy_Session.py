t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    counter = [0] * 31
    a = list(map(int, input().split()))
    for num in a:
        for j in range(30, -1, -1):
            if num & (1 << j):
                counter[j] += 1
    result = 0
    for i in range(30, -1, -1):
        what = n - counter[i]
        if what <= k:
            k -= what
            result += (1 << i)
    print(result)
