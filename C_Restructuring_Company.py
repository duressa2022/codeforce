def main():
    n,q = list(map(int,input().split()))
    parent= list(range(n + 2))
    next = list(range(1, n + 2 + 1))
    results = []
    while q > 0:
        a,b,c=list(map(int,input().split()))
        q -= 1
        if a == 1:
            union(parent, b, c)
        elif a == 2:
            aroot = find(parent, c)
            i = b
            while i <= c:
                parent[find(parent, i)] = aroot
                tmp = i
                i = next[i]
                next[tmp] = next[c]
        elif a == 3:
            results.append("YES" if find(parent, b) == find(parent, c) else "NO")

    print("\n".join(results))

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    parent[find(parent, a)] = find(parent, b)

if __name__ == "__main__":
    main()
