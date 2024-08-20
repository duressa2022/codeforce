def solver(x):
    y=x&-x
    while x==y or x&y==0:
        y=y+1
    return y

for _ in range(int(input())):
    print(solver(int(input())))
