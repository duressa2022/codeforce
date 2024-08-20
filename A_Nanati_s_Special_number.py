string="abcdefghijklmnopqrstuvwxyz"
hash_map={string[index]:index+1 for index in range(26)}
t=int(input())
for i in range(t):
    n=int(input())
    message=input()
    maxFinder="a"
    for char in message:
        if hash_map[char]>hash_map[maxFinder]:
            maxFinder=char
    print(hash_map[maxFinder])