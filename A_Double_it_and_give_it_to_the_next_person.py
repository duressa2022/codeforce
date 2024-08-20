def solver():
    for _ in range(int(input())):
        string=input()
        result=string+string[::-1]
        print(result)
solver()