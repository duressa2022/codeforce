n=int(input())
for i in range(n):
    string=input()
    if len(string)<=10:
        print(string)
    else:
        result=""
        result+=string[0]
        result+=str(len(string)-2)
        result+=string[-1]
        print(result)