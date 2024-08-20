def solver(tc):
    n = int(input())
    a = list(map(int, input().split()))
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]
    q = int(input())
    for _ in range(q):
        l, u = map(int, input().split())
        left, right = l, n
        while left < right:
            mid = (left + right + 1) >> 1
            if prefix[mid] - prefix[l - 1] <= u:
                left = mid
            else:
                right = mid - 1
        maxvalue = -1e18
        value = 0
        for i in range(max(l, left - 2), min(n, right + 2) + 1):
            t = prefix[i] - prefix[l - 1]
            uvalue= (u + (u - t + 1)) * t // 2
            if uvalue > maxvalue:
                maxvalue = uvalue
                value = i
        print(value, end=" ")

t = int(input())
for i in range(1, t + 1):
    solver(i)
    print()
