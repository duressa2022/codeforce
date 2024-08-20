length=int(input())
array=list(map(int,input().split()))
i=0
j=1
k=2
counter1=0
counter2=0
counter3=0
while k<length:
    counter1+=array[i]
    counter2+=array[j]
    counter3+=array[k]
    i=k+1
    j=i+1
    k=j+1
while j<length:
    counter1+=array[i]
    counter2+=array[j]
    i=j+1
    j=i+1
while i<length:
    counter1+=array[i]
    i=i+1
if counter1>counter2 and counter1>counter3:
    print("chest")
elif counter2>counter1 and counter2>counter3:
    print("biceps")
else:
    print("back")
