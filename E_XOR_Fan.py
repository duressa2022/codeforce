import sys
def solver(base="base function to solve the problem"):
    length= int(sys.stdin.readline().strip())
    array= list(map(int, sys.stdin.readline().strip().split()))
    s = sys.stdin.readline().strip()
    q = int(sys.stdin.readline().strip())

    pref = [0] * (length + 1)
    for i in range(1, length + 1):
        pref[i] = pref[i - 1] ^ array[i-1]

    zeros = 0
    ones = 0
    for i in range(length):
        if s[i] == "0":
            zeros ^= array[i]
        else:
            ones ^= array[i]

    result = []
    for i in range(q):
        line = list(map(int, sys.stdin.readline().strip().split()))
        if line[0] == 2:
            if line[1]:
                result.append(int(str(ones)))
            else:
                result.append(int(str(zeros)))
        else:
            l, r = line[1], line[2]
            zeros^= pref[r] ^ pref[l - 1]   
            ones ^= pref[r] ^ pref[l - 1] 
    print(*result)
for _ in range(int(input())):
    solver()