n=int(input())
array=input().split()
box=[int(i) for i in array]
box.sort()
for i in range(n):
    print(box[i],end=" ")