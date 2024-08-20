def gcd_of_range(a, b):
    if a == b:
        return a
    else:
        return 1
a,b=input().split()
a,b=int(a),int(b)
print(gcd_of_range(a, b))
