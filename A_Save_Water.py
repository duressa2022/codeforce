n=int(input())
m=int(input())
array=[]
for i in range(n):
    array.append(int(input()))
array.sort(reverse=True)
temp_counter=[0]*(len(array)+1)
for i in range(1,len(array)+1):
    temp_counter[i]=temp_counter[i-1]+array[i-1]
for i in range(len(temp_counter)):
    if temp_counter[i]>=m:
        print(i)
        break