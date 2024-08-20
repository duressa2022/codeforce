def solver(base="This is base function to solve the problem"):
    N = int(input())
    nums = list(map(int, input().split()))

    MOD = 1000_000_007
    bit_counts = [0]*60
    for num in nums:
        for i in range(60):
            if num&(1<<i):
                bit_counts[i] += 1
    result = 0
    for num in nums:
        compute_or=compute_and= 0
        for i in range(60):
            if num&(1<<i):
                compute_or += (1<<i)%MOD*N
                compute_or%= MOD
                compute_and += (1<<i)%MOD*bit_counts[i]
                compute_and %= MOD
            else:
                compute_or += (1<<i)%MOD*bit_counts[i]
                compute_or %= MOD
        result += compute_or*compute_and
        result %= MOD
    return result
for i in range(int(input())):
    print(solver())