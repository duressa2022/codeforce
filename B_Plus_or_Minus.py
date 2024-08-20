t=int(input())
for i in range(t):
    array=input().split(" ")
    a,b,c=array[0],array[1],array[2]
    a,b,c=int(a),int(b),int(c)
    if a+b==c:
        print("+")
    else:
        print("-")

