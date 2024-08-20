from collections import Counter
def solver():
    array=[char for char in input()]
    length=len(array)//2
    one=array[:length]
    other=array[length:]
    return "".join(one)=="".join(other)
for _ in range(int(input())):
    if solver():
        print("YES")
    else:
        print("NO")

    