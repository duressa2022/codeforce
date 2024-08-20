def solver():
    vowels={"a","e","i","o","u","y"}
    length=int(input())
    string=input()
    result=[]
    i=0
    while i<length:
        if string[i] not in vowels:
            result.append(string[i])
            i=i+1
        else:
            result.append(string[i])
            i=i+1
            while i<length and string[i] in vowels:
                i=i+1

    print("".join(result))
solver()