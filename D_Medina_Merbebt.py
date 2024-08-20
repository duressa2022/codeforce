def solver():
    n = int(input()) 
    nums = list(map(int, input().split()))  
    q = int(input()) 

    arr = [0] * 32
    prefix = [arr] 
    for num in nums:
        bits = prefix[-1].copy()
        for i in range(32):
            if num & (1 << i) != 0:
                bits[i] += 1
        prefix.append(bits)
    def helperFunc1(left, right):
        result = 0
        for i in range(32):
            counter = prefix[right][i] - prefix[left - 1][i] if left > 0 else prefix[right][i]
            if counter == (right - left + 1):
                result |= (1 << i)
        return result
    def helperFunc2(l, k):
        left = l
        right = n
        while left <= right:
            mid = (right + left) // 2
            if helperFunc1(l, mid) >= k:
                left = mid + 1
            else:
                right = mid - 1

        if right < l:
            return -1
        return right

    result = []
    for _ in range(q):
        l, k = map(int, input().split())
        result.append(helperFunc2(l, k))

    print(*result)
for _ in range(int(input())):
    solver()