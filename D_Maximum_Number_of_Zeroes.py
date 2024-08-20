import sys
from collections import Counter
from math import gcd
def solver():
    n = int(sys.stdin.readline().strip())
    array1 =list(map(int, sys.stdin.readline().strip().split()))
    array2 =list(map(int, sys.stdin.readline().strip().split()))
    count = Counter()
    current = 0
    for i in range(n):
        if array1[i] == 0:
            if array2[i] == 0:
                current += 1
        else:
            x = array2[i] // (gcd(abs(array1[i]), abs(array2[i])))
            y = array1[i] // (gcd(abs(array1[i]), abs(array2[i])))
            if array2[i] < 0:
                x *=  -1
                y *= -1
            elif array2[i] == 0 and array1[i] < 0:
                y *=  -1
            count[(x, y)] += 1
    if len(count) == 0:
        print(current)
    else:
        print(current + max(count.values()))
solver()