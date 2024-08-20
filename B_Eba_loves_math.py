def solver():
    for _ in range(int(input())):
        length=int(input())
        array=list(map(int,input().split()))
        ans=array[0]
        for num in array:
            ans=min(ans,ans&num)
        print(ans)
solver()