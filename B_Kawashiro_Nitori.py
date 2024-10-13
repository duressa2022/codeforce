def solve(s, k):
    n = len(s)
    # Iterate over possible lengths for the first `k` substrings
    for i in range(n // (k + 1) + 1):
        # Try every possible split point for the k substrings
        if i * (k + 1) > n:
            continue
        prefix_length = i * k
        suffix_length = n - (prefix_length + i)
        
        if suffix_length < i:
            continue
        
        prefix_part = s[:prefix_length]
        remaining_string = s[prefix_length:]
        reverse_part = remaining_string[i:]
        ak1_length = len(remaining_string) - len(reverse_part)
        
        # Extract substrings a1, a2, ..., ak and ak+1
        substrings = []
        start = 0
        for _ in range(k):
            substrings.append(prefix_part[start:start + i])
            start += i
        ak1 = remaining_string[:ak1_length]
        substrings.append(ak1)
        
        # Construct the reverse part
        reversed_part = ''.join(reversed(substrings[:-1]))  # exclude ak1
        
        if remaining_string == ak1 + reversed_part:
            return "YES"
    return "NO"

# Reading input
t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().strip().split())
    s = input().strip()
    print(solve(s, k))
