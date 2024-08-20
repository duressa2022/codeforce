for _ in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    counter1=counter2=0
    for num in array:
        if num%2==0:
            counter1+=1
        else:
            counter2+=1
    if counter1==counter2:
        print("Yes")
    else:
        print("No")