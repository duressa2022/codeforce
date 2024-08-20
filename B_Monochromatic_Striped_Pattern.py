t=int(input())
for i in range(t):
    n,k=input().split()
    n,k=int(n),int(k)
    string=input()
    temp_counter=[0]*(n+1)
    for i in range(1,len(string)+1):
        if string[i-1]=="B":
            temp_counter[i]=temp_counter[i-1]
        else:
            temp_counter[i]=temp_counter[i-1]+1
    left=0
    right=k
    minFinder=float("inf")
    while right<n+1:
        current=temp_counter[right]-temp_counter[left]
        minFinder=min(current,minFinder)
        left=left+1
        right=right+1
    print(minFinder)
        