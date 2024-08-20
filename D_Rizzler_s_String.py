
import sys
input = lambda: sys.stdin.readline().rstrip()
mod = 10**9 + 7
s = input()

def solver(mod, s):
    counter=0
    before= 0 

    for idx, char in enumerate(s):
        if char == 'b':
            before= counter
    
        elif char == 'a':
            counter += before+ 1
            counter %= mod
    print(counter)
solver(mod, s)