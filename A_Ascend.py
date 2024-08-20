def solver():
    length=int(input())
    array=list(map(int,input().split()))
    maxlength=1
    left=0
    right=1
    counter=1
    while right<length:
        if array[left]<array[right]:
            counter+=1
            left=left+1
            right=right+1
        else:
            maxlength=max(maxlength,counter)
            counter=1
            left=right
            right=right+1
    print(max(maxlength,counter))
solver()
