
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index+n]))
        index += n
        
        # Binary search for the maximum k
        left = 1
        right = max(arr)
        
        # Prefix maximum array
        prefix_max = [0] * n
        prefix_max[0] = arr[0]
        
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], arr[i])
        
        def can_win_with_k(k):
            for i in range(n - 1):
                if prefix_max[i] > k:
                    return True
            return False
        
        while left < right:
            mid = (left + right) // 2
            if can_win_with_k(mid):
                left = mid + 1
            else:
                right = mid
        
        results.append(right - 1)  # We want the maximum k Alice is guaranteed to win
        
    sys.stdout.write('\n'.join(map(str, results)) + '\n')
solve()
