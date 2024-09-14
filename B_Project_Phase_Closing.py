def find(n, m, k):
    r = (k - 1) // (2 * m) + 1
    
    pos = (k - 1) % (2 * m)
    
    d = (pos // 2) + 1
    
    s = 'L' if pos % 2 == 0 else 'R'
    
    return r, d, s
n, m, k = map(int, input().split())
r, d, s = find(n, m, k)
print(r, d, s)

