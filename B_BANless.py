def solve(n):
    print(n // 2 + n % 2)
    l = 1
    r = 3 * n
    while l < r:
        print(l, r)
        l += 3
        r -= 3

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        n = int(data[index])
        solve(n)
        index += 1

if __name__ == "__main__":
    main()
